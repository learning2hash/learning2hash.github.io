---
layout: publication
title: 'Rankdnn: Learning To Rank For Few-shot Learning'
authors: Qianyu Guo, Hongtong Gong, Xujun Wei, Yanwei Fu, Weifeng Ge, Yizhou Yu, Wenqiang
  Zhang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: guo2022rankdnn
citations: 19
additional_links: [{name: Code, url: 'https://github.com/guoqianyu-alberta/RankDNN'},
  {name: Paper, url: 'https://arxiv.org/abs/2211.15320'}]
tags: ["AAAI", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Re-Ranking"]
short_authors: Guo et al.
---
This paper introduces a new few-shot learning pipeline that casts relevance
ranking for image retrieval as binary ranking relation classification. In
comparison to image classification, ranking relation classification is sample
efficient and domain agnostic. Besides, it provides a new perspective on
few-shot learning and is complementary to state-of-the-art methods. The core
component of our deep neural network is a simple MLP, which takes as input an
image triplet encoded as the difference between two vector-Kronecker products,
and outputs a binary relevance ranking order. The proposed RankMLP can be built
on top of any state-of-the-art feature extractors, and our entire deep neural
network is called the ranking deep neural network, or RankDNN. Meanwhile,
RankDNN can be flexibly fused with other post-processing methods. During the
meta test, RankDNN ranks support images according to their similarity with the
query samples, and each query sample is assigned the class label of its nearest
neighbor. Experiments demonstrate that RankDNN can effectively improve the
performance of its baselines based on a variety of backbones and it outperforms
previous state-of-the-art algorithms on multiple few-shot learning benchmarks,
including miniImageNet, tieredImageNet, Caltech-UCSD Birds, and CIFAR-FS.
Furthermore, experiments on the cross-domain challenge demonstrate the superior
transferability of RankDNN.The code is available at:
https://github.com/guoqianyu-alberta/RankDNN.