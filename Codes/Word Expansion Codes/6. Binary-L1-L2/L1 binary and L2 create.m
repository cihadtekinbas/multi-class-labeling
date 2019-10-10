testArticle = load('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/testArticle.mat');
trainArticle = load('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/Data/Train-Test/trainArticle.mat');

testArticle = testArticle.testArticle;
trainArticle = trainArticle.trainArticle;

binaryTestArticle = logical(testArticle > 0);
L1testArticle = testArticle/norm(testArticle,1);
L2testArticle = testArticle/norm(testArticle,2);

binaryTrainArticle = logical(trainArticle > 0);
L1trainArticle = trainArticle/norm(trainArticle,1);
L2trainArticle = trainArticle/norm(trainArticle,2);