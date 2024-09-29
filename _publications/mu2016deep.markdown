---
layout: publication
title: Deep Hashing A Joint Approach For Image Signature Learning
authors: Mu Yadong, Liu Zhu
conference: "Arxiv"
year: 2016
bibkey: mu2016deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1608.03658"}
tags: ['ARXIV', 'Deep Learning', 'Supervised']
---
Similarity45;based image hashing represents crucial technique for visual data storage reduction and expedited image search. Conventional hashing schemes typically feed hand45;crafted features into hash functions which separates the procedures of feature extraction and hash function learning. In this paper we propose a novel algorithm that concurrently performs feature engineering and non45;linear supervised hashing function learning. Our technical contributions in this paper are two45;folds 1) deep network optimization is often achieved by gradient propagation which critically requires a smooth objective function. The discrete nature of hash codes makes them not amenable for gradient45;based optimization. To address this issue we propose an exponentiated hashing loss function and its bilinear smooth approximation. Effective gradient calculation and propagation are thereby enabled; 2) pre45;training is an important trick in supervised deep learning. The impact of pre45;training on the hash code quality has never been discussed in current deep hashing literature. We propose a pre45;training scheme inspired by recent advance in deep network based image classification and experimentally demonstrate its effectiveness. Comprehensive quantitative evaluations are conducted on several widely45;used image benchmarks. On all benchmarks our proposed deep hashing algorithm outperforms all state45;of45;the45;art competitors by significant margins. In particular our algorithm achieves a near45;perfect 0.99 in terms of Hamming ranking accuracy with only 12 bits on MNIST and a new record of 0.74 on the CIFAR10 dataset. In comparison the best accuracies obtained on CIFAR10 by existing hashing algorithms without or with deep networks are known to be 0.36 and 0.58 respectively.
