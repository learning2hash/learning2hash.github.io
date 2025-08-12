---
layout: publication
title: 'Visual Transformers: Token-based Image Representation And Processing For Computer
  Vision'
authors: Bichen Wu, Chenfeng Xu, Xiaoliang Dai, Alvin Wan, Peizhao Zhang, Zhicheng
  Yan, Masayoshi Tomizuka, Joseph Gonzalez, Kurt Keutzer, Peter Vajda
conference: Arxiv
year: 2020
bibkey: wu2020visual
citations: 315
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.03677'}]
tags: ["Image Retrieval", "Transformer Based ANN"]
short_authors: Wu et al.
---
Computer vision has achieved remarkable success by (a) representing images as
uniformly-arranged pixel arrays and (b) convolving highly-localized features.
However, convolutions treat all image pixels equally regardless of importance;
explicitly model all concepts across all images, regardless of content; and
struggle to relate spatially-distant concepts. In this work, we challenge this
paradigm by (a) representing images as semantic visual tokens and (b) running
transformers to densely model token relationships. Critically, our Visual
Transformer operates in a semantic token space, judiciously attending to
different image parts based on context. This is in sharp contrast to
pixel-space transformers that require orders-of-magnitude more compute. Using
an advanced training recipe, our VTs significantly outperform their
convolutional counterparts, raising ResNet accuracy on ImageNet top-1 by 4.6 to
7 points while using fewer FLOPs and parameters. For semantic segmentation on
LIP and COCO-stuff, VT-based feature pyramid networks (FPN) achieve 0.35 points
higher mIoU while reducing the FPN module's FLOPs by 6.5x.