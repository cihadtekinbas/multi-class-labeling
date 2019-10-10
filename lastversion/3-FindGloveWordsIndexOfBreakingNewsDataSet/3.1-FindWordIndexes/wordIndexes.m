taglist = fopen('taglist.csv', 'r');
taglist = fgetl(taglist);
taglist = split(taglist, ',');
[num, ~] = size(taglist);
fid = fopen('datapnew3200', 'r');
dict = containers.Map

% keys(dict)
% values(dict)
% dict('school')
fid1 = fopen('vocabulary_article_sorted.txt', 'r');
count = 1;
while ~ feof(fid1)
    line1 = fgetl(fid1);
    splited = split(line1, ' ');
    dict(char(splited(1)))=count;
    count = count + 1;
    if isempty(line1)
        break
    end
end
fclose(fid1);



z = zeros(num, 50);
while ~ feof(fid)
    line = fgetl(fid);
    line = split(line, '$#$');
    name = line(1);
    found = - 1;
    for n = 1:num
        if strcmp(name, taglist(n)) == 1
            found = n;
            break
        end
    end
    disp(length(line))
    for n = 2:length(line)
        if isKey(dict,char(line(n))) == 1
            z(found, n) = dict(char(line(n)));
            
        end
        
    end
    
    if isempty(line)
        break
    end
end
fclose(fid);
wordindexes = z;
data = wordindexes;
name = strcat("word_index3200", '.mat');
save(name, 'data');


