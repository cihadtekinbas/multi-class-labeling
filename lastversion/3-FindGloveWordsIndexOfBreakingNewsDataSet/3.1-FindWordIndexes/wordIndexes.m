taglist = fopen('/home/asus/Desktop/Classification/lastversion/3-FindGloveWordsIndexOfBreakingNewsDataSet/3.1-FindWordIndexes/taglist.csv', 'r');
taglist = fgetl(taglist);
taglist = split(taglist, ',');
[num, ~] = size(taglist);
fid = fopen('/home/asus/Desktop/Classification/lastversion/3-FindGloveWordsIndexOfBreakingNewsDataSet/3.1-FindWordIndexes/datapnew100', 'r');
z = zeros(num, 50);
while ~ feof(fid)
    line = fgetl(fid);
    line = split(line, ',');
    name = line(1);
    found = - 1;
    for n = 1:num
        if strcmp(name, taglist(n)) == 1
            found = n;
            break
        end
    end
    for n = 2:length(line)
        fid1 = fopen('/home/asus/Desktop/Classification/lastversion/3-FindGloveWordsIndexOfBreakingNewsDataSet/3.1-FindWordIndexes/vocabulary_article_sorted.txt', 'r');
        count = 1;
        while ~ feof(fid1)
            line1 = fgetl(fid1);
            splited = split(line1, ' ');
            if strcmp(line(n), splited(1)) == 1
                z(found, n) = count;
                break
            end
            count = count + 1;
            if isempty(line1)
                break
            end
        end
        fclose(fid1);
    end
    if isempty(line)
        break
    end
    count = count + 1;
end
fclose(fid);
wordindexes = z;
data = wordindexes;
name = strcat("word_index100", '.mat');
save(name, 'data');


