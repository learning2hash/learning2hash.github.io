---
layout: publication
title: 'Semantic Regularization: Improve Few-shot Image Classification By Reducing
  Meta Shift'
authors: da Chen, Yongliang Yang, Zunlei Feng, Xiang Wu, Mingli Song, Wenbin Li, Yuan
  He, Hui Xue, Feng Mao
conference: Arxiv
year: 2019
bibkey: chen2019semantic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.08395'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Few-shot image classification requires the classifier to robustly cope with
unseen classes even if there are only a few samples for each class. Recent
advances benefit from the meta-learning process where episodic tasks are formed
to train a model that can adapt to class change. However, these task sare
independent to each other and existing works mainly rely on limited samples of
individual support set in a single meta task. This strategy leads to severe
meta shift issues across multiple tasks, meaning the learned prototypes or
class descriptors are not stable as each task only involves their own support
set. To avoid this problem, we propose a concise Semantic RegularizationNetwork
to learn a common semantic space under the framework of meta-learning. In this
space, all class descriptors can be regularized by the learned semantic basis,
which can effectively solve the meta shift problem. The key is to train a class
encoder and decoder structure that can encode the sample embedding features
into the semantic domain with trained semantic basis, and generate a more
stable and general class descriptor from the decoder. We evaluate our work by
extensive comparisons with previous methods on three benchmark datasets
(MiniImageNet, TieredImageNet, and CUB). The results show that the semantic
regularization module improves performance by 4%-7% over the baseline method,
and achieves competitive results over the current state-of-the-art models.