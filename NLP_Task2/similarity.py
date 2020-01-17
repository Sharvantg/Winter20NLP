


# code will take all ".txt" files in the given folder path and calculate a similarity matrix between every combination of files
# code will calculate the matrix once without stemming and once with stemming



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import pandas as pd
import numpy
from nltk.stem.snowball import SnowballStemmer
import scipy


stopwords = set(stopwords.words('english'))

words=[]
folder_path = "/Users/sharvan/Desktop/NLP_Task"
file_list = os.listdir(folder_path)
doc = []
for i in file_list:
        if ".txt" in i:
                doc.append(i)

for iteration in range(2):
    vectorised_words = {}
    temp_words = []
    for i in doc:
            doc_path = folder_path+"/"+i
            fo=open(doc_path,"r",encoding='ISO-8859-1').read()
            tokens = word_tokenize(fo.lower())
            stemmer = SnowballStemmer("english")
            for word in tokens:
                    if word not in stopwords:
                        if iteration == 1:
                            word = stemmer.stem(word)
                        words.append(word)
                        temp_words.append(word)
            vectorised_words.update({i :temp_words})
            temp_words = []

    temp = set(words)
    unique_words = list(temp)


    dict = {}
    dict.update({"Document":doc})

    for i in unique_words:
        dict.update({i:[]})


    dframe = pd.DataFrame

    for i in doc:
        for j in unique_words:
            dict[j].append(vectorised_words[i].count(j))
            

    dframe  = pd.DataFrame(dict)
    dframe.set_index('Document',inplace = True)

#    print(dframe)
    no_stemming_similarity_dict  = {}
    stemming_similarity_dict  = {}
    
    for i in doc:
        stemming_similarity_dict.update({i : {}})
        no_stemming_similarity_dict.update({i : {}})

    if(iteration == 1):
        for i in doc:
            for j in doc:
                stemming_similarity_dict[i].update({j : 100*(1-scipy.spatial.distance.cosine(dframe.loc[i].values,dframe.loc[j].values))})
        
        stemming_similarity_dframe = pd.DataFrame(stemming_similarity_dict)
        print("\nsimilarity after stemming: ")
        print(stemming_similarity_dframe)
        print("\n");
    else:
        for i in doc:
            for j in doc:
                no_stemming_similarity_dict[i].update({j : 100*(1-scipy.spatial.distance.cosine(dframe.loc[i].values,dframe.loc[j].values))})
        
        no_stemming_similarity_dframe = pd.DataFrame(no_stemming_similarity_dict)
        print("\nsimilarity before stemming: ")
        print(no_stemming_similarity_dframe)
        print("\n");


