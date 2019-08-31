% Load datasets
tags = load('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/meta_bow_tags.mat');
articles = load('/home/saidaltindis/ALL FILES/PROJECTS/MULTI-LABEL CLASSIFICATION/text_article_bow.mat');

%tags = transpose(tags.features);
articles = transpose(articles.features);

% Analyze on articles
% There are total of 115499 article and 115427 unique word
numberOfWordsInArticle = sum(articles,2);
notEmptyArticles = logical(numberOfWordsInArticle > 0 );
notEmptyArticlesNumber = sum(notEmptyArticles);

totalArticleWordNumber = sum(numberOfWordsInArticle);
meanOfArticleWord = totalArticleWordNumber/notEmptyArticlesNumber;

wordUsage = transpose(sum(articles));
[M,I] = max(wordUsage);


% RESULTS
% 1. There are no empty matrix.
% 2. Mean of article words is = 216.2
% 3. Most used word is "year" with 191911 time.

% ----------------------------------------------------- %

% Analyze on tags
% There are total of 115499 article and 31237 tags.
%usageOfTags = sum(tags);
%nonZeroUsageTag = logical(usageOfTags > 0);
%numberOfNonZeroUsageTag = sum(nonZeroUsageTag);

%totalUsageOfTags = sum(usageOfTags);
%meanOfTotalUsageOfTags = totalUsageOfTags/numberOfNonZeroUsageTag;

%[M,I] = max(usageOfTags);

% RESULTS
% 1. From 31237 tags only 16531 of them is used.
% 2. Mean of tag usage is 9.36
% 3. Maximum used tag is "business" with 4070 usage.

