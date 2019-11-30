import sys
import heapq_max
import heapq
import pygtrie
import numpy as np
import shelve
from scipy import spatial
import math
from nltk.corpus import reuters

#open glove data set
def readdata():
    trie = pygtrie.StringTrie()
    db = shelve.open("/home/saidaltindis/Desktop/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/shelve_dict")

    #Set categories 
    tags = reuters.categories()

    tag_dict = {}
    print(1)

    #Find all tags' vector
    for key in tags:  # <- 1
        try:
            if '-' in key:
                keys = key.split('-')
                try:
                    key_1 = np.asarray(db[key[0]], dtype="float64")
                    key_2 = np.asarray(db[key[1]], dtype="float64")
                    tag_dict[key] = (key_1+key_2)/2
                    trie[key] = (key_1+key_2)/2
                    db.sync()
                except KeyError:
                    print("[ERROR] -> Tag \'" + key + '\' is not found in GloVe. Contains (-)' )
            else:
                data = np.asarray(db[key], dtype="float64")
                tag_dict[key] = data  # <- 1
                trie[key] = data
                db.sync()
        except KeyError:
            print("[ERROR] -> Tag \'" + key + '\' is not found in GloVe.' )
            
    print("[INFO] -> Reading tags is finished.")
    tm = db.keys()
    print("[INFO] -> All words are adding to trie.")
    data = []
    count = 0
    #Add all words vector to trie
    for x in tm:
        trie[x] = np.asarray(db[x], dtype="float64")
    print("[INFO] -> Adding words to trie is finished.")
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

    print("[INFO] -> 1st and 2nd loops end.")
    for x in trie:
        for y in tag_dict:
                result=spatial.distance.cosine(trie[x],tag_dict[y])
                heapq_max.heappush_max(min_list[y],(result,x))
                if len(min_list[y])>number:
                    heapq_max.heappop_max(min_list[y])

    '''
    for x in trie:
        for y in tag_dict.keys():
            vector = tag_dict.get(y)
            if type(vector) is list:
                try:
                    print("list")
                    result1 = spatial.distance.cosine(trie[x],vector[0])
                    result2 = spatial.distance.cosine(trie[x],vector[1])
                    minResult = min(result1, result2)
                    heapq_max.heappush_max(min_list[y],(minResult,x))
                    if len(min_list[y]) > number:
                        heapq_max.heappop_max(min_list[y])
                
                except KeyError:
                    print("[ERROR] -> Key error occured in 'if' ")
                except ValueError:
                    print("[ERROR] -> Value error occured in 'if' ")

            else:
                print("not list")
                print(vector)
                try:
                    result=spatial.distance.cosine(trie[x],vector)
                    heapq_max.heappush_max(min_list[y],(result,x))
                    if len(min_list[y])>number:
                        heapq_max.heappop_max(min_list[y])
                except KeyError:
                    print("[ERROR] -> Key error occured in 'else' ")
                except ValueError:
                    print("[ERROR] -> Value error occured in 'else' ")
    '''

    print("[INFO] ->  3rd loop end.")
    for name in min_list:
        
        length=len(min_list[name])
        for i in range(length):
            out=heapq_max.heappop_max(min_list[name])
            if name!=out[1]:
                detail_info[name].append(out)
                name_list[name].append(out[1])
        detail_info[name].append((0.0,name))
        name_list[name].append(name)
    
    print("[INFO] -> 4th loop end.")
    f1=open("./AllCatWords/words"+str(number),"w")  
    print("[INFO] -> Writing 1st file.")          
    for y in name_list:
        name_list[y].reverse()
        # print(name_list[y])
        f1.write(str(name_list[y]))
        f1.write("\n")
    f2=open("./AllCatWords/wordsD"+str(number),"w")
    print("[INFO] -> Writing 2nd file.")
    for y in detail_info:
        detail_info[y].reverse()
        # print(detail_info[y])
        f2.write(str(detail_info[y]))
        f2.write("\n")
    f3=open("./AllCatWords/wordsP"+str(number),"w")
    print("[INFO] -> Writing 3rd file.")
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
for i in range(0,3):
    print(str(i) + ". Iteration:")
    print(50*pow(2,i))
    writefile(50*pow(2,i),trie,tag_dict)
