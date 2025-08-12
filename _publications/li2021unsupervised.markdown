---
layout: publication
title: Unsupervised Person Re-identification With Multi-label Learning Guided Self-paced
  Clustering
authors: Qing Li, Xiaojiang Peng, Yu Qiao, Qi Hao
conference: Pattern Recognition
year: 2022
bibkey: li2021unsupervised
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04580'}]
tags: ["Unsupervised"]
short_authors: Li et al.
---
Although unsupervised person re-identification (Re-ID) has drawn increasing
research attention recently, it remains challenging to learn discriminative
features without annotations across disjoint camera views. In this paper, we
address the unsupervised person Re-ID with a conceptually novel yet simple
framework, termed as Multi-label Learning guided self-paced Clustering (MLC).
MLC mainly learns discriminative features with three crucial modules, namely a
multi-scale network, a multi-label learning module, and a self-paced clustering
module. Specifically, the multi-scale network generates multi-granularity
person features in both global and local views. The multi-label learning module
leverages a memory feature bank and assigns each image with a multi-label
vector based on the similarities between the image and feature bank. After
multi-label training for several epochs, the self-paced clustering joins in
training and assigns a pseudo label for each image. The benefits of our MLC
come from three aspects: i) the multi-scale person features for better
similarity measurement, ii) the multi-label assignment based on the whole
dataset ensures that every image can be trained, and iii) the self-paced
clustering removes some noisy samples for better feature learning. Extensive
experiments on three popular large-scale Re-ID benchmarks demonstrate that our
MLC outperforms previous state-of-the-art methods and significantly improves
the performance of unsupervised person Re-ID.