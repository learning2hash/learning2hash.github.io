---
layout: publication
title: Attribute-guided Multi-level Attention Network For Fine-grained Fashion Retrieval
authors: Ling Xiao, Toshihiko Yamasaki
conference: IEEE Access
year: 2024
bibkey: xiao2022attribute
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.13014'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Ling Xiao, Toshihiko Yamasaki
---
Fine-grained fashion retrieval searches for items that share a similar
attribute with the query image. Most existing methods use a pre-trained feature
extractor (e.g., ResNet 50) to capture image representations. However, a
pre-trained feature backbone is typically trained for image classification and
object detection, which are fundamentally different tasks from fine-grained
fashion retrieval. Therefore, existing methods suffer from a feature gap
problem when directly using the pre-trained backbone for fine-tuning. To solve
this problem, we introduce an attribute-guided multi-level attention network
(AG-MAN). Specifically, we first enhance the pre-trained feature extractor to
capture multi-level image embedding, thereby enriching the low-level features
within these representations. Then, we propose a classification scheme where
images with the same attribute, albeit with different values, are categorized
into the same class. This can further alleviate the feature gap problem by
perturbing object-centric feature learning. Moreover, we propose an improved
attribute-guided attention module for extracting more accurate
attribute-specific representations. Our model consistently outperforms existing
attention based methods when assessed on the FashionAI (62.8788% in MAP),
DeepFashion (8.9804% in MAP), and Zappos50k datasets (93.32% in Prediction
accuracy). Especially, ours improves the most typical ASENet_V2 model by 2.12%,
0.31%, and 0.78% points in FashionAI, DeepFashion, and Zappos50k datasets,
respectively. The source code is available in
https://github.com/Dr-LingXiao/AG-MAN.