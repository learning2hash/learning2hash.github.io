---
layout: publication
title: Weakly-supervised Object Localization For Few-shot Learning And Fine-grained
  Few-shot Learning
authors: Xiaojian He, Jinfu Lin, Junming Shen
conference: Arxiv
year: 2020
bibkey: he2020weakly
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.00874'}]
tags: ["Few Shot & Zero Shot", "Supervised"]
short_authors: Xiaojian He, Jinfu Lin, Junming Shen
---
Few-shot learning (FSL) aims to learn novel visual categories from very few
samples, which is a challenging problem in real-world applications. Many
methods of few-shot classification work well on general images to learn global
representation. However, they can not deal with fine-grained categories well at
the same time due to a lack of subtle and local information. We argue that
localization is an efficient approach because it directly provides the
discriminative regions, which is critical for both general classification and
fine-grained classification in a low data regime. In this paper, we propose a
Self-Attention Based Complementary Module (SAC Module) to fulfill the
weakly-supervised object localization, and more importantly produce the
activated masks for selecting discriminative deep descriptors for few-shot
classification. Based on each selected deep descriptor, Semantic Alignment
Module (SAM) calculates the semantic alignment distance between the query and
support images to boost classification performance. Extensive experiments show
our method outperforms the state-of-the-art methods on benchmark datasets under
various settings, especially on the fine-grained few-shot tasks. Besides, our
method achieves superior performance over previous methods when training the
model on miniImageNet and evaluating it on the different datasets,
demonstrating its superior generalization capacity. Extra visualization shows
the proposed method can localize the key objects more interval.