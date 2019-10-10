from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import scipy.io
import numpy as np

# DATAPATH :        '/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/'

def readData(dataPath):
    #testArticle = scipy.io.loadmat(dataPath + "testArticle.mat")
    testTag = scipy.io.loadmat(dataPath + 'testTags.mat')
    #trainArticle = scipy.io.loadmat(dataPath + 'trainArticle.mat')
    trainTag = scipy.io.loadmat(dataPath + 'trainTags.mat')

    '''
    binaryTestArticle = scipy.io.loadmat(dataPath+'binary/binaryTestArticle.mat');
    binaryTrainArticle = scipy.io.loadmat(dataPath+'binary/binaryTrainArticle.mat');
    
    
    L1normTestArticle = scipy.io.loadmat(dataPath+'L1norm/L1testArticle.mat');
    L1normTrainArticle = scipy.io.loadmat(dataPath+'L1norm/L1trainArticle.mat');

    '''
    L2normTestArticle = scipy.io.loadmat(dataPath+'L2norm/L2testArticle.mat');
    L2normTrainArticle = scipy.io.loadmat(dataPath+'L2norm/L2trainArticle.mat');
    

    trainTag = trainTag.get('trainTags')
    testTag = testTag.get('testTags')
    
    '''
    trainArticle = trainArticle.get('trainArticle')
    testArticle = testArticle.get('testArticle')
    
    binaryTestArticle = binaryTestArticle.get('binaryTestArticle')
    binaryTrainArticle = binaryTrainArticle.get('binaryTrainArticle')
    
    L1normTestArticle = L1normTestArticle.get('L1testArticle')
    L1normTrainArticle = L1normTrainArticle.get('L1trainArticle')
    '''
    L2normTestArticle = L2normTestArticle.get('L2testArticle')
    L2normTrainArticle = L2normTrainArticle.get('L2trainArticle')
    
    # return trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle
    # return trainArticle, testArticle, trainTag, testTag
    # return binaryTrainArticle, binaryTestArticle, trainTag, testTag
    # return L1normTrainArticle, L1normTestArticle, trainTag, testTag
    return L2normTrainArticle, L2normTestArticle, trainTag, testTag

def SplitMatrix(trainArticle, testArticle, trainTag, testTag,num):
    SplitedNum=100
    SplitedNum2 = 50
    trainSelect = 11
    testSelect = 5
    
    # TRAIN ARTICLE
    first = trainArticle[num*SplitedNum:(num+1)*SplitedNum,:]
    first = first[0:99,:]

    trainArticleFeatures = first

    for i in range(0,10):
        if i != num:
            second = trainArticle[i*SplitedNum:(i*SplitedNum+trainSelect),:]
            trainArticleFeatures = np.concatenate((trainArticleFeatures,second))

    # TEST ARTICLE
    first = testArticle[num*SplitedNum2:(num+1)*SplitedNum2,:]
    first = first[0:45,:]

    testArticleFeatures = first

    for i in range(0,10):
        if i != num:
            second = testArticle[i*SplitedNum2:(i*SplitedNum2+testSelect),:]
            testArticleFeatures = np.concatenate((testArticleFeatures,second))
   
    # TRAIN TAG
    first=trainTag[num,num*SplitedNum:(num+1)*SplitedNum]
    first = first[0:99]

    trainArticleTags = first

    for i in range(0,10):
        if i != num:
            second = trainTag[num,i*SplitedNum:(i*SplitedNum+trainSelect)]
            trainArticleTags = np.concatenate((trainArticleTags,second))

    
    # TEST TAGS
    first=testTag[num,num*SplitedNum2:(num+1)*SplitedNum2]
    first = first[0:45]

    testArticleTags = first

    for i in range(0,10):
        if i != num:
            second = testTag[num,i*SplitedNum2:(i*SplitedNum2+testSelect)]
            testArticleTags = np.concatenate((testArticleTags,second))

    return trainArticleFeatures,testArticleFeatures,trainArticleTags,testArticleTags

def SVMLearning(trainArticle, testArticle, trainTag, testTag):
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


trainArticle, testArticle, trainTag, testTag = readData("/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/")
print(trainArticle.shape,testArticle.shape,trainTag.shape,testTag.shape)

for i in range(0,10):
    print("iteration: ", i)
    trainArticle1, testArticle1, trainTag1, testTag1 = SplitMatrix(trainArticle, testArticle, trainTag, testTag,i)
    SVMLearning(trainArticle1, testArticle1, trainTag1, testTag1)




