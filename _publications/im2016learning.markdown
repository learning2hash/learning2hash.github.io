---
layout: publication
title: Learning A Metric For Class-conditional KNN
authors: Im Daniel Jiwoong, Taylor Graham W.
conference: 2016 International Joint Conference on Neural Networks (IJCNN)
year: 2016
bibkey: im2016learning
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.03050'}]
tags: [DATASETS, Tools & Libraries, Evaluation, Distance Metric Learning]
---
Naive Bayes Nearest Neighbour (NBNN) is a simple and effective framework
which addresses many of the pitfalls of K-Nearest Neighbour (KNN)
classification. It has yielded competitive results on several computer vision
benchmarks. Its central tenet is that during NN search, a query is not compared
to every example in a database, ignoring class information. Instead, NN
searches are performed within each class, generating a score per class. A key
problem with NN techniques, including NBNN, is that they fail when the data
representation does not capture perceptual (e.g.~class-based) similarity. NBNN
circumvents this by using independent engineered descriptors (e.g.~SIFT). To
extend its applicability outside of image-based domains, we propose to learn a
metric which captures perceptual similarity. Similar to how Neighbourhood
Components Analysis optimizes a differentiable form of KNN classification, we
propose "Class Conditional" metric learning (CCML), which optimizes a soft form
of the NBNN selection rule. Typical metric learning algorithms learn either a
global or local metric. However, our proposed method can be adjusted to a
particular level of locality by tuning a single parameter. An empirical
evaluation on classification and retrieval tasks demonstrates that our proposed
method clearly outperforms existing learned distance metrics across a variety
of image and non-image datasets.