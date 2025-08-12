---
layout: publication
title: Negative Prototypes Guided Contrastive Learning For WSOD
authors: Yu Zhang, Chuang Zhu, Guoqing Yang, Siqi Chen
conference: Arxiv
year: 2024
bibkey: zhang2024negative
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.18576'}]
tags: ["Self-Supervised"]
short_authors: Zhang et al.
---
Weakly Supervised Object Detection (WSOD) with only image-level annotation
has recently attracted wide attention. Many existing methods ignore the
inter-image relationship of instances which share similar characteristics while
can certainly be determined not to belong to the same category. Therefore, in
order to make full use of the weak label, we propose the Negative Prototypes
Guided Contrastive learning (NPGC) architecture. Firstly, we define Negative
Prototype as the proposal with the highest confidence score misclassified for
the category that does not appear in the label. Unlike other methods that only
utilize category positive feature, we construct an online updated global
feature bank to store both positive prototypes and negative prototypes.
Meanwhile, we propose a pseudo label sampling module to mine reliable instances
and discard the easily misclassified instances based on the feature similarity
with corresponding prototypes in global feature bank. Finally, we follow the
contrastive learning paradigm to optimize the proposal's feature representation
by attracting same class samples closer and pushing different class samples
away in the embedding space. Extensive experiments have been conducted on
VOC07, VOC12 datasets, which shows that our proposed method achieves the
state-of-the-art performance.