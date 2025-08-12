---
layout: publication
title: Exploring Fine-grained Representation And Recomposition For Cloth-changing
  Person Re-identification
authors: Qizao Wang, Xuelin Qian, Bin Li, Xiangyang Xue, Yanwei Fu
conference: IEEE Transactions on Information Forensics and Security
year: 2024
bibkey: wang2023exploring
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.10692'}]
tags: []
short_authors: Wang et al.
---
Cloth-changing person Re-IDentification (Re-ID) is a particularly challenging
task, suffering from two limitations of inferior discriminative features and
limited training samples. Existing methods mainly leverage auxiliary
information to facilitate identity-relevant feature learning, including
soft-biometrics features of shapes or gaits, and additional labels of clothing.
However, this information may be unavailable in real-world applications. In
this paper, we propose a novel FIne-grained Representation and Recomposition
(FIRe\\(^\{2\}\\)) framework to tackle both limitations without any auxiliary
annotation or data. Specifically, we first design a Fine-grained Feature Mining
(FFM) module to separately cluster images of each person. Images with similar
so-called fine-grained attributes (e.g., clothes and viewpoints) are encouraged
to cluster together. An attribute-aware classification loss is introduced to
perform fine-grained learning based on cluster labels, which are not shared
among different people, promoting the model to learn identity-relevant
features. Furthermore, to take full advantage of fine-grained attributes, we
present a Fine-grained Attribute Recomposition (FAR) module by recomposing
image features with different attributes in the latent space. It significantly
enhances robust feature learning. Extensive experiments demonstrate that
FIRe\\(^\{2\}\\) can achieve state-of-the-art performance on five widely-used
cloth-changing person Re-ID benchmarks. The code is available at
https://github.com/QizaoWang/FIRe-CCReID.