---
layout: publication
title: Confusable Learning For Large-class Few-shot Classification
authors: Bingcong Li, Bo Han, Zhuowei Wang, Jing Jiang, Guodong Long
conference: Lecture Notes in Computer Science
year: 2021
bibkey: li2020confusable
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.03154'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Li et al.
---
Few-shot image classification is challenging due to the lack of ample samples
in each class. Such a challenge becomes even tougher when the number of classes
is very large, i.e., the large-class few-shot scenario. In this novel scenario,
existing approaches do not perform well because they ignore confusable classes,
namely similar classes that are difficult to distinguish from each other. These
classes carry more information. In this paper, we propose a biased learning
paradigm called Confusable Learning, which focuses more on confusable classes.
Our method can be applied to mainstream meta-learning algorithms. Specifically,
our method maintains a dynamically updating confusion matrix, which analyzes
confusable classes in the dataset. Such a confusion matrix helps meta learners
to emphasize on confusable classes. Comprehensive experiments on Omniglot,
Fungi, and ImageNet demonstrate the efficacy of our method over
state-of-the-art baselines.