#!/usr/bin/env python
# coding: utf-8

# In[31]:


#!/usr/bin/env python
# coding: utf-8

# In[31]:


from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import scipy.io
import numpy as np
import xlsxwriter
# DATAPATH :        '/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/'

def readData(dataPath):
    testArticle = scipy.io.loadmat(dataPath + "testArticle.mat")
    trainArticle = scipy.io.loadmat(dataPath + 'trainArticle.mat')

    testTag = scipy.io.loadmat(dataPath + 'testTags.mat')
    trainTag = scipy.io.loadmat(dataPath + 'trainTags.mat')
    
    
    binaryTestArticle = scipy.io.loadmat(dataPath+'binary/binaryTestArticle.mat');
    binaryTrainArticle = scipy.io.loadmat(dataPath+'binary/binaryTrainArticle.mat');
   
    L1normTestArticle = scipy.io.loadmat(dataPath+'L1norm/L1testArticle.mat');
    L1normTrainArticle = scipy.io.loadmat(dataPath+'L1norm/L1trainArticle.mat');
    
    L2normTestArticle = scipy.io.loadmat(dataPath+'L2norm/L2testArticle.mat');
    L2normTrainArticle = scipy.io.loadmat(dataPath+'L2norm/L2trainArticle.mat');
    
    trainArticle = trainArticle.get('trainArticle')
    testArticle = testArticle.get('testArticle')
    
    trainTag = trainTag.get('trainTags')
    testTag = testTag.get('testTags')
    
    binaryTestArticle = binaryTestArticle.get('binaryTestArticle')
    binaryTrainArticle = binaryTrainArticle.get('binaryTrainArticle')
    
    L1normTestArticle = L1normTestArticle.get('L1testArticle')
    L1normTrainArticle = L1normTrainArticle.get('L1trainArticle')
  
    L2normTestArticle = L2normTestArticle.get('L2testArticle')
    L2normTrainArticle = L2normTrainArticle.get('L2trainArticle')

    return trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle
    # return trainArticle, testArticle, trainTag, testTag
    #return L2normTrainArticle,L2normTestArticle,trainTag, testTag
def SplitMatrix(trainArticle, testArticle, trainTag, testTag,num,num2):
    SplitedNum=100
    SplitedNum2=50
    trainArticleFeatures = np.concatenate((trainArticle[num*SplitedNum:(num+1)*SplitedNum,:], trainArticle[num2*SplitedNum:(num2+1)*SplitedNum,:]))
    testArticleFeatures= np.concatenate((testArticle[num*SplitedNum2:(num+1)*SplitedNum2,:], testArticle[num2*SplitedNum2:(num2+1)*SplitedNum2,:]))
    
    first=trainTag[num,num*SplitedNum:(num+1)*SplitedNum]
    second= trainTag[num,num2*SplitedNum:(num2+1)*SplitedNum]
    trainArticleTags = np.concatenate((first,second))


    first=testTag[num,num*SplitedNum2:(num+1)*SplitedNum2]
    second=testTag[num,num2*SplitedNum2:(num2+1)*SplitedNum2]
    testArticleTags = np.concatenate((first,second))
    return trainArticleFeatures,testArticleFeatures,trainArticleTags,testArticleTags



def SVMLearning(trainArticle, testArticle, trainTag, testTag,i,j,num,num2):
    svc = SVC(kernel="linear")
    scores = []
    truePositiveScore = []
    confusionMatrix = []

    svc.fit(trainArticle, trainTag)
    predictResults = svc.predict(testArticle)

    confMatrix = confusion_matrix(testTag, predictResults)
    positiveScore = ((confMatrix[1, 1]) / (confMatrix[1, 1] + confMatrix[1, 0]))
    score = ((confMatrix[0, 0] + confMatrix[1, 1]) / (
                confMatrix[0, 0] + confMatrix[1, 1] + confMatrix[0, 1] + confMatrix[1, 0]))

    scores.append(score)
    truePositiveScore.append(positiveScore)
    confusionMatrix.append(confMatrix)

    print(scores)

    worksheet.write(6+i*9+j,num, scores[0])
        
    
    print('--------------')
    print(truePositiveScore)

    worksheet.write(6+i*9+j, num+1, truePositiveScore[0])
    print('--------------')
    print(confusionMatrix)
    if num ==11:
        num=15
    if num==9:
         num=11
    if num ==13:
        num=19
        
  
    x=0
    for e in range(2):
        for z in range(2):
            worksheet2.write(6+i*9+j,num+x,confusionMatrix[0][e][z])
            x+=1
    print('--------------')


trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle = readData("C:\\Users\\asus\\data\\")
#trainArticle, testArticle, trainTag, testTag = readData("C:\\Users\\asus\\data\\")
print(trainArticle.shape,testArticle.shape,trainTag.shape,testTag.shape)
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()
for i in range(0,10):
    for j in range(0,10):
        if i!=j:
            print("iteration: ", i,j)
            trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(trainArticle, testArticle, trainTag, testTag,i,j)
            SVMLearning(trainArticle1, testArticle1, trainTag1, testTag1,i,j,7,11)
            trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(binaryTrainArticle, binaryTestArticle, trainTag, testTag,i,j)
            SVMLearning(trainArticle1, testArticle1, trainTag1, testTag1,i,j,9,11)
            trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(L1normTrainArticle, L1normTestArticle, trainTag, testTag,i,j)
            SVMLearning(trainArticle1, testArticle1, trainTag1, testTag1,i,j,11,11)
            trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(L2normTrainArticle, L2normTestArticle, trainTag, testTag,i,j)
            SVMLearning(trainArticle1, testArticle1, trainTag1, testTag1,i,j,13,11)

            

            
workbook.close()




# In[10]:


print(worksheet)


# In[22]:


workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet("ewrw")
worksheet2 = workbook.add_worksheet("wqeqeq")
worksheet.write(1, 1, 1)


# In[20]:


f


# In[29]:


print(scores)


# In[ ]:




