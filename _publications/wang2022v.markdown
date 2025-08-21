---
layout: publication
title: 'V\(^2\)L: Leveraging Vision And Vision-language Models Into Large-scale Product
  Retrieval'
authors: Wenhao Wang, Yifan Sun, Zongxin Yang, Yi Yang
conference: Arxiv
year: 2022
bibkey: wang2022v
citations: 0
additional_links: [{name: Code, url: 'https://github.com/WangWenhao0716/V2L\'}, {
    name: Paper, url: 'https://arxiv.org/abs/2207.12994'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Scalability", "Self-Supervised", "Supervised"]
short_authors: Wang et al.
---
Product retrieval is of great importance in the ecommerce domain. This paper
introduces our 1st-place solution in eBay eProduct Visual Search Challenge
(FGVC9), which is featured for an ensemble of about 20 models from vision
models and vision-language models. While model ensemble is common, we show that
combining the vision models and vision-language models brings particular
benefits from their complementarity and is a key factor to our superiority.
Specifically, for the vision models, we use a two-stage training pipeline which
first learns from the coarse labels provided in the training set and then
conducts fine-grained self-supervised training, yielding a coarse-to-fine
metric learning manner. For the vision-language models, we use the textual
description of the training image as the supervision signals for fine-tuning
the image-encoder (feature extractor). With these designs, our solution
achieves 0.7623 MAR@10, ranking the first place among all the competitors. The
code is available at: \href\{https://github.com/WangWenhao0716/V2L\}\{V\(^2\)L\}.