---
layout: publication
title: Introspective Deep Metric Learning
authors: Chengkun Wang, Wenzhao Zheng, Zheng Zhu, Jie Zhou, Jiwen Lu
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: wang2023introspective
citations: 18
additional_links: [{name: Code, url: 'https://github.com/wzzheng/IDML'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.09982'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Robustness"]
short_authors: Wang et al.
---
This paper proposes an introspective deep metric learning (IDML) framework
for uncertainty-aware comparisons of images. Conventional deep metric learning
methods focus on learning a discriminative embedding to describe the semantic
features of images, which ignore the existence of uncertainty in each image
resulting from noise or semantic ambiguity. Training without awareness of these
uncertainties causes the model to overfit the annotated labels during training
and produce unsatisfactory judgments during inference. Motivated by this, we
argue that a good similarity model should consider the semantic discrepancies
with awareness of the uncertainty to better deal with ambiguous images for more
robust training. To achieve this, we propose to represent an image using not
only a semantic embedding but also an accompanying uncertainty embedding, which
describes the semantic characteristics and ambiguity of an image, respectively.
We further propose an introspective similarity metric to make similarity
judgments between images considering both their semantic differences and
ambiguities. The gradient analysis of the proposed metric shows that it enables
the model to learn at an adaptive and slower pace to deal with the uncertainty
during training. The proposed IDML framework improves the performance of deep
metric learning through uncertainty modeling and attains state-of-the-art
results on the widely used CUB-200-2011, Cars196, and Stanford Online Products
datasets for image retrieval and clustering. We further provide an in-depth
analysis of our framework to demonstrate the effectiveness and reliability of
IDML. Code: https://github.com/wzzheng/IDML.