import sys
import heapq_max
import heapq
import pygtrie
import numpy as np
import shelve
from scipy import spatial
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd

#open glove data set

def readVectors():
    trie = pygtrie.StringTrie()
    db = shelve.open("n_shelve_10_cat")

    #Set categories 
    tags =["education", "music", "film", "food","police","health","women","children","technology","sport"]

    tag_dict = {}
    print(1)

    #Find all tags' vector
    for value in tags:  # <- 1
        data = np.asarray(db[value], dtype="float64")
        tag_dict[value] = data  # <- 1
        db.sync()
    print(2)
    tm = db.keys()
    print(3)
    data = []
    count = 0
    #Add all words vector to trie
    for x in tm:
        trie[x] = np.asarray(db[x], dtype="float64")
    print(4)
    return trie,tag_dict


def readWords():
    words = []
    words_index = 0
    with open('datapnew100.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for word in row:
                words.append(word)
    
    return words

def calculateDistances(words, trie):

    row_count = 0
    col_count = 0

    distances = np.zeros((1010,1010))

    for word in words:
        word_vector = trie.__getitem__(word)
        print(word)
        for word2 in words:
            word2_vector = trie.__getitem__(word2)
            distance = spatial.distance.cosine(word_vector,word2_vector)
            distances[row_count, col_count] = distance
            col_count = col_count + 1
            print(distance)
        
        row_count = row_count + 1
        col_count = 0

    np.save("distanceMatrix", distances)

def loadNumpyArray():
    distances = np.load("distanceMatrix.npy")
    df = pd.DataFrame(distances)

    #tags =["education", "music", "film", "food","police","health","women","children","technology","sport"]
	
    tags = [""]

    #cor_dist = np.corrcoef(distances)
    #plt.matshow(dist_pand.corr())
    f = plt.figure(figsize=(19, 15))
    plt.matshow(df.corr(), fignum=f.number)
    plt.xticks(range(df.shape[1]),tags, fontsize=14, rotation=45)
    plt.yticks(range(df.shape[1]),tags, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16);
    plt.show()  



#trie,tag_dict=readVectors()
#words = readWords()
#calculateDistances(words, trie)
loadNumpyArray()
