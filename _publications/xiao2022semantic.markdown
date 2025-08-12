---
layout: publication
title: Semantic Cross Attention For Few-shot Learning
authors: Bin Xiao, Chien-Liang Liu, Wen-Hoar Hsaio
conference: Arxiv
year: 2022
bibkey: xiao2022semantic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.06311'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bin Xiao, Chien-Liang Liu, Wen-Hoar Hsaio
---
Few-shot learning (FSL) has attracted considerable attention recently. Among
existing approaches, the metric-based method aims to train an embedding network
that can make similar samples close while dissimilar samples as far as possible
and achieves promising results. FSL is characterized by using only a few images
to train a model that can generalize to novel classes in image classification
problems, but this setting makes it difficult to learn the visual features that
can identify the images' appearance variations. The model training is likely to
move in the wrong direction, as the images in an identical semantic class may
have dissimilar appearances, whereas the images in different semantic classes
may share a similar appearance. We argue that FSL can benefit from additional
semantic features to learn discriminative feature representations. Thus, this
study proposes a multi-task learning approach to view semantic features of
label text as an auxiliary task to help boost the performance of the FSL task.
Our proposed model uses word-embedding representations as semantic features to
help train the embedding network and a semantic cross-attention module to
bridge the semantic features into the typical visual modal. The proposed
approach is simple, but produces excellent results. We apply our proposed
approach to two previous metric-based FSL methods, all of which can
substantially improve performance. The source code for our model is accessible
from github.