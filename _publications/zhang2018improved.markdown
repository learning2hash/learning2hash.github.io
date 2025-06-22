---
layout: publication
title: Improved Deep Hashing With Soft Pairwise Similarity For Multi-label Image Retrieval
authors: Zheng Zhang, Qin Zou, Yuewei Lin, Long Chen, Song Wang
conference: Arxiv
year: 2018
citations: 139
bibkey: zhang2018improved
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.02987'}]
tags: [Applications, Deep Hashing, ANN Search, Hashing Methods]
---
Hash coding has been widely used in the approximate nearest neighbor search
for large-scale image retrieval. Recently, many deep hashing methods have been
proposed and shown largely improved performance over traditional
feature-learning-based methods. Most of these methods examine the pairwise
similarity on the semantic-level labels, where the pairwise similarity is
generally defined in a hard-assignment way. That is, the pairwise similarity is
'1' if they share no less than one class label and '0' if they do not share
any. However, such similarity definition cannot reflect the similarity ranking
for pairwise images that hold multiple labels. In this paper, a new deep
hashing method is proposed for multi-label image retrieval by re-defining the
pairwise similarity into an instance similarity, where the instance similarity
is quantified into a percentage based on the normalized semantic labels. Based
on the instance similarity, a weighted cross-entropy loss and a minimum mean
square error loss are tailored for loss-function construction, and are
efficiently used for simultaneous feature learning and hash coding. Experiments
on three popular datasets demonstrate that, the proposed method outperforms the
competing methods and achieves the state-of-the-art performance in multi-label
image retrieval.