---
layout: publication
title: Bringing Multimodality To Amazon Visual Search System
authors: Xinliang Zhu, Michael Huang, Han Ding, Jinyu Yang, Kelvin Chen, Tao Zhou,
  Tal Neiman, Ouye Xie, Son Tran, Benjamin Yao, Doug Gray, Anuj Bindal, Arnab Dhua
conference: Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2024
bibkey: zhu2024bringing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13364'}]
tags: [Distance Metric Learning, KDD, Image Retrieval]
short_authors: Zhu et al.
---
Image to image matching has been well studied in the computer vision
community. Previous studies mainly focus on training a deep metric learning
model matching visual patterns between the query image and gallery images. In
this study, we show that pure image-to-image matching suffers from false
positives caused by matching to local visual patterns. To alleviate this issue,
we propose to leverage recent advances in vision-language pretraining research.
Specifically, we introduce additional image-text alignment losses into deep
metric learning, which serve as constraints to the image-to-image matching
loss. With additional alignments between the text (e.g., product title) and
image pairs, the model can learn concepts from both modalities explicitly,
which avoids matching low-level visual features. We progressively develop two
variants, a 3-tower and a 4-tower model, where the latter takes one more short
text query input. Through extensive experiments, we show that this change leads
to a substantial improvement to the image to image matching problem. We further
leveraged this model for multimodal search, which takes both image and
reformulation text queries to improve search quality. Both offline and online
experiments show strong improvements on the main metrics. Specifically, we see
4.95% relative improvement on image matching click through rate with the
3-tower model and 1.13% further improvement from the 4-tower model.