---
layout: publication
title: 'Pn-net: Conjoined Triple Deep Network For Learning Local Image Descriptors'
authors: Vassileios Balntas, Edward Johns, Lilian Tang, Krystian Mikolajczyk
conference: Arxiv
year: 2016
bibkey: balntas2016pn
citations: 165
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.05030'}]
tags: [Evaluation, Memory Efficiency]
short_authors: Balntas et al.
---
In this paper we propose a new approach for learning local descriptors for
matching image patches. It has recently been demonstrated that descriptors
based on convolutional neural networks (CNN) can significantly improve the
matching performance. Unfortunately their computational complexity is
prohibitive for any practical application. We address this problem and propose
a CNN based descriptor with improved matching performance, significantly
reduced training and execution time, as well as low dimensionality.
  We propose to train the network with triplets of patches that include a
positive and negative pairs. To that end we introduce a new loss function that
exploits the relations within the triplets. We compare our approach to recently
introduced MatchNet and DeepCompare and demonstrate the advantages of our
descriptor in terms of performance, memory footprint and speed i.e. when run in
GPU, the extraction time of our 128 dimensional feature is comparable to the
fastest available binary descriptors such as BRIEF and ORB.