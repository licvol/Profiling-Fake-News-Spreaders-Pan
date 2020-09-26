#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mars 06 21:18:08 2020
@author: drMohamedLichouri
@email: licvol@gmail.com

@Description: This script will permit us to investigate the impact of some features like:
    stopwords removal, punctuation removal, normalization, stemming, PosTagging, Lemmatizer.
On the problem of Text classification.
"""
import argparse
import glob
import pandas as pd
import pickle
import nltk
import os
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

from nltk.stem import SnowballStemmer # for english
from nltk.stem import WordNetLemmatizer
import xml.etree.ElementTree as ET

def xmlToCorpusTest(xmlDocs):
    xmlFiles = sorted(xmlDocs)
    textList = []
    idsList = []
    for txt in xmlFiles:
        tree = ET.parse(txt)
        root = tree.getroot()
        dcs = root.findall("documents")
        dcTxt = [d.findall('document') for d in dcs][0]
        xmlText = [t.text for t in dcTxt]
        ids = txt.split('/')[-1][:-4] 
        textList.append(xmlText)
        idsList.append(ids)
    return textList, idsList

def readTestDataset(inputDir):
    esPath = inputDir + '/es/'
    enPath = inputDir + '/en/'
    esDirXmls = glob.glob(esPath + '*.xml')
    enDirXmls = glob.glob(enPath + '*.xml')
    xmlTextEs, idsEs = xmlToCorpusTest(esDirXmls)
    xmlTextEn, idsEn = xmlToCorpusTest(enDirXmls)
    return xmlTextEs, idsEs, xmlTextEn, idsEn


# remove emoji
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    res = []
    for s in text:
        out = emoji_pattern.sub(r'', str(s))
        res.append(out)
    return res

# remove ponctuations
def removePunctuation(text):
    lst = string.punctuation + '…–'
    res = []
    for s in text:
        for l in lst:
            s = s.replace(l,'')
        res.append(s)
    return res

# filter stopwords
def removeStopWord(text, lang):
  stop = stopwords.words(lang)
  res = []
  for s in text:
      out = ' '.join([word for word in str(s).split() if word not in (stop)])
      res.append(out)
  return res


# apply steeming
def applyStemmer(text, lang):
  st = SnowballStemmer(lang)
  res = []
  for s in text:
      out = ' '.join([st.stem(word) for word in str(s).split()])
      res.append(out)
  return res


# apply pos tagging
def applyPosTag(text):
  wpt = nltk.WordPunctTokenizer()
  # sentences 1
  out = []
  for s in text:
    text1 = wpt.tokenize(str(s))
    text_tagged = nltk.pos_tag(text1)
    new_text = []
    new_tag = []
    for word in text_tagged:
        new_text.append(word[0])
        new_tag.append(word[1])
    #s1 = new_text + new_tag
    out.append(' '.join(new_tag))
  return out

# apply lemmatizer
def applyLemme(text):
    wnl = WordNetLemmatizer()
    outText = []
    for s in text:
        lm = [wnl.lemmatize(i,j[0].lower()) if j[0].lower() in ['a','n','v'] else wnl.lemmatize(i) for i,j in nltk.pos_tag(word_tokenize(str(s)))]
        outText.append(' '.join(lm))
    return outText 

# features extraction
def featuresExtraction(xmlText, ids, lang):
    dataTestText = xmlText
    # id
    dataTestId = ids
    # features
    dataTestText = remove_emoji(dataTestText)
    dataTestText = removePunctuation(dataTestText)
    dataTestText = removeStopWord(dataTestText, lang)
    dataStemTest = applyStemmer(dataTestText, lang)
    dataPosTagTest = applyPosTag(dataTestText) 
    dataLemmeTest = applyLemme(dataTestText)
    dataTest = [' '.join([m,n,p,q]) for m,n,p,q in zip(dataTestText, dataStemTest, dataPosTagTest, dataLemmeTest)]
    # vectorize
    # Initial model selection process
    if lang == 'english':
        file = open('tfidfEn.pkl', 'rb')
    else:
        file = open('tfidfEs.pkl','rb')
    vectorizer = pickle.load(file)
    X_test = vectorizer.transform(dataTest)
    return X_test, dataTestId

# train and test
def trainAndTest(X_test, id_test, output, lang):
    outp = output + '/' + lang
    if not os.path.exists(outp):
        os.mkdir(outp)
    # Initial model selection process
    if lang == 'en':
        file = open('modelEn_LSVC.pkl', 'rb')
    else:
        file = open('modelEs_LSVC.pkl','rb')
    model = pickle.load(file)
    # start train and test phase
    #Prediction  
    y_pred = model.predict(X_test)
    for y, idx in zip(y_pred, list(id_test)):
        filename = outp + '/' + idx +'.xml'
        print('Predicting file %s'%filename)
        print('='*20)
        with open(filename,'w') as out:
            out.write('<author id="%s"'%idx)
            out.write('\n')
            out.write('lang="%s"'%lang)
            out.write('\n')
            out.write('type="%s"'%y)
            out.write('\n')
            out.write('/>')  


def defArgparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--corpus', required=False, help="input training directory")  
    parser.add_argument('-r','--run', required=False, help="input run directory")  
    parser.add_argument('-o','--output', required=True, help="output directory")  
    #parser.add_argument('arg',nargs='*') #use '+' for 1 or more args(instead of 0 or more)
    args = parser.parse_args()
    #NOTE: args with'-' have it replaced with'-'
    if args.run:
        xmlTextEs, idsEs, xmlTextEn, idsEn  = readTestDataset(args.run)
    elif args.corpus:
        xmlTextEs, idsEs, xmlTextEn, idsEn  = readTestDataset(args.corpus)
        
    output = args.output
    
    X_testEn, dataTestIdEn = featuresExtraction(xmlTextEn, idsEn, 'english')
    X_testEs, dataTestIdEs = featuresExtraction(xmlTextEs, idsEs, 'spanish')
    return output, X_testEn, dataTestIdEn, X_testEs, dataTestIdEs

if __name__ == "__main__":
    
    output, X_testEn, dataTestIdEn, X_testEs, dataTestIdEs = defArgparse()


    # start train and test for En
    trainAndTest(X_testEn, dataTestIdEn, output, 'en')
    trainAndTest(X_testEs, dataTestIdEs, output, 'es')
    