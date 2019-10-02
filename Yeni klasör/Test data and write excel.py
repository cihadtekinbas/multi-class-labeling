#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import scipy.io
import xlsxwriter

# DATAPATH :        '/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/'

def readData(dataPath):
    testArticle = scipy.io.loadmat(dataPath + "testArticle.mat");
    testTag = scipy.io.loadmat(dataPath + 'testTags.mat');

    trainArticle = scipy.io.loadmat(dataPath + 'trainArticle.mat');

    trainTag = scipy.io.loadmat(dataPath + 'trainTags.mat');


    
    binaryTestArticle = scipy.io.loadmat(dataPath+'binary/binaryTestArticle.mat');
    binaryTrainArticle = scipy.io.loadmat(dataPath+'binary/binaryTrainArticle.mat');

    L1normTestArticle = scipy.io.loadmat(dataPath+'L1norm/L1testArticle.mat');
    L1normTrainArticle = scipy.io.loadmat(dataPath+'L1norm/L1trainArticle.mat');

    L2normTestArticle = scipy.io.loadmat(dataPath+'L2norm/L2testArticle.mat');
    L2normTrainArticle = scipy.io.loadmat(dataPath+'L2norm/L2trainArticle.mat');
    

    trainTag = trainTag.get('trainTags')
    testTag = testTag.get('testTags')

    trainArticle = trainArticle.get('trainArticle')
    testArticle = testArticle.get('testArticle')
    
    binaryTestArticle = binaryTestArticle.get('binaryTestArticle')
    binaryTrainArticle = binaryTrainArticle.get('binaryTrainArticle')

    L1normTestArticle = L1normTestArticle.get('L1testArticle')
    L1normTrainArticle = L1normTrainArticle.get('L1trainArticle')

    L2normTestArticle = L2normTestArticle.get('L2testArticle')
    L2normTrainArticle = L2normTrainArticle.get('L2trainArticle')
    
    return trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle
   # return trainArticle, testArticle, trainTag, testTag


def SVMLearning(trainArticle, testArticle, trainTag, testTag,num,num2):
    svc = SVC(kernel="linear")
    scores = []
    truePositiveScore = []
    confusionMatrix = []

    for i in range(0, 10):
        svc.fit(trainArticle, trainTag[i, :])
        predictResults = svc.predict(testArticle)

        confMatrix = confusion_matrix(testTag[i, :], predictResults)
        positiveScore = ((confMatrix[1, 1]) / (confMatrix[1, 1] + confMatrix[1, 0]))
        score = ((confMatrix[0, 0] + confMatrix[1, 1]) / (
                    confMatrix[0, 0] + confMatrix[1, 1] + confMatrix[0, 1] + confMatrix[1, 0]))

        scores.append(score)
        truePositiveScore.append(positiveScore)
        confusionMatrix.append(confMatrix)
    
    print(scores)
    for j in range(len(scores)):
        worksheet.write(num2+j, num, scores[j])

        
    
    print('--------------')
    print(truePositiveScore)
    for j in range(len(truePositiveScore)):
        worksheet.write(num2+j, num+1, truePositiveScore[j])
    print('--------------')
    print(confusionMatrix)
   
    if num ==11:
        num=15
    if num==9:
         num=11
    if num ==13:
        num=19
        
    for j in range(len(confusionMatrix)):
        x=0
        for i in range(2):
            for z in range(2):
                worksheet2.write(num2+j,num+x,confusionMatrix[j][i][z])
                x+=1
    print('--------------')


trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle = readData("C:\\Users\\asus\\data\\")
#trainArticle, testArticle, trainTag, testTag = readData("C:\\Users\\asus\\data\\")

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

#worksheet=workbook.get_worksheet_by_name("Sheet1")

print("*******normal********")
SVMLearning(trainArticle, testArticle, trainTag, testTag,7,11)
''''
print("********binary*******")
SVMLearning(binaryTrainArticle, binaryTestArticle, trainTag, testTag,9,11)

print("*********L1**********")
SVMLearning(L1normTrainArticle, L1normTestArticle, trainTag, testTag,11,11)
print("*********L2**********")
SVMLearning(L2normTrainArticle, L2normTestArticle, trainTag, testTag,13,11)
''''
workbook.close()



# In[3]:





# In[42]:


num=11
if num!=7:
        num+=2
print(num)


# In[25]:


for i in range(1,3):
    print(i)


# In[7]:


workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()
print("*******normal********")
SVMLearning(trainArticle, testArticle, trainTag, testTag,7,11)


# In[ ]:




