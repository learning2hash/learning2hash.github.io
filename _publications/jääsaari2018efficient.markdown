---
layout: publication
title: Efficient Autotuning Of Hyperparameters In Approximate Nearest Neighbor Search
authors: "Elias J\xE4\xE4saari, Ville Hyv\xF6nen, Teemu Roos"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: "j\xE4\xE4saari2018efficient"
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.07484'}]
tags: ["Efficiency", "Locality Sensitive Hashing", "Tree Based ANN"]
short_authors: "Elias J\xE4\xE4saari, Ville Hyv\xF6nen, Teemu Roos"
---
Approximate nearest neighbor algorithms are used to speed up nearest neighbor
search in a wide array of applications. However, current indexing methods
feature several hyperparameters that need to be tuned to reach an acceptable
accuracy--speed trade-off. A grid search in the parameter space is often
impractically slow due to a time-consuming index-building procedure. Therefore,
we propose an algorithm for automatically tuning the hyperparameters of
indexing methods based on randomized space-partitioning trees. In particular,
we present results using randomized k-d trees, random projection trees and
randomized PCA trees. The tuning algorithm adds minimal overhead to the
index-building process but is able to find the optimal hyperparameters
accurately. We demonstrate that the algorithm is significantly faster than
existing approaches, and that the indexing methods used are competitive with
the state-of-the-art methods in query time while being faster to build.