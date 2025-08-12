---
layout: publication
title: Training ELECTRA Augmented With Multi-word Selection
authors: Jiaming Shen, Jialu Liu, Tianqi Liu, Cong Yu, Jiawei Han
conference: 'Findings of the Association for Computational Linguistics: ACL-IJCNLP
  2021'
year: 2021
bibkey: shen2021training
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.00139'}]
tags: []
short_authors: Shen et al.
---
Pre-trained text encoders such as BERT and its variants have recently
achieved state-of-the-art performances on many NLP tasks. While being
effective, these pre-training methods typically demand massive computation
resources. To accelerate pre-training, ELECTRA trains a discriminator that
predicts whether each input token is replaced by a generator. However, this new
task, as a binary classification, is less semantically informative. In this
study, we present a new text encoder pre-training method that improves ELECTRA
based on multi-task learning. Specifically, we train the discriminator to
simultaneously detect replaced tokens and select original tokens from candidate
sets. We further develop two techniques to effectively combine all pre-training
tasks: (1) using attention-based networks for task-specific heads, and (2)
sharing bottom layers of the generator and the discriminator. Extensive
experiments on GLUE and SQuAD datasets demonstrate both the effectiveness and
the efficiency of our proposed method.