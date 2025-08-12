---
layout: publication
title: Rethink Arbitrary Style Transfer With Transformer And Contrastive Learning
authors: Zhanjie Zhang, Jiakai Sun, Guangyuan Li, Lei Zhao, Quanwei Zhang, Zehua Lan,
  Haolin Yin, Wei Xing, Huaizhong Lin, Zhiwen Zuo
conference: Computer Vision and Image Understanding
year: 2024
bibkey: zhang2024rethink
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.13584'}]
tags: ["Self-Supervised"]
short_authors: Zhang et al.
---
Arbitrary style transfer holds widespread attention in research and boasts
numerous practical applications. The existing methods, which either employ
cross-attention to incorporate deep style attributes into content attributes or
use adaptive normalization to adjust content features, fail to generate
high-quality stylized images. In this paper, we introduce an innovative
technique to improve the quality of stylized images. Firstly, we propose Style
Consistency Instance Normalization (SCIN), a method to refine the alignment
between content and style features. In addition, we have developed an
Instance-based Contrastive Learning (ICL) approach designed to understand the
relationships among various styles, thereby enhancing the quality of the
resulting stylized images. Recognizing that VGG networks are more adept at
extracting classification features and need to be better suited for capturing
style features, we have also introduced the Perception Encoder (PE) to capture
style features. Extensive experiments demonstrate that our proposed method
generates high-quality stylized images and effectively prevents artifacts
compared with the existing state-of-the-art methods.