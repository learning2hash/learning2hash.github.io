---
layout: publication
title: Ensemble Feature For Person Re-identification
authors: Jiabao Wang, Yang Li, Zhuang Miao
conference: Arxiv
year: 2019
bibkey: wang2019ensemble
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.05798'}]
tags: [Evaluation, Neural Hashing]
short_authors: Jiabao Wang, Yang Li, Zhuang Miao
---
In person re-identification (re-ID), the key task is feature representation,
which is used to compute distance or similarity in prediction. Person re-ID
achieves great improvement when deep learning methods are introduced to tackle
this problem. The features extracted by convolutional neural networks (CNN) are
more effective and discriminative than the hand-crafted features. However, deep
feature extracted by a single CNN network is not robust enough in testing
stage. To improve the ability of feature representation, we propose a new
ensemble network (EnsembleNet) by dividing a single network into multiple
end-to-end branches. The ensemble feature is obtained by concatenating each of
the branch features to represent a person. EnsembleNet is designed based on
ResNet-50 and its backbone shares most of the parameters for saving computation
and memory cost. Experimental results show that our EnsembleNet achieves the
state-of-the-art performance on the public Market1501, DukeMTMC-reID and CUHK03
person re-ID benchmarks.