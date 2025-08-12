---
layout: publication
title: Kernel Relative-prototype Spectral Filtering For Few-shot Learning
authors: Tao Zhang, Wu Huang
conference: Lecture Notes in Computer Science
year: 2022
bibkey: zhang2022kernel
citations: 7
additional_links: [{name: Code, url: 'https://github.com/zhangtao2022/DSFN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.11685'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tao Zhang, Wu Huang
---
Few-shot learning performs classification tasks and regression tasks on
scarce samples. As one of the most representative few-shot learning models,
Prototypical Network represents each class as sample average, or a prototype,
and measures the similarity of samples and prototypes by Euclidean distance. In
this paper, we propose a framework of spectral filtering (shrinkage) for
measuring the difference between query samples and prototypes, or namely the
relative prototypes, in a reproducing kernel Hilbert space (RKHS). In this
framework, we further propose a method utilizing Tikhonov regularization as the
filter function for few-shot classification. We conduct several experiments to
verify our method utilizing different kernels based on the miniImageNet
dataset, tiered-ImageNet dataset and CIFAR-FS dataset. The experimental results
show that the proposed model can perform the state-of-the-art. In addition, the
experimental results show that the proposed shrinkage method can boost the
performance. Source code is available at https://github.com/zhangtao2022/DSFN.