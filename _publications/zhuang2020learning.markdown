---
layout: publication
title: Learning Attentive Pairwise Interaction For Fine-grained Classification
authors: Peiqin Zhuang, Yali Wang, Yu Qiao
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: zhuang2020learning
citations: 336
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10191'}]
tags: ["AAAI"]
short_authors: Peiqin Zhuang, Yali Wang, Yu Qiao
---
Fine-grained classification is a challenging problem, due to subtle
differences among highly-confused categories. Most approaches address this
difficulty by learning discriminative representation of individual input image.
On the other hand, humans can effectively identify contrastive clues by
comparing image pairs. Inspired by this fact, this paper proposes a simple but
effective Attentive Pairwise Interaction Network (API-Net), which can
progressively recognize a pair of fine-grained images by interaction.
Specifically, API-Net first learns a mutual feature vector to capture semantic
differences in the input pair. It then compares this mutual vector with
individual vectors to generate gates for each input image. These distinct gate
vectors inherit mutual context on semantic differences, which allow API-Net to
attentively capture contrastive clues by pairwise interaction between two
images. Additionally, we train API-Net in an end-to-end manner with a score
ranking regularization, which can further generalize API-Net by taking feature
priorities into account. We conduct extensive experiments on five popular
benchmarks in fine-grained classification. API-Net outperforms the recent SOTA
methods, i.e., CUB-200-2011 (90.0%), Aircraft(93.9%), Stanford Cars (95.3%),
Stanford Dogs (90.3%), and NABirds (88.1%).