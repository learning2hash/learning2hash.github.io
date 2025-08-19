---
layout: publication
title: 'OV-DQUO: Open-vocabulary DETR With Denoising Text Query Training And Open-world
  Unknown Objects Supervision'
authors: Junjie Wang, Bin Chen, Bin Kang, Yulin Li, Yichi Chen, Weizhi Xian, Huifeng
  Chang, Yong Xu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: wang2025ov
citations: 0
additional_links: [{name: Code, url: 'https://github.com/xiaomoguhz/OV-DQUO'}, {name: Paper,
    url: 'https://arxiv.org/abs/2405.17913'}]
tags: [Self-Supervised, Transformer-based ANN, AAAI, Evaluation]
short_authors: Wang et al.
---
Open-vocabulary detection aims to detect objects from novel categories beyond
the base categories on which the detector is trained. However, existing
open-vocabulary detectors trained on base category data tend to assign higher
confidence to trained categories and confuse novel categories with the
background. To resolve this, we propose OV-DQUO, an
\textbf\{O\}pen-\textbf\{V\}ocabulary DETR with \textbf\{D\}enoising text
\textbf\{Q\}uery training and open-world \textbf\{U\}nknown \textbf\{O\}bjects
supervision. Specifically, we introduce a wildcard matching method. This method
enables the detector to learn from pairs of unknown objects recognized by the
open-world detector and text embeddings with general semantics, mitigating the
confidence bias between base and novel categories. Additionally, we propose a
denoising text query training strategy. It synthesizes foreground and
background query-box pairs from open-world unknown objects to train the
detector through contrastive learning, enhancing its ability to distinguish
novel objects from the background. We conducted extensive experiments on the
challenging OV-COCO and OV-LVIS benchmarks, achieving new state-of-the-art
results of 45.6 AP50 and 39.3 mAP on novel categories respectively, without the
need for additional training data. Models and code are released at
https://github.com/xiaomoguhz/OV-DQUO