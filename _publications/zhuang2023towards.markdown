---
layout: publication
title: Towards Fast And Accurate Image-text Retrieval With Self-supervised Fine-grained
  Alignment
authors: Jiamin Zhuang, Jing Yu, Yang Ding, Xiangyan Qu, Yue Hu
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: zhuang2023towards
citations: 5
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2308.14009'}]
tags: ["Datasets", "Efficiency", "Self-Supervised", "Similarity Search", "Supervised", "Text Retrieval", "Tools & Libraries"]
short_authors: Zhuang et al.
---
Image-text retrieval requires the system to bridge the heterogenous gap
between vision and language for accurate retrieval while keeping the network
lightweight-enough for efficient retrieval. Existing trade-off solutions mainly
study from the view of incorporating cross-modal interactions with the
independent-embedding framework or leveraging stronger pretrained encoders,
which still demand time-consuming similarity measurement or heavyweight model
structure in the retrieval stage. In this work, we propose an image-text
alignment module SelfAlign on top of the independent-embedding framework, which
improves the retrieval accuracy while maintains the retrieval efficiency
without extra supervision. SelfAlign contains two collaborative sub-modules
that force image-text alignment at both concept level and context level by
self-supervised contrastive learning. It does not require cross-modal embedding
interactions during training while maintaining independent image and text
encoders during retrieval. With comparable time cost, SelfAlign consistently
boosts the accuracy of state-of-the-art non-pretraining independent-embedding
models respectively by 9.1%, 4.2% and 6.6% in terms of R@sum score on
Flickr30K, MSCOCO 1K and MS-COCO 5K datasets. The retrieval accuracy also
outperforms most existing interactive-embedding models with orders of magnitude
decrease in retrieval time. The source code is available at:
https://github.com/Zjamie813/SelfAlign.