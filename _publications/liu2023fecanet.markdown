---
layout: publication
title: 'Fecanet: Boosting Few-shot Semantic Segmentation With Feature-enhanced Context-aware
  Network'
authors: Huafeng Liu, Pai Peng, Tao Chen, Qiong Wang, Yazhou Yao, Xian-Sheng Hua
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: liu2023fecanet
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.08160'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot semantic segmentation is the task of learning to locate each pixel
of the novel class in the query image with only a few annotated support images.
The current correlation-based methods construct pair-wise feature correlations
to establish the many-to-many matching because the typical prototype-based
approaches cannot learn fine-grained correspondence relations. However, the
existing methods still suffer from the noise contained in naive correlations
and the lack of context semantic information in correlations. To alleviate
these problems mentioned above, we propose a Feature-Enhanced Context-Aware
Network (FECANet). Specifically, a feature enhancement module is proposed to
suppress the matching noise caused by inter-class local similarity and enhance
the intra-class relevance in the naive correlation. In addition, we propose a
novel correlation reconstruction module that encodes extra correspondence
relations between foreground and background and multi-scale context semantic
features, significantly boosting the encoder to capture a reliable matching
pattern. Experiments on PASCAL-\(5^i\) and COCO-\(20^i\) datasets demonstrate that
our proposed FECANet leads to remarkable improvement compared to previous
state-of-the-arts, demonstrating its effectiveness.