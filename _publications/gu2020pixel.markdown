---
layout: publication
title: 'From Pixel To Patch: Synthesize Context-aware Features For Zero-shot Semantic
  Segmentation'
authors: Zhangxuan Gu, Siyuan Zhou, Li Niu, Zihan Zhao, Liqing Zhang
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2022
bibkey: gu2020pixel
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.12232'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Gu et al.
---
Zero-shot learning has been actively studied for image classification task to
relieve the burden of annotating image labels. Interestingly, semantic
segmentation task requires more labor-intensive pixel-wise annotation, but
zero-shot semantic segmentation has only attracted limited research interest.
Thus, we focus on zero-shot semantic segmentation, which aims to segment unseen
objects with only category-level semantic representations provided for unseen
categories. In this paper, we propose a novel Context-aware feature Generation
Network (CaGNet), which can synthesize context-aware pixel-wise visual features
for unseen categories based on category-level semantic representations and
pixel-wise contextual information. The synthesized features are used to
finetune the classifier to enable segmenting unseen objects. Furthermore, we
extend pixel-wise feature generation and finetuning to patch-wise feature
generation and finetuning, which additionally considers inter-pixel
relationship. Experimental results on Pascal-VOC, Pascal-Context, and
COCO-stuff show that our method significantly outperforms the existing
zero-shot semantic segmentation methods. Code is available at
https://github.com/bcmi/CaGNetv2-Zero-Shot-Semantic-Segmentation.