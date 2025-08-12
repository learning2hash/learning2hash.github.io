---
layout: publication
title: Classifying Relations By Ranking With Convolutional Neural Networks
authors: Cicero Nogueira Dos Santos, Bing Xiang, Bowen Zhou
conference: 'Proceedings of the 53rd Annual Meeting of the Association for Computational
  Linguistics and the 7th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2015
bibkey: santos2015classifying
citations: 485
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1504.06580'}]
tags: []
short_authors: Cicero Nogueira Dos Santos, Bing Xiang, Bowen Zhou
---
Relation classification is an important semantic processing task for which
state-ofthe-art systems still rely on costly handcrafted features. In this work
we tackle the relation classification task using a convolutional neural network
that performs classification by ranking (CR-CNN). We propose a new pairwise
ranking loss function that makes it easy to reduce the impact of artificial
classes. We perform experiments using the the SemEval-2010 Task 8 dataset,
which is designed for the task of classifying the relationship between two
nominals marked in a sentence. Using CRCNN, we outperform the state-of-the-art
for this dataset and achieve a F1 of 84.1 without using any costly handcrafted
features. Additionally, our experimental results show that: (1) our approach is
more effective than CNN followed by a softmax classifier; (2) omitting the
representation of the artificial class Other improves both precision and
recall; and (3) using only word embeddings as input features is enough to
achieve state-of-the-art results if we consider only the text between the two
target nominals.