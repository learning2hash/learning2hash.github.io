---
layout: publication
title: Missing Data Imputation For Classification Problems
authors: Arkopal Choudhury, Michael R. Kosorok
conference: Arxiv
year: 2020
bibkey: choudhury2020missing
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10709'}]
tags: ["Datasets", "Evaluation"]
short_authors: Arkopal Choudhury, Michael R. Kosorok
---
Imputation of missing data is a common application in various classification
problems where the feature training matrix has missingness. A widely used
solution to this imputation problem is based on the lazy learning technique,
\(k\)-nearest neighbor (kNN) approach. However, most of the previous work on
missing data does not take into account the presence of the class label in the
classification problem. Also, existing kNN imputation methods use variants of
Minkowski distance as a measure of distance, which does not work well with
heterogeneous data. In this paper, we propose a novel iterative kNN imputation
technique based on class weighted grey distance between the missing datum and
all the training data. Grey distance works well in heterogeneous data with
missing instances. The distance is weighted by Mutual Information (MI) which is
a measure of feature relevance between the features and the class label. This
ensures that the imputation of the training data is directed towards improving
classification performance. This class weighted grey kNN imputation algorithm
demonstrates improved performance when compared to other kNN imputation
algorithms, as well as standard imputation algorithms such as MICE and
missForest, in imputation and classification problems. These problems are based
on simulated scenarios and UCI datasets with various rates of missingness.