from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import scipy.io

# DATAPATH :        '/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/'

def readData(dataPath):
    testArticle = scipy.io.loadmat(dataPath+'/testArticle.mat');
    testTag = scipy.io.loadmat(dataPath+'/testTag.mat');

    trainArticle = scipy.io.loadmat(dataPath+'/trainArticle.mat');
    trainTag = scipy.io.loadmat(dataPath+'/trainTag.mat');
    
    ''' 
    binaryTestArticle = scipy.io.loadmat(dataPath+'binary/binaryTestArticle.mat');
    binaryTrainArticle = scipy.io.loadmat(dataPath+'binary/binaryTrainArticle.mat');

    L1normTestArticle = scipy.io.loadmat(dataPath+'L1norm/L1testArticle.mat');
    L1normTrainArticle = scipy.io.loadmat(dataPath+'L1norm/L1trainArticle.mat');

    L2normTestArticle = scipy.io.loadmat(dataPath+'L2norm/L2testArticle.mat');
    L2normTrainArticle = scipy.io.loadmat(dataPath+'L2norm/L2trainArticle.mat');
    '''
    
    trainTag = trainTag.get('trainTags')
    testTag = testTag.get('testTags')

    trainArticle = trainArticle.get('trainArticle')
    testArticle = testArticle.get('testArticle')
    ''' 
    binaryTestArticle = binaryTestArticle.get('binaryTestArticle')
    binaryTrainArticle = binaryTrainArticle.get('binaryTrainArticle')
    
    L1normTestArticle = L1normTestArticle.get('L1testArticle')
    L1normTrainArticle = L1normTrainArticle.get('L1trainArticle')
    
    L2normTestArticle = L2normTestArticle.get('L2testArticle')
    L2normTrainArticle = L2normTrainArticle.get('L2trainArticle')
    '''
    #return trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle
    return trainArticle, testArticle, trainTag, testTag
def SVMLearning(trainArticle, testArticle, trainTag, testTag):
    
    svc = SVC(kernel = "linear")
    scores = []
    truePositiveScore = []
    confusionMatrix = []
    
    for i in range(2,3):
        svc.fit(trainArticle, trainTag[i,:])
        predictResults = svc.predict(testArticle)

        confMatrix = confusion_matrix(testTag[i,:], predictResults)
        positiveScore = ((confMatrix[1,1])/(confMatrix[1,1]+confMatrix[1,0]))
        score = ((confMatrix[0,0]+confMatrix[1,1])/(confMatrix[0,0]+confMatrix[1,1]+confMatrix[0,1]+confMatrix[1,0]))
        
        scores.append(score)
        truePositiveScore.append(positiveScore)
        confusionMatrix.append(confMatrix)

    print(scores)
    print('--------------')
    print(truePositiveScore)
    print('--------------')
    print(confusionMatrix)
    print('--------------')

#trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle = readData('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/')
trainArticle, testArticle, trainTag, testTag = readData('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/')
SVMLearning(trainArticle,testArticle,trainTag,testTag)
