import sys
import heapq_max
import heapq
import pygtrie
import numpy as np
import shelve
from scipy import spatial
import math

#open glove data set
def readdata():
    trie = pygtrie.StringTrie()
    db = shelve.open("/home/saidaltindis/Desktop/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/n_shelve_5_cat_reuters")

    #Set categories 
    tags =['earn', 'grain', 'crude', 'trade', 'interest']

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




def writefile(number,trie,tag_dict):

    detail_info={}
    name_list = {}  # eklenen kelimeleri ismini tut
    for i in tag_dict:
        name_list[i] = []
        # name_list[i].append(i)
        detail_info[i]=[]
    min_list = {}  # temp min list
    for j in tag_dict:
        min_list[j] = []

    for x in trie:
        for y in tag_dict:
                result=spatial.distance.cosine(trie[x],tag_dict[y])
                heapq_max.heappush_max(min_list[y],(result,x))
                if len(min_list[y])>number:
                    heapq_max.heappop_max(min_list[y])

                    

    for name in min_list:
        
        length=len(min_list[name])
        for i in range(length):
            out=heapq_max.heappop_max(min_list[name])
            if name!=out[1]:
                detail_info[name].append(out)
                name_list[name].append(out[1])
        detail_info[name].append((0.0,name))
        name_list[name].append(name)
    f1=open("./words"+str(number),"w")            
    for y in name_list:
        name_list[y].reverse()
        # print(name_list[y])
        f1.write(str(name_list[y]))
        f1.write("\n")
    f2=open("./wordsD"+str(number),"w")
    for y in detail_info:
        detail_info[y].reverse()
        # print(detail_info[y])
        f2.write(str(detail_info[y]))
        f2.write("\n")
    f3=open("./wordsP"+str(number),"w")
    for y in name_list:
        # name_list[y].reverse()
        # print(name_list[y])
        num1=0
        for j in name_list[y]:
            # num1=num1+1
            # if num1>1900 and num1 <2500:
            f3.write(str(j))
            if j!= name_list[y][-1]:
                f3.write("$#$")
        f3.write("\n")

trie,tag_dict=readdata()
for i in range(0,6):
    print(50*pow(2,i))
    writefile(50*pow(2,i),trie,tag_dict)
