---
layout: publication
title: 'Tsf: Transformer-based Semantic Filter For Few-shot Learning'
authors: Jinxiang Lai, Siqian Yang, Wenlong Liu, Yi Zeng, Zhongyi Huang, Wenlong Wu,
  Jun Liu, Bin-Bin Gao, Chengjie Wang
conference: Lecture Notes in Computer Science
year: 2022
bibkey: lai2022tsf
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.00868'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Lai et al.
---
Few-Shot Learning (FSL) alleviates the data shortage challenge via embedding
discriminative target-aware features among plenty seen (base) and few unseen
(novel) labeled samples. Most feature embedding modules in recent FSL methods
are specially designed for corresponding learning tasks (e.g., classification,
segmentation, and object detection), which limits the utility of embedding
features. To this end, we propose a light and universal module named
transformer-based Semantic Filter (tSF), which can be applied for different FSL
tasks. The proposed tSF redesigns the inputs of a transformer-based structure
by a semantic filter, which not only embeds the knowledge from whole base set
to novel set but also filters semantic features for target category.
Furthermore, the parameters of tSF is equal to half of a standard transformer
block (less than 1M). In the experiments, our tSF is able to boost the
performances in different classic few-shot learning tasks (about 2%
improvement), especially outperforms the state-of-the-arts on multiple
benchmark datasets in few-shot classification task.