load('finalDataMatrix.mat')
for n=0:6
    tf_idf_score = zeros(10,200);
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

    matrix_to_update = finalDataMatrix;
    for x = 1:10
        for y = 1:x2
            if word_index(x,y) ~= 0 && tf_idf_score(x,y) ~= 0
                start=(x-1)*150;
                if (x-1)==0
                    start=1
                end
                %             matrix_to_update(word_index(x,y),nonzeros(AIDs(x,:))) = features(x,y)+features(x,y)*tf_idf_score(x,y)*10000;
                %             matrix_to_update((start:((x)*150)),word_index(x,y)) = mean(finalDataMatrix(:,word_index(x,y)))+ mean(finalDataMatrix(:,word_index(x,y)))*tf_idf_score(x,y)*10000;
                matrix_to_update((start:((x)*150)),word_index(x,y)) = tf_idf_score(x,y)*10000;

            end
        end
    end
    
    name=strcat(int2str(x2),'matrixUpdateV1.mat');
    finalDataMatrixYedek=finalDataMatrix;
    finalDataMatrix=matrix_to_update;
    save(name,'finalDataMatrix');
    finalDataMatrix=finalDataMatrixYedek;
    
    
end



