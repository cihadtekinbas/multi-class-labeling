#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import scipy.io
import xlsxwriter
import numpy as np

def main(pathoffile,pathofname):

    def readData(dataPath):
        testArticle = scipy.io.loadmat(dataPath + "testArticle.mat");
        testTag = scipy.io.loadmat(dataPath + 'testTags.mat');

        trainArticle = scipy.io.loadmat(dataPath + 'trainArticle.mat');

        trainTag = scipy.io.loadmat(dataPath + 'trainTags.mat');



        binaryTestArticle = scipy.io.loadmat(dataPath+'binaryTestArticle.mat');
        binaryTrainArticle = scipy.io.loadmat(dataPath+'binaryTrainArticle.mat');

        L1normTestArticle = scipy.io.loadmat(dataPath+'L1testArticle.mat');
        L1normTrainArticle = scipy.io.loadmat(dataPath+'L1trainArticle.mat');

        L2normTestArticle = scipy.io.loadmat(dataPath+'L2testArticle.mat');
        L2normTrainArticle = scipy.io.loadmat(dataPath+'L2trainArticle.mat');


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
    def SVMLearningFirst(trainArticle, testArticle, trainTag, testTag,num,num2):
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
    def SplitMatrixSecond(trainArticle, testArticle, trainTag, testTag,num):
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
    def SVMLearningThird(trainArticle, testArticle, trainTag, testTag,i,num,num2):
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
        worksheet.write(num2+i, num, scores[0])



        print('--------------')
        print(truePositiveScore)
        worksheet.write(num2+i, num+1, truePositiveScore[0])
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
                worksheet2.write(num2+i,num+x,confusionMatrix[0][e][z])
                x+=1
        print('--------------')




    def SVMLearningSecond(trainArticle, testArticle, trainTag, testTag,i,j,num,num2):
        if i!=j:
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

            worksheet3.write(6+i*9+j+i,num, scores[0])


            print('--------------')
            print(truePositiveScore)

            worksheet3.write(6+i*9+j+i, num+1, truePositiveScore[0])
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
                    worksheet4.write(6+i*9+j+i,num+x,confusionMatrix[0][e][z])
                    x+=1
            print('--------------')
        else:
            worksheet3.write(6+i*9+j+i,num, 0)
            worksheet3.write(6+i*9+j+i, num+1, 0)
            if num ==11:
                num=15
            if num==9:
                num=11
            if num ==13:
                num=19
            x=0
            for e in range(2):
                for z in range(2):
                    worksheet4.write(6+i*9+j+i,num+x,0)
                    x+=1







    trainArticle, testArticle, trainTag, testTag, binaryTrainArticle, binaryTestArticle, L1normTrainArticle ,L1normTestArticle, L2normTrainArticle, L2normTestArticle = readData(pathoffile)
    #trainArticle, testArticle, trainTag, testTag = readData("C:\\Users\\asus\\data\\")

    workbook = xlsxwriter.Workbook(pathofname+'.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet()
    worksheet3 = workbook.add_worksheet()
    worksheet4 = workbook.add_worksheet()
    #worksheet=workbook.get_worksheet_by_name("Sheet1")

    print("*******Not Equal Sample Size********")
    SVMLearningFirst(trainArticle, testArticle, trainTag, testTag,7,11)
    SVMLearningFirst(binaryTrainArticle, binaryTestArticle, trainTag, testTag,9,11)
    SVMLearningFirst(L1normTrainArticle, L1normTestArticle, trainTag, testTag,11,11)
    SVMLearningFirst(L2normTrainArticle, L2normTestArticle, trainTag, testTag,13,11)
    print("*******Binary Equal Sample Size********")

    for i in range(0,10):
        for j in range(0,10):
                print("iteration: ", i,j)
                trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(trainArticle, testArticle, trainTag, testTag,i,j)
                SVMLearningSecond(trainArticle1, testArticle1, trainTag1, testTag1,i,j,7,11)
                trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(binaryTrainArticle, binaryTestArticle, trainTag, testTag,i,j)
                SVMLearningSecond(trainArticle1, testArticle1, trainTag1, testTag1,i,j,9,11)
                trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(L1normTrainArticle, L1normTestArticle, trainTag, testTag,i,j)
                SVMLearningSecond(trainArticle1, testArticle1, trainTag1, testTag1,i,j,11,11)
                trainArticle1, testArticle1, trainTag1, testTag1=SplitMatrix(L2normTrainArticle, L2normTestArticle, trainTag, testTag,i,j)
                SVMLearningSecond(trainArticle1, testArticle1, trainTag1, testTag1,i,j,13,11)
    print("*******Equal Sample Size********")

    for i in range(0,10):
        print("iteration: ", i)
        trainArticle1, testArticle1, trainTag1, testTag1 = SplitMatrixSecond(trainArticle, testArticle, trainTag, testTag,i)
        SVMLearningThird(trainArticle1, testArticle1, trainTag1, testTag1,i,7,21)
        trainArticle1, testArticle1, trainTag1, testTag1 = SplitMatrixSecond(binaryTrainArticle, binaryTestArticle, trainTag, testTag,i)
        SVMLearningThird(trainArticle1, testArticle1, trainTag1, testTag1,i,9,21)
        trainArticle1, testArticle1, trainTag1, testTag1 = SplitMatrixSecond(L1normTrainArticle, L1normTestArticle, trainTag, testTag,i)
        SVMLearningThird(trainArticle1, testArticle1, trainTag1, testTag1,i,11,21)
        trainArticle1, testArticle1, trainTag1, testTag1 = SplitMatrixSecond(L2normTrainArticle, L2normTestArticle, trainTag, testTag,i)
        SVMLearningThird(trainArticle1, testArticle1, trainTag1, testTag1,i,13,21)

    workbook.close()
    
    
    
    
main("C:\\Users\\asus\\Desktop\\Yeni klasör (11)\\4v3\\","4v3")
'''
main("E:\\200\\200creationv1\\","200creationv1")

main("E:\\400\\400updatev1\\","400updatev1")
main("E:\\400\\400creationv1\\","400creationv1")

main("E:\\800\\800updatev1\\","800updatev1")
main("E:\\800\\800creationv1\\","800creationv1")

main("E:\\1600\\1600updatev1\\","1600updatev1")
main("E:\\1600\\1600creationv1\\","1600creationv1")
'''


# In[ ]:





# In[ ]:





# In[ ]:




