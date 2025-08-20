---
layout: publication
title: Deep Person Re-identification With Improved Embedding And Efficient Training
authors: Haibo Jin, Xiaobo Wang, Shengcai Liao, Stan Z. Li
conference: 2017 IEEE International Joint Conference on Biometrics (IJCB)
year: 2017
bibkey: jin2017deep
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.03332'}]
tags: [Evaluation, Datasets]
short_authors: Jin et al.
---
Person re-identification task has been greatly boosted by deep convolutional
neural networks (CNNs) in recent years. The core of which is to enlarge the
inter-class distinction as well as reduce the intra-class variance. However, to
achieve this, existing deep models prefer to adopt image pairs or triplets to
form verification loss, which is inefficient and unstable since the number of
training pairs or triplets grows rapidly as the number of training data grows.
Moreover, their performance is limited since they ignore the fact that
different dimension of embedding may play different importance. In this paper,
we propose to employ identification loss with center loss to train a deep model
for person re-identification. The training process is efficient since it does
not require image pairs or triplets for training while the inter-class
distinction and intra-class variance are well handled. To boost the
performance, a new feature reweighting (FRW) layer is designed to explicitly
emphasize the importance of each embedding dimension, thus leading to an
improved embedding. Experiments on several benchmark datasets have shown the
superiority of our method over the state-of-the-art alternatives on both
accuracy and speed.