---
layout: publication
title: Neighborhood Contrastive Learning For Novel Class Discovery
authors: Zhun Zhong, Enrico Fini, Subhankar Roy, Zhiming Luo, Elisa Ricci, Nicu Sebe
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: zhong2021neighborhood
citations: 108
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.10731'}]
tags: ["CVPR", "Datasets", "Distance Metric Learning", "Evaluation", "Tools & Libraries"]
short_authors: Zhong et al.
---
In this paper, we address Novel Class Discovery (NCD), the task of unveiling
new classes in a set of unlabeled samples given a labeled dataset with known
classes. We exploit the peculiarities of NCD to build a new framework, named
Neighborhood Contrastive Learning (NCL), to learn discriminative
representations that are important to clustering performance. Our contribution
is twofold. First, we find that a feature extractor trained on the labeled set
generates representations in which a generic query sample and its neighbors are
likely to share the same class. We exploit this observation to retrieve and
aggregate pseudo-positive pairs with contrastive learning, thus encouraging the
model to learn more discriminative representations. Second, we notice that most
of the instances are easily discriminated by the network, contributing less to
the contrastive loss. To overcome this issue, we propose to generate hard
negatives by mixing labeled and unlabeled samples in the feature space. We
experimentally demonstrate that these two ingredients significantly contribute
to clustering performance and lead our model to outperform state-of-the-art
methods by a large margin (e.g., clustering accuracy +13% on CIFAR-100 and +8%
on ImageNet).