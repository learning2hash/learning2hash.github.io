---
layout: publication
title: Deep Ordinal Hashing With Spatial Attention
authors: Jin et al.
conference: IEEE Transactions on Image Processing
year: 2018
bibkey: jin2018deep
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.02459'}]
tags: [Hashing Methods]
---
Hashing has attracted increasing research attentions in recent years due to
its high efficiency of computation and storage in image retrieval. Recent works
have demonstrated the superiority of simultaneous feature representations and
hash functions learning with deep neural networks. However, most existing deep
hashing methods directly learn the hash functions by encoding the global
semantic information, while ignoring the local spatial information of images.
The loss of local spatial structure makes the performance bottleneck of hash
functions, therefore limiting its application for accurate similarity
retrieval. In this work, we propose a novel Deep Ordinal Hashing (DOH) method,
which learns ordinal representations by leveraging the ranking structure of
feature space from both local and global views. In particular, to effectively
build the ranking structure, we propose to learn the rank correlation space by
exploiting the local spatial information from Fully Convolutional Network (FCN)
and the global semantic information from the Convolutional Neural Network (CNN)
simultaneously. More specifically, an effective spatial attention model is
designed to capture the local spatial information by selectively learning
well-specified locations closely related to target objects. In such hashing
framework,the local spatial and global semantic nature of images are captured
in an end-to-end ranking-to-hashing manner. Experimental results conducted on
three widely-used datasets demonstrate that the proposed DOH method
significantly outperforms the state-of-the-art hashing methods.