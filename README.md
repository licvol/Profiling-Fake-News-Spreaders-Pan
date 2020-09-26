# Profiling-Fake-News-Spreaders-Pan@CLEF2020
This repository cover our submission to the Pan@CLEF2020 workshop that deals with the problem of Profiling Fake News Spreaders on Twitter: https://pan.webis.de/clef20/pan20-web/author-profiling.html

Our submited system and despite its simplicity has ranked in 45 from 66 participating teams. In this workshop, we have participated in both English and Spanish subTasks. We have opted for a simple unification approach of multiple TF-IDF features as well as three Morphological processes (Lemmatization, Stemming and Part-Of-Speech Tagging). 

This setup has permit us to obtain the following scores:  	0.5850 (English), 0.7600 (Spanish), and 	0.6725 (Average).

# Clone and unzip models
In the start you have to clone this repository:

     git clone https://github.com/computational-linguistics-department/Profiling-Fake-News-Spreaders-Pan.git

If you are in Unix environment, you can unzip the two models using:

     7z e tfidfEn.7z
     7z e tfidfEs.7z
In windows or others you can use any .7z unpacking software.

# How to use:
You can run the code in this repository for both training and evaluating phases by using one of these commands:

For training purpose: 

     python software1.py -c nameOfTrainFolder -o nameOfOutputFolder
     
For test purpose: 

     python software1.py -r nameOfTestFolder -o nameOfOutputFolder
	 
# Contact
Please email to authors if you have question.<br />
Mohamed Lichouri (m.lichouri@crstdla.dz)<br />
Mourad Abbas (m.abbas@crstdla.dz)<br />
Besma Benaziz (b.benaziz@crstdla.dz)



# Citing

      @InProceedings{lichouri:2020,
        author =              {Mohamed Lichouri and Mourad Abbas and Besma Benaziz},
        booktitle =           {{CLEF 2020 Labs and Workshops, Notebook Papers}},
        crossref =            {pan:2020},
        editor =              {Linda Cappellato and Carsten Eickhoff and Nicola Ferro and Aur{\'e}lie N{\'e}v{\'e}ol},
        month =               sep,
        publisher =           {CEUR-WS.org},
        title =               {{Profiling Fake News Spreaders on Twitter-based on TFIDF Features and Morphological Process---Notebook for PAN at CLEF 2020}},
        url =                 {},
        year =                2020
        }
