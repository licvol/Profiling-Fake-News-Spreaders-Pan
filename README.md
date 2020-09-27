# Profiling-Fake-News-Spreaders-Pan@CLEF2020
This repository deals with the problem of Profiling Fake News Spreaders on Twitter: https://pan.webis.de/clef20/pan20-web/author-profiling.html

In this workshop, we have participated in both English and Spanish subTasks. Our approach is based on the unification of multiple TF-IDF features as well as three Morphological processes (Lemmatization, Stemming and Part-Of-Speech Tagging). 

# Clone and unzip models
At first, you need to clone this repository:

     git clone https://github.com/computational-linguistics-department/Profiling-Fake-News-Spreaders-Pan.git

If you are in Unix environment, you can unzip the two models using:

     7z e tfidfEn.7z
     7z e tfidfEs.7z
In windows you can use any .7z unpacking software.

# Dataset
For the dataset you can refer to this website: https://pan.webis.de/data.html .The data is also shared in zenodo: https://zenodo.org/record/4039435#.X28orYbjLVQ
# How to use:
You can run the code in this repository for both training and evaluating phases by using one of these commands:

For training purpose: 

     python software1.py -c nameOfTrainFolder -o nameOfOutputFolder
     
For test purpose: 

     python software1.py -r nameOfTestFolder -o nameOfOutputFolder
	 
# Contact
Please email to authors if you have question.<br />
Mohamed Lichouri (licvol@gmail.com)<br />
Mourad Abbas (m_abbas04@yahoo.fr)<br />

# Link to the paper:

    Mohamed Lichouri, Mourad Abbas, and Besma Benaziz. Profiling Fake News Spreaders on Twitter-based on TFIDF 
    Features and Morphological Process—Notebook for PAN at CLEF 2020. In Linda Cappellato, Carsten Eickhoff, 
    Nicola Ferro, and Aurélie Névéol, editors, CLEF 2020 Labs and Workshops, Notebook Papers, September 2020. 
    CEUR-WS.org. https://pan.webis.de/downloads/publications/papers/lichouri_2020.pdf

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
