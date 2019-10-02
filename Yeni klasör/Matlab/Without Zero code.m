
for n=0:6
    x=power(2,n)*50;
    temp=data(:,1:x);
    name=strcat(int2str(x),'.mat');
    disp(name)
    save(name,'temp');
end

for n=0:4
    x=power(2,n)*50;
    y=power(2,(n+1))*50;
    name=strcat(int2str(x),'.mat');
    name2=strcat(int2str(y),'.mat');
    load(name2);
    data=temp
    load(name)
    for a = 1:10
    for n = 2:x
        if temp(a, n) == 0
            for c = 2:y
                if data(a, c) ~= 0
                    disp(data(a, c))
                    ss = find(temp(a, :) == data(a, c));
                    if isempty(ss)
                        disp("cihad")
                        temp(a, n) = data(a, c);
                        break
                    end
                end
            end
        end
    end
end
    name=strcat(int2str(x),'withoutZero.mat');
        save(name,'temp');


end


    x=power(2,5)*50;
    
    name=strcat(int2str(x),'.mat');
    name2=strcat('word_index3200n.mat');
    load(name2);
    load(name)
    for a = 1:10
    for n = 2:x
        if temp(a, n) == 0
            for c = 2:913
                if data(a, c) ~= 0
                    disp(data(a, c))
                    ss = find(temp(a, :) == data(a, c));
                    if isempty(ss)
                        disp("cihad")
                        temp(a, n) = data(a, c);
                        break
                    end
                end
            end
        end
    end
end
    name=strcat(int2str(x),'withoutZero.mat');
        save(name,'temp');






