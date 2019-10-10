import scipy.io

path="/home/asus/Desktop/Project/Last/newData/1600withoutZero.mat"


matrix=scipy.io.loadmat(path)
matrix=matrix.get("temp")


# print(matrix)

import pygtrie

trie=pygtrie.StringTrie()

path="/home/asus/Desktop/Project/Matlab/project/vocabulary_article_sorted.txt"


file=open(path,"r")
j=1
for i in file:
    a=i.split(" ")
    trie[str(j)]=a[0]
    # trie[a[0]]=j

    j+=1
tags =["education", "music", "film", "food","police","health","women","children","technology","sport"]

num=1600
f=open("/home/asus/Desktop/Project/Last/newData/New Folder/wordlist"+str(num),"w")
for j in range(10):
    f.write(tags[j])
    f.write(",")
    for i in range(1,num):
        f.write(trie[str(matrix[j][i])])
        if i!=num-1:
            f.write(",")
    f.write("\n")
