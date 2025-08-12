---
layout: publication
title: Leaf Cultivar Identification Via Prototype-enhanced Learning
authors: Yiyi Zhang, Zhiwen Ying, Ying Zheng, Cuiling Wu, Nannan Li, Jun Wang, Xianzhong
  Feng, Xiaogang Xu
conference: Computer Vision and Image Understanding
year: 2024
bibkey: zhang2023leaf
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03351'}]
tags: ["Datasets", "Evaluation"]
short_authors: Zhang et al.
---
Plant leaf identification is crucial for biodiversity protection and
conservation and has gradually attracted the attention of academia in recent
years. Due to the high similarity among different varieties, leaf cultivar
recognition is also considered to be an ultra-fine-grained visual
classification (UFGVC) task, which is facing a huge challenge. In practice, an
instance may be related to multiple varieties to varying degrees, especially in
the UFGVC datasets. However, deep learning methods trained on one-hot labels
fail to reflect patterns shared across categories and thus perform poorly on
this task. To address this issue, we generate soft targets integrated with
inter-class similarity information. Specifically, we continuously update the
prototypical features for each category and then capture the similarity scores
between instances and prototypes accordingly. Original one-hot labels and the
similarity scores are incorporated to yield enhanced labels. Prototype-enhanced
soft labels not only contain original one-hot label information, but also
introduce rich inter-category semantic association information, thus providing
more effective supervision for deep model training. Extensive experimental
results on public datasets show that our method can significantly improve the
performance on the UFGVC task of leaf cultivar identification.