---
layout: publication
title: Text-guided Image Restoration And Semantic Enhancement For Text-to-image Person
  Retrieval
authors: Delong Liu, Haiwen Li, Zhicheng Zhao, Yuan Dong
conference: Neural Networks
year: 2024
bibkey: liu2023text
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.09059'}]
tags: []
short_authors: Liu et al.
---
The goal of Text-to-Image Person Retrieval (TIPR) is to retrieve specific
person images according to the given textual descriptions. A primary challenge
in this task is bridging the substantial representational gap between visual
and textual modalities. The prevailing methods map texts and images into
unified embedding space for matching, while the intricate semantic
correspondences between texts and images are still not effectively constructed.
To address this issue, we propose a novel TIPR framework to build fine-grained
interactions and alignment between person images and the corresponding texts.
Specifically, via fine-tuning the Contrastive Language-Image Pre-training
(CLIP) model, a visual-textual dual encoder is firstly constructed, to
preliminarily align the image and text features. Secondly, a Text-guided Image
Restoration (TIR) auxiliary task is proposed to map abstract textual entities
to specific image regions, improving the alignment between local textual and
visual embeddings. Additionally, a cross-modal triplet loss is presented to
handle hard samples, and further enhance the model's discriminability for minor
differences. Moreover, a pruning-based text data augmentation approach is
proposed to enhance focus on essential elements in descriptions, thereby
avoiding excessive model attention to less significant information. The
experimental results show our proposed method outperforms state-of-the-art
methods on three popular benchmark datasets, and the code will be made publicly
available at https://github.com/Delong-liu-bupt/SEN.