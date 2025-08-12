---
layout: publication
title: Generalized Semantic Contrastive Learning Via Embedding Side Information For
  Few-shot Object Detection
authors: Ruoyu Chen, Hua Zhang, Jingzhi Li, Li Liu, Zhen Huang, Xiaochun Cao
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2025
bibkey: chen2025generalized
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.07060'}]
tags: ["Self-Supervised"]
short_authors: Chen et al.
---
The objective of few-shot object detection (FSOD) is to detect novel objects
with few training samples. The core challenge of this task is how to construct
a generalized feature space for novel categories with limited data on the basis
of the base category space, which could adapt the learned detection model to
unknown scenarios. However, limited by insufficient samples for novel
categories, two issues still exist: (1) the features of the novel category are
easily implicitly represented by the features of the base category, leading to
inseparable classifier boundaries, (2) novel categories with fewer data are not
enough to fully represent the distribution, where the model fine-tuning is
prone to overfitting. To address these issues, we introduce the side
information to alleviate the negative influences derived from the feature space
and sample viewpoints and formulate a novel generalized feature representation
learning method for FSOD. Specifically, we first utilize embedding side
information to construct a knowledge matrix to quantify the semantic
relationship between the base and novel categories. Then, to strengthen the
discrimination between semantically similar categories, we further develop
contextual semantic supervised contrastive learning which embeds side
information. Furthermore, to prevent overfitting problems caused by sparse
samples, a side-information guided region-aware masked module is introduced to
augment the diversity of samples, which finds and abandons biased information
that discriminates between similar categories via counterfactual explanation,
and refines the discriminative representation space further. Extensive
experiments using ResNet and ViT backbones on PASCAL VOC, MS COCO, LVIS V1,
FSOD-1K, and FSVOD-500 benchmarks demonstrate that our model outperforms the
previous state-of-the-art methods, significantly improving the ability of FSOD
in most shots/splits.