---
layout: publication
title: Rescuing Deep Hashing From Dead Bits Problem
authors: Shu Zhao, Dayan Wu, Yucan Zhou, Bo Li, Weiping Wang
conference: Proceedings of the Thirtieth International Joint Conference on Artificial
  Intelligence
year: 2021
bibkey: zhao2021rescuing
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.00648'}]
tags: [Image Retrieval, Neural Hashing, Hashing Methods, AAAI, Scalability, Efficiency,
  IJCAI, Datasets, Quantization]
short_authors: Zhao et al.
---
Deep hashing methods have shown great retrieval accuracy and efficiency in
large-scale image retrieval. How to optimize discrete hash bits is always the
focus in deep hashing methods. A common strategy in these methods is to adopt
an activation function, e.g. \(\operatorname\{sigmoid\}(\cdot)\) or
\(\operatorname\{tanh\}(\cdot)\), and minimize a quantization loss to approximate
discrete values. However, this paradigm may make more and more hash bits stuck
into the wrong saturated area of the activation functions and never escaped. We
call this problem "Dead Bits Problem~(DBP)". Besides, the existing quantization
loss will aggravate DBP as well. In this paper, we propose a simple but
effective gradient amplifier which acts before activation functions to
alleviate DBP. Moreover, we devise an error-aware quantization loss to further
alleviate DBP. It avoids the negative effect of quantization loss based on the
similarity between two images. The proposed gradient amplifier and error-aware
quantization loss are compatible with a variety of deep hashing methods.
Experimental results on three datasets demonstrate the efficiency of the
proposed gradient amplifier and the error-aware quantization loss.