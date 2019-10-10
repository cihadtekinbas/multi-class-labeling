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


for n=0:0
    tf_idf_score = zeros(8,200);
    x2=power(2,n)*50;
    %     temp=data(:,1:x);
    name=strcat(int2str(x2),'withoutZero.mat');
    disp(name)
    name2=strcat('idf_score',int2str(x2));
    name2=strcat(name2,'.mat');
    name3=strcat('tf_score',int2str(x2));
    name3=strcat(name3,'.mat');
    load(name2)
    idf_score = data;
    load(name3)
    tf_score=data;
    load(name);
    word_index=temp;
    
    for x = 1:10
        for y = 1:x2
            if tf_score(x,y) ~= 0 && idf_score(x,y) ~= 0
                tf_idf_score(x,y) = tf_score(x,y) * log(idf_score(x,y));
            end
        end
    end
    name=strcat(int2str(x2),'tf_idfscore.mat');
    save(name,'tf_idf_score');
    %     b=tf_idf_score;
    %     b(~b)=0.0001
    %     tf_idf_score=b; %to get rid of zeros
    for x = 1:10
        for y = 1:x2
            if word_index(x,y) ~= 0 && tf_idf_score(x,y) ~= 0
                start=(x-1)*150;
                if (x-1)==0
                    start=1;
                end
                
                update((start:((x)*150)),word_index(x,y))=tf_idf_score(x,y)*10000;
            end
        end
    end
    
    
    matrix_to_update = finalDataMatrix;

    newmmatrix=finalDataMatrix;
    for i=1:10
        for n=1:x2
            start=(i-1)*150;
            if (i-1)==0
                start=1
            end
            if word_index(i,n)~=0 && tf_idf_score(i,n) ~= 0
                newmmatrix((start:((i)*150)),word_index(i,n))= update((start:((i)*150)),word_index(i,n)).*matrix_to_update((start:((i)*150)),word_index(i,n));
                newmmatrix((start:((i)*150)),word_index(i,n))= update((start:((i)*150)),word_index(i,n))+newmmatrix((start:((i)*150)),word_index(i,n));
            end
        end
    end
    
    
    name=strcat(int2str(x2),'matrixUpdatev4.mat');
    finalDataMatrixYedek=finalDataMatrix;
    finalDataMatrix=newmmatrix;
    save(name,'finalDataMatrix');
    
    finalDataMatrix=finalDataMatrixYedek;
end





