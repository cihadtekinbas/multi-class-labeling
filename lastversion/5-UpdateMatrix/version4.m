

for n=0:6
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





