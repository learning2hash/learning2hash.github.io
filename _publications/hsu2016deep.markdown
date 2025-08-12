---
layout: publication
title: Deep Image Category Discovery Using A Transferred Similarity Function
authors: Yen-Chang Hsu, Zhaoyang Lv, Zsolt Kira
conference: Arxiv
year: 2016
bibkey: hsu2016deep
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.01253'}]
tags: ["Distance Metric Learning"]
short_authors: Yen-Chang Hsu, Zhaoyang Lv, Zsolt Kira
---
Automatically discovering image categories in unlabeled natural images is one
of the important goals of unsupervised learning. However, the task is
challenging and even human beings define visual categories based on a large
amount of prior knowledge. In this paper, we similarly utilize prior knowledge
to facilitate the discovery of image categories. We present a novel end-to-end
network to map unlabeled images to categories as a clustering network. We
propose that this network can be learned with contrastive loss which is only
based on weak binary pair-wise constraints. Such binary constraints can be
learned from datasets in other domains as transferred similarity functions,
which mimic a simple knowledge transfer. We first evaluate our experiments on
the MNIST dataset as a proof of concept, based on predicted similarities
trained on Omniglot, showing a 99% accuracy which significantly outperforms
clustering based approaches. Then we evaluate the discovery performance on
Cifar-10, STL-10, and ImageNet, which achieves both state-of-the-art accuracy
and shows it can be scalable to various large natural images.