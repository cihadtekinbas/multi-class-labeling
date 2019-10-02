#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[31]:


from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import scipy.io
import numpy as np

# DATAPATH :        '/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/'

def readData(dataPath):
    testArticle = scipy.io.loadmat(dataPath + "testArticle.mat")
    testTag = scipy.io.loadmat(dataPath + 'testTags.mat')
    trainArticle = scipy.io.loadmat(dataPath + 'trainArticle.mat')
    trainTag = scipy.io.loadmat(dataPath + 'trainTags.mat')

    trainTag = trainTag.get('trainTags')
    testTag = testTag.get('testTags')

    '''
    binaryTestArticle = scipy.io.loadmat(dataPath+'binary/binaryTestArticle.mat');
    binaryTrainArticle = scipy.io.loadmat(dataPath+'binary/binaryTrainArticle.mat');
    
    '''
    '''
    L1normTestArticle = scipy.io.loadmat(dataPath+'L1norm/L1testArticle.mat');
    L1normTrainArticle = scipy.io.loadmat(dataPath+'L1norm/L1trainArticle.mat');
    '''
    '''
    L2normTestArticle = scipy.io.loadmat(dataPath+'L2norm/L2testArticle.mat');
    L2normTrainArticle = scipy.io.loadmat(dataPath+'L2norm/L2trainArticle.mat');
    '''
    '''
    trainTag = trainTag.get('trainTags')
    testTag = testTag.get('testTags')
    '''
    trainArticle = trainArticle.get('trainArticle')
    testArticle = testArticle.get('testArticle')
    '''
    binaryTestArticle = binaryTestArticle.get('binaryTestArticle')
    binaryTrainArticle = binaryTrainArticle.get('binaryTrainArticle')
    '''
    
    '''
    L1normTestArticle = L1normTestArticle.get('L1testArticle')
    L1normTrainArticle = L1normTrainArticle.get('L1trainArticle')



    L2normTestArticle = L2normTestArticle.get('L2testArticle')
    L2normTrainArticle = L2normTrainArticle.get('L2trainArticle')
    '''
    # return trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle
    # return trainArticle, testArticle, trainTag, testTag
    return trainArticle,testArticle,trainTag, testTag
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



def SVMLearning(trainArticle, testArticle, trainTag, testTag,i,j):
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
    print('--------------')
    print(truePositiveScore)
    print('--------------')
    print(confusionMatrix)
    print('--------------')


# trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle = readData('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/')
trainArticle, testArticle, trainTag, testTag = readData("C:\\Users\\asus\\data\\")
print(trainArticle.shape,testArticle.shape,trainTag.shape,testTag.shape)

for i in range(0,10):
    for j in range(0,10):
        if i!=j:
            print("iteration: ", i,j)
            trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(trainArticle, testArticle, trainTag, testTag,i,j)
            SVMLearning(trainArticle1, testArticle1, trainTag1, testTag1,i,j)





# In[ ]:




