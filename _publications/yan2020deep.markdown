---
layout: publication
title: Deep Multi-view Enhancement Hashing For Image Retrieval
authors: Chenggang Yan, Biao Gong, Yuxuan Wei, Yue Gao
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2020
bibkey: yan2020deep
citations: 414
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00169'}]
tags: ["Compact Codes", "Evaluation", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Scalability", "Supervised"]
short_authors: Yan et al.
---
Hashing is an efficient method for nearest neighbor search in large-scale
data space by embedding high-dimensional feature descriptors into a similarity
preserving Hamming space with a low dimension. However, large-scale high-speed
retrieval through binary code has a certain degree of reduction in retrieval
accuracy compared to traditional retrieval methods. We have noticed that
multi-view methods can well preserve the diverse characteristics of data.
Therefore, we try to introduce the multi-view deep neural network into the hash
learning field, and design an efficient and innovative retrieval model, which
has achieved a significant improvement in retrieval performance. In this paper,
we propose a supervised multi-view hash model which can enhance the multi-view
information through neural networks. This is a completely new hash learning
method that combines multi-view and deep learning methods. The proposed method
utilizes an effective view stability evaluation method to actively explore the
relationship among views, which will affect the optimization direction of the
entire network. We have also designed a variety of multi-data fusion methods in
the Hamming space to preserve the advantages of both convolution and
multi-view. In order to avoid excessive computing resources on the enhancement
procedure during retrieval, we set up a separate structure called memory
network which participates in training together. The proposed method is
systematically evaluated on the CIFAR-10, NUS-WIDE and MS-COCO datasets, and
the results show that our method significantly outperforms the state-of-the-art
single-view and multi-view hashing methods.