How weighted results are obtained?

1. F-Measure

First, weighted precision is calculated by dividing all true positives to sum of all true positives and true negatives.

P = TP / (TP+FP)

Second, weighted recall is calculated by dividing all true positives to sum of all true positives and false negatives.

R = TP / (TP+FN)

Then, F-Measure is calculated.

F = (2*R*P)/(R+P)


2. Jaccard Score

There is a method in sklearn library that calculates jaccard score. It takes two input: predicted results and ground truths.

Every binary classifier has jaccard score but in order to calculate a weighted jaccard score following procedure has been done.

1. Concatenate all predicted results for all classifiers in a single array.
2. Concatenate all ground truths for all classifiers in a single array.
3. Calculate jaccard score using those array as inputs.