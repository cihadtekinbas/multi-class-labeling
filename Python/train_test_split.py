import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split
import scipy.io
from sklearn.naive_bayes import GaussianNB

def Average(lst): 
    return sum(lst) / len(lst)

# /home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/150articlesForEachCategoryMatrix.mat

# /home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/150articlesForEachCategoryMatrixTarget.mat

def prepareData(featureDataPath, targetDataPath):
    
    articleFeatures = scipy.io.loadmat(featureDataPath);
    articleFeatures = articleFeatures.get('finalDataMatrix')

    articleTags = scipy.io.loadmat(targetDataPath)
    articleTags = articleTags.get('finalDataMatrixTarget')

    return articleFeatures, articleTags

def train_test_split(articleFeatures, articleTags, splitNumber):

    articleNumber = 150
    wordNumber = 115427
    totalArticleNumber = 1500
    # Creating train articleFeatures.
    trainArticleFeatures = np.zeros((splitNumber,wordNumber))
    for i in range(0,10):
        startingIndex = articleNumber * i
        endingIndex = articleNumber * i + splitNumber
        trainArticleFeatures = np.concatenate((trainArticleFeatures, np.array(articleFeatures[startingIndex:endingIndex,:].toarray())))
    
    trainArticleFeatures = trainArticleFeatures[splitNumber:,:]

    # Creating test articleFeatures
    testArticleFeatures = np.zeros((articleNumber-splitNumber,wordNumber))
    for i in range(0,10):
        startingIndex = articleNumber * i + splitNumber
        endingIndex = startingIndex + articleNumber - splitNumber
        testArticleFeatures = np.concatenate((testArticleFeatures, np.array(articleFeatures[startingIndex:endingIndex,:].toarray())))
    
    testArticleFeatures = testArticleFeatures[articleNumber-splitNumber:,:]


    print(trainArticleFeatures.shape)
 
    print(testArticleFeatures.shape)

  
    CategoryNumber=10
    # Creating train articleFeatures.
    trainArticleTags = np.zeros((CategoryNumber,splitNumber))
    for i in range(0,10):
        startingIndex = articleNumber * i
        endingIndex = articleNumber * i + splitNumber
        trainArticleTags = np.concatenate((trainArticleTags, np.array(articleTags[:,startingIndex:endingIndex].toarray())),axis=1)
    
    trainArticleTags = trainArticleTags[:,splitNumber:]
    # Creating test articleFeatures
    testArticleTags = np.zeros((CategoryNumber,articleNumber-splitNumber))
    for i in range(0,10):
        startingIndex = articleNumber * i + splitNumber
        endingIndex = startingIndex + articleNumber - splitNumber
        testArticleTags = np.concatenate((testArticleTags, np.array(articleTags[:,startingIndex:endingIndex].toarray())),axis=1)
    
    testArticleTags = testArticleTags[:,articleNumber-splitNumber:]

    scipy.io.savemat('trainArticle',{'trainArticle':trainArticleFeatures})
    scipy.io.savemat('testArticle', {'testArticle':testArticleFeatures})
    scipy.io.savemat('trainTags', {'trainTags':trainArticleTags})
    scipy.io.savemat('testTags', {'testTags':testArticleTags})

def SVMLearning(train,target,education,music,film,food,police,health,women,children):
    
    scores = []

    svc = SVC()
    education_score = cross_val_score(svc,train,education,cv=3)
    scores.append(Average(education_score))

    music_score = cross_val_score(svc,train,music,cv=3)
    scores.append(Average(music_score))

    film_score = cross_val_score(svc,train,film,cv=3)
    scores.append(Average(film_score))

    food_score = cross_val_score(svc,train,food,cv=3)
    scores.append(Average(food_score))

    police_score = cross_val_score(svc,train,police,cv=3)
    scores.append(Average(police_score))

    health_score = cross_val_score(svc,train,health,cv=3)
    scores.append(Average(health_score))

    women_score = cross_val_score(svc,train,women,cv=3)
    scores.append(Average(women_score))

    children_score = cross_val_score(svc,train,children,cv=3)
    scores.append(Average(children_score))

    print(scores)

article, tag = prepareData("/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/150articlesForEachCategoryMatrix.mat",'/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/150articlesForEachCategoryMatrixTarget.mat')
train_test_split(article, tag, 100)


'''
nb = GaussianNB()
train = train[:,0:50000].toarray()
education_score = cross_val_score(nb,train,education,cv=3)
scores.append(Average(education_score))

music_score = cross_val_score(nb,train,music,cv=3)
scores.append(Average(music_score))

film_score = cross_val_score(nb,train,film,cv=3)
scores.append(Average(film_score))

food_score = cross_val_score(nb,train,food,cv=3)
scores.append(Average(food_score))

police_score = cross_val_score(nb,train,police,cv=3)
scores.append(Average(police_score))

health_score = cross_val_score(nb,train,health,cv=3)
scores.append(Average(health_score))

women_score = cross_val_score(nb,train,women,cv=3)
scores.append(Average(women_score))

children_score = cross_val_score(nb,train,children,cv=3)
scores.append(Average(children_score))
'''


