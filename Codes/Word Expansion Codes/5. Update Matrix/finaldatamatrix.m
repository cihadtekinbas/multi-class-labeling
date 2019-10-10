% Load datasets
tags = load('meta_bow_tags.mat');

articles=load('text_article_bow.mat');
articles=articles.features;

tags = tags.features;

categoryIndex = [220 284 257 264 325 387 258 252 1259 862];

selectedTags = logical(tags(categoryIndex,:) > 0);

[T,A] = find(selectedTags>0);
[Tsort, AIdx] = sort(T);

for k1 = 1:max(T)
    articlesForTags{k1} = A(AIdx(Tsort== k1));
end


%  for k = 1:10
%      art = transpose(articles);
%      catArticles = art(articlesForTags{k},:);
%      numberOfWordsInArticle = sum(catArticles,2);
%      minFiftyWordArticles = logical(numberOfWordsInArticle > 75);
%      minFiftyWordArticlesNumber = sum(minFiftyWordArticles);
%      listForMin{k} = minFiftyWordArticlesNumber;
%  end

for k = 1:10
    art = transpose(articles);
    catArticles = art(articlesForTags{k},:);
    numberOfWordsInArticle = sum(catArticles,2);
    [minSeventyFiveWordArticles{k}, NoNeed] = find(numberOfWordsInArticle > 75);
end

for k = 1:10
    categoryIndex = articlesForTags{k}(minSeventyFiveWordArticles{k});
    articleIndexForEachCategory{k}= categoryIndex;
end

for k = 1:10
    if k ~= 4
        selectionLimit = 222;
    else
        selectionLimit = 150;
    end
    categoryList = size(articleIndexForEachCategory{k});
    randomIndexes = randperm(categoryList(1),selectionLimit);
    edu_articles = articleIndexForEachCategory{k};
    tmp = edu_articles(randomIndexes,:)
    edu_articless = art(tmp,:);
    edu_tags = selectedTags(:,tmp);
    allArticles{k} = edu_articless;
    allTags{k} = edu_tags;
end

for k = 1:10
    if k == 4
        uniqueArticles{k} = allArticles{k};
        uniqueArticlesTags{k} = allTags{k};
    else
        numberOfWordsInArticle2 = sum(allArticles{k},2);
        [elements, elementsIndex, ~] = unique(numberOfWordsInArticle2,'stable');
        uniqueArticles{k} = allArticles{k}(elementsIndex,:);
        uniqueArticlesTags{k} = allTags{k}(:,elementsIndex);
    end
end

for k = 1:10
    finalData{k} = uniqueArticles{k}(1:150,:);
    finalDataTarget{k} = uniqueArticlesTags{k}(:,1:150);
end
finalDataMatrix=[];
finalDataMatrixTarget=[];
for k = 1:10
    finalDataMatrix = [finalDataMatrix; finalData{k}];
    finalDataMatrixTarget = [finalDataMatrixTarget finalDataTarget{k}];
end

save('finalDataMatrix.mat','finalDataMatrix')
save('finalDataMatrixTarget.mat','finalDataMatrixTarget')
