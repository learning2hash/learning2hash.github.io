---
layout: publication
title: 'Query2label: A Simple Transformer Way To Multi-label Classification'
authors: Shilong Liu, Lei Zhang, Xiao Yang, Hang Su, Jun Zhu
conference: Arxiv
year: 2021
bibkey: liu2021query2label
citations: 111
additional_links: [{name: Code, url: 'https://github.com/SlongLiu/query2labels'},
  {name: Paper, url: 'https://arxiv.org/abs/2107.10834'}]
tags: []
short_authors: Liu et al.
---
This paper presents a simple and effective approach to solving the
multi-label classification problem. The proposed approach leverages Transformer
decoders to query the existence of a class label. The use of Transformer is
rooted in the need of extracting local discriminative features adaptively for
different labels, which is a strongly desired property due to the existence of
multiple objects in one image. The built-in cross-attention module in the
Transformer decoder offers an effective way to use label embeddings as queries
to probe and pool class-related features from a feature map computed by a
vision backbone for subsequent binary classifications. Compared with prior
works, the new framework is simple, using standard Transformers and vision
backbones, and effective, consistently outperforming all previous works on five
multi-label classification data sets, including MS-COCO, PASCAL VOC, NUS-WIDE,
and Visual Genome. Particularly, we establish \(91.3%\) mAP on MS-COCO. We hope
its compact structure, simple implementation, and superior performance serve as
a strong baseline for multi-label classification tasks and future studies. The
code will be available soon at https://github.com/SlongLiu/query2labels.