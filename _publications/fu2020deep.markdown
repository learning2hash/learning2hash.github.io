---
layout: publication
title: Deep Momentum Uncertainty Hashing
authors: Fu et al.
conference: Pattern Recognition
year: 2020
bibkey: fu2020deep
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.08012'}]
tags: [DATASETS, Hashing Methods, CVPR, Compact Codes, Neural Hashing, Evaluation]
---
Combinatorial optimization (CO) has been a hot research topic because of its
theoretic and practical importance. As a classic CO problem, deep hashing aims
to find an optimal code for each data from finite discrete possibilities, while
the discrete nature brings a big challenge to the optimization process.
Previous methods usually mitigate this challenge by binary approximation,
substituting binary codes for real-values via activation functions or
regularizations. However, such approximation leads to uncertainty between
real-values and binary ones, degrading retrieval performance. In this paper, we
propose a novel Deep Momentum Uncertainty Hashing (DMUH). It explicitly
estimates the uncertainty during training and leverages the uncertainty
information to guide the approximation process. Specifically, we model
bit-level uncertainty via measuring the discrepancy between the output of a
hashing network and that of a momentum-updated network. The discrepancy of each
bit indicates the uncertainty of the hashing network to the approximate output
of that bit. Meanwhile, the mean discrepancy of all bits in a hashing code can
be regarded as image-level uncertainty. It embodies the uncertainty of the
hashing network to the corresponding input image. The hashing bit and image
with higher uncertainty are paid more attention during optimization. To the
best of our knowledge, this is the first work to study the uncertainty in
hashing bits. Extensive experiments are conducted on four datasets to verify
the superiority of our method, including CIFAR-10, NUS-WIDE, MS-COCO, and a
million-scale dataset Clothing1M. Our method achieves the best performance on
all of the datasets and surpasses existing state-of-the-art methods by a large
margin.