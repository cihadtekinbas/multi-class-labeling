testArticle = load('testArticle.mat');
trainArticle = load('trainArticle.mat');

testArticle = testArticle.testArticle;
trainArticle = trainArticle.trainArticle;

binaryTestArticle = logical(testArticle > 0);
L1testArticle = testArticle/norm(testArticle,1);
L2testArticle = testArticle/norm(testArticle,2);

binaryTrainArticle = logical(trainArticle > 0);
L1trainArticle = trainArticle/norm(trainArticle,1);
L2trainArticle = trainArticle/norm(trainArticle,2);
save('L1testArticle.mat','L1testArticle')
save('L1trainArticle.mat','L1trainArticle')
save('L2testArticle.mat','L2testArticle')
save('L2trainArticle.mat','L2trainArticle')
save('binaryTestArticle.mat','binaryTestArticle')
save('binaryTrainArticle.mat','binaryTrainArticle')