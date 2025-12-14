---
layout: publication
title: Deep Forest With Hashing Screening And Window Screening
authors: Pengfei Ma, Youxi Wu, Yan Li, Lei Guo, He Jiang, Xingquan Zhu, Xindong Wu
conference: Arxiv
year: 2022
bibkey: ma2022deep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.11951'}]
tags: [Hashing Methods, Evaluation, Datasets, Neural Hashing]
short_authors: Ma et al.
---
As a novel deep learning model, gcForest has been widely used in various
applications. However, the current multi-grained scanning of gcForest produces
many redundant feature vectors, and this increases the time cost of the model.
To screen out redundant feature vectors, we introduce a hashing screening
mechanism for multi-grained scanning and propose a model called HW-Forest which
adopts two strategies, hashing screening and window screening. HW-Forest
employs perceptual hashing algorithm to calculate the similarity between
feature vectors in hashing screening strategy, which is used to remove the
redundant feature vectors produced by multi-grained scanning and can
significantly decrease the time cost and memory consumption. Furthermore, we
adopt a self-adaptive instance screening strategy to improve the performance of
our approach, called window screening, which can achieve higher accuracy
without hyperparameter tuning on different datasets. Our experimental results
show that HW-Forest has higher accuracy than other models, and the time cost is
also reduced.