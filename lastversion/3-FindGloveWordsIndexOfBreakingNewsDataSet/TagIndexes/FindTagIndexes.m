taglist = fopen('/home/asus/Desktop/Classification/lastversion/3-FindGloveWordsIndexOfBreakingNewsDataSet/3.1-FindWordIndexes/taglist.csv', 'r');
taglist = fgetl(taglist);
taglist = split(taglist, ',');
[num, ~] = size(taglist);
disp("level1")
fid = fopen('/home/asus/Desktop/Classification/lastversion/3-FindGloveWordsIndexOfBreakingNewsDataSet/TagIndexes/vocabulary_tags_sorted.txt', 'r');
count = 1;
x = zeros(1, num);
while ~ feof(fid)
    line = fgetl(fid);
    %     sp=split(line,' ')
    k = strfind(line, ' ');
    line = line(1:k(length(k)) - 1);
    for n = 1:num
        %     disp(taglist(n));
        tfe = strcmp(line, taglist(n));
        if tfe == 1
            x(n) = count;
        end
    end
    if isempty(line)
        break
    end
    count = count + 1;
end
fclose(fid);
for n = 1:num
    disp(taglist(n));
end

tagindexes = x;
save('tagindexes',"tagindexes")