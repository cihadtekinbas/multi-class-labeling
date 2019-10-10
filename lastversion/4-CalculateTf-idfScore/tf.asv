words=load('text_article_bow.mat');
words=words.features;

tags=load('meta_bow_tags.mat');
tags=tags.features;


load('tagindexes.mat');
num=length(tagindexes)
taglist = fopen('taglist.csv', 'r');
taglist = fgetl(taglist);
taglist = split(taglist, ',');

% AIDs_for_tags=findAIDs(tags); tags=tags(tagindexes,:);

s=zeros(num,2000);
for n = 1:num
    x=find(tags(tagindexes(n),:));
    for i=1:length(x)
        s(n,i)=x(i);
    end
end
AIDs_for_tags=s;
save('AIDs_for_tags.mat','AIDs_for_tags')
% film_genre_set=zeros(115427,115499);
clear film_genre_set;

for i=1:num
    for n=1:length(s(i,:))
        if s(i,n)>0
            film_genre_set(:,s(i,n))=words(:,s(i,n));
         
        end
    end
    data=film_genre_set;
    name=strcat(char(taglist(i)),'.mat');
    save(name,'data');
    clear data
    clear film_genre_set;
    
end


load('800withoutZero.mat');
wordindexes=temp
tf_score=zeros(10,50);
idf_score=zeros(10,50);
disp("level3")

for j=1:num
    name=strcat(char(taglist(j)),'.mat');
    load (name);
    clear film_genre_set;
    film_genre_set=data;
    sum1=sum(film_genre_set);
    g_sum=sum(sum(film_genre_set));
    [row,col] = size(film_genre_set);

    num_col=0;
    for n=1:col
        if sum(film_genre_set(:,n))>0
        num_col=num_col+1;
        end    
    end
    
    for n1=1:length(wordindexes(j,:))
    ss=wordindexes(j,n1);
    if ss>0
        tf_score(j,n1)=sum(film_genre_set(ss,:))/g_sum;
        count=0;
        for nn=1:col
            if film_genre_set(ss,nn) >0
                count=count+1;
            end
        end
        idf_score(j,n1)=num_col/count;
%         disp(count)
    end
    end

end



data=tf_score;
name='tf_score800.mat';
save(name,'data');
data=idf_score;
name='idf_score800.mat';
save(name,'data');
 






