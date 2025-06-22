---
layout: publication
title: Distillhash Unsupervised Deep Hashing By Distilling Data Pairs
authors: Yang Erkun, Liu Tongliang, Deng Cheng, Liu Wei, Tao Dacheng
conference: Arxiv
year: 2019
citations: 121
bibkey: yang2019distillhash
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.03465'}]
tags: [ARXIV, Unsupervised, Supervised]
---
Due to the high storage and search efficiency, hashing has become prevalent
for large-scale similarity search. Particularly, deep hashing methods have
greatly improved the search performance under supervised scenarios. In
contrast, unsupervised deep hashing models can hardly achieve satisfactory
performance due to the lack of reliable supervisory similarity signals. To
address this issue, we propose a novel deep unsupervised hashing model, dubbed
DistillHash, which can learn a distilled data set consisted of data pairs,
which have confidence similarity signals. Specifically, we investigate the
relationship between the initial noisy similarity signals learned from local
structures and the semantic similarity labels assigned by a Bayes optimal
classifier. We show that under a mild assumption, some data pairs, of which
labels are consistent with those assigned by the Bayes optimal classifier, can
be potentially distilled. Inspired by this fact, we design a simple yet
effective strategy to distill data pairs automatically and further adopt a
Bayesian learning framework to learn hash functions from the distilled data
set. Extensive experimental results on three widely used benchmark datasets
show that the proposed DistillHash consistently accomplishes the
state-of-the-art search performance.