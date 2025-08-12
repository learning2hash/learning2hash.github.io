---
layout: publication
title: Instance Similarity Learning For Unsupervised Feature Representation
authors: Ziwei Wang, Yunsong Wang, Ziyi Wu, Jiwen Lu, Jie Zhou
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: wang2021instance
citations: 9
additional_links: [{name: Code, url: 'https://github.com/ZiweiWangTHU/ISL.git'}, {
    name: Paper, url: 'https://arxiv.org/abs/2108.02721'}]
tags: ["Distance Metric Learning", "ICCV", "Unsupervised"]
short_authors: Wang et al.
---
In this paper, we propose an instance similarity learning (ISL) method for
unsupervised feature representation. Conventional methods assign close instance
pairs in the feature space with high similarity, which usually leads to wrong
pairwise relationship for large neighborhoods because the Euclidean distance
fails to depict the true semantic similarity on the feature manifold. On the
contrary, our method mines the feature manifold in an unsupervised manner,
through which the semantic similarity among instances is learned in order to
obtain discriminative representations. Specifically, we employ the Generative
Adversarial Networks (GAN) to mine the underlying feature manifold, where the
generated features are applied as the proxies to progressively explore the
feature manifold so that the semantic similarity among instances is acquired as
reliable pseudo supervision. Extensive experiments on image classification
demonstrate the superiority of our method compared with the state-of-the-art
methods. The code is available at https://github.com/ZiweiWangTHU/ISL.git.