---
layout: publication
title: 'Deepemd: Differentiable Earth Mover''s Distance For Few-shot Learning'
authors: Chi Zhang, Yujun Cai, Guosheng Lin, Chunhua Shen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: zhang2020deepemd
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.06777'}]
tags: [Few-shot & Zero-shot, Image Retrieval]
short_authors: Zhang et al.
---
In this work, we develop methods for few-shot image classification from a new
perspective of optimal matching between image regions. We employ the Earth
Mover's Distance (EMD) as a metric to compute a structural distance between
dense image representations to determine image relevance. The EMD generates the
optimal matching flows between structural elements that have the minimum
matching cost, which is used to calculate the image distance for
classification. To generate the important weights of elements in the EMD
formulation, we design a cross-reference mechanism, which can effectively
alleviate the adverse impact caused by the cluttered background and large
intra-class appearance variations. To implement k-shot classification, we
propose to learn a structured fully connected layer that can directly classify
dense image representations with the EMD. Based on the implicit function
theorem, the EMD can be inserted as a layer into the network for end-to-end
training. Our extensive experiments validate the effectiveness of our algorithm
which outperforms state-of-the-art methods by a significant margin on five
widely used few-shot classification benchmarks, namely, miniImageNet,
tieredImageNet, Fewshot-CIFAR100 (FC100), Caltech-UCSD Birds-200-2011 (CUB),
and CIFAR-FewShot (CIFAR-FS). We also demonstrate the effectiveness of our
method on the image retrieval task in our experiments.