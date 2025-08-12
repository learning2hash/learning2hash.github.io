---
layout: publication
title: An Improved K-nearest Neighbor Algorithm For Text Categorization
authors: Baoli Li, Shiwen Yu, Qin Lu
conference: Expert Systems with Applications
year: 2011
bibkey: li2003improved
citations: 300
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/cs/0306099'}]
tags: ["Evaluation"]
short_authors: Baoli Li, Shiwen Yu, Qin Lu
---
k is the most important parameter in a text categorization system based on
k-Nearest Neighbor algorithm (kNN).In the classification process, k nearest
documents to the test one in the training set are determined firstly. Then, the
predication can be made according to the category distribution among these k
nearest neighbors. Generally speaking, the class distribution in the training
set is uneven. Some classes may have more samples than others. Therefore, the
system performance is very sensitive to the choice of the parameter k. And it
is very likely that a fixed k value will result in a bias on large categories.
To deal with these problems, we propose an improved kNN algorithm, which uses
different numbers of nearest neighbors for different categories, rather than a
fixed number across all categories. More samples (nearest neighbors) will be
used for deciding whether a test document should be classified to a category,
which has more samples in the training set. Preliminary experiments on Chinese
text categorization show that our method is less sensitive to the parameter k
than the traditional one, and it can properly classify documents belonging to
smaller classes with a large k. The method is promising for some cases, where
estimating the parameter k via cross-validation is not allowed.