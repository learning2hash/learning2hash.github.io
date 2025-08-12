---
layout: publication
title: A Discriminative Learned CNN Embedding For Remote Sensing Image Scene Classification
authors: Wen Wang, Lijun Du, Yinxing Gao, Yanzhou Su, Feng Wang, Jian Cheng
conference: IGARSS 2019 - 2019 IEEE International Geoscience and Remote Sensing Symposium
year: 2019
bibkey: wang2019discriminative
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.12517'}]
tags: ["Distance Metric Learning"]
short_authors: Wang et al.
---
In this work, a discriminatively learned CNN embedding is proposed for remote
sensing image scene classification. Our proposed siamese network simultaneously
computes the classification loss function and the metric learning loss function
of the two input images. Specifically, for the classification loss, we use the
standard cross-entropy loss function to predict the classes of the images. For
the metric learning loss, our siamese network learns to map the intra-class and
inter-class input pairs to a feature space where intra-class inputs are close
and inter-class inputs are separated by a margin. Concretely, for remote
sensing image scene classification, we would like to map images from the same
scene to feature vectors that are close, and map images from different scenes
to feature vectors that are widely separated. Experiments are conducted on
three different remote sensing image datasets to evaluate the effectiveness of
our proposed approach. The results demonstrate that the proposed method
achieves an excellent classification performance.