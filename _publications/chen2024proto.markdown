---
layout: publication
title: 'Proto-ood: Enhancing OOD Object Detection With Prototype Feature Similarity'
authors: Junkun Chen, Jilin Mei, Liang Chen, Fangzhou Zhao, Yan Xing, Yu Hu
conference: Arxiv
year: 2024
bibkey: chen2024proto
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.05466'}]
tags: ["Distance Metric Learning"]
short_authors: Chen et al.
---
Neural networks that are trained on limited category samples often mispredict
out-of-distribution (OOD) objects. We observe that features of the same
category are more tightly clustered in feature space, while those of different
categories are more dispersed. Based on this, we propose using prototype
similarity for OOD detection. Drawing on widely used prototype features in
few-shot learning, we introduce a novel OOD detection network structure
(Proto-OOD). Proto-OOD enhances the representativeness of category prototypes
using contrastive loss and detects OOD data by evaluating the similarity
between input features and category prototypes. During training, Proto-OOD
generates OOD samples for training the similarity module with a negative
embedding generator. When Pascal VOC are used as the in-distribution dataset
and MS-COCO as the OOD dataset, Proto-OOD significantly reduces the FPR (false
positive rate). Moreover, considering the limitations of existing evaluation
metrics, we propose a more reasonable evaluation protocol. The code will be
released.