---
layout: publication
title: 'Detailclip: Injecting Image Details Into Clip''s Feature Space'
authors: Zilun Zhang, Cuifeng Shen, Yuan Shen, Huixin Xiong, Xinyu Zhou, Tiancheng
  Zhao, Jianwei Yin
conference: Arxiv
year: 2022
bibkey: zhang2022detailclip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.14649'}]
tags: ["Datasets", "Evaluation", "Supervised", "Tools & Libraries"]
short_authors: Zhang et al.
---
Although CLIP-like Visual Language Models provide a functional joint feature space for image and text, due to the limitation of the CILP-like model's image input size (e.g., 224), subtle details are lost in the feature representation if we input high-resolution images (e.g., 2240). In this work, we introduce an efficient framework that can produce a single feature representation for a high-resolution image that injects image details and shares the same semantic space as the original CLIP. In the framework, we train a feature fusing model based on CLIP features extracted from a carefully designed image patch method that can cover objects of any scale, weakly supervised by image-agnostic class prompted queries. We validate our framework by retrieving images from class prompted queries on the real world and synthetic datasets, showing significant performance improvement on these tasks. Furthermore, to fully demonstrate our framework's detail retrieval ability, we construct a CLEVR-like synthetic dataset called CLVER-DS, which is fully annotated and has a controllable object scale.