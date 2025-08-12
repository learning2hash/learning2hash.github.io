---
layout: publication
title: Reverse Region-to-entity Annotation For Pixel-level Visual Entity Linking
authors: Zhengfei Xu, Sijia Zhao, Yanchao Hao, Xiaolong Liu, Lili Li, Yuyang Yin,
  Bo Li, Xi Chen, Xin Xin
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: xu2024reverse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.13614'}]
tags: ["AAAI"]
short_authors: Xu et al.
---
Visual Entity Linking (VEL) is a crucial task for achieving fine-grained
visual understanding, matching objects within images (visual mentions) to
entities in a knowledge base. Previous VEL tasks rely on textual inputs, but
writing queries for complex scenes can be challenging. Visual inputs like
clicks or bounding boxes offer a more convenient alternative. Therefore, we
propose a new task, Pixel-Level Visual Entity Linking (PL-VEL), which uses
pixel masks from visual inputs to refer to objects, supplementing reference
methods for VEL. To facilitate research on this task, we have constructed the
MaskOVEN-Wiki dataset through an entirely automatic reverse region-entity
annotation framework. This dataset contains over 5 million annotations aligning
pixel-level regions with entity-level labels, which will advance visual
understanding towards fine-grained. Moreover, as pixel masks correspond to
semantic regions in an image, we enhance previous patch-interacted attention
with region-interacted attention by a visual semantic tokenization approach.
Manual evaluation results indicate that the reverse annotation framework
achieved a 94.8% annotation success rate. Experimental results show that models
trained on this dataset improved accuracy by 18 points compared to zero-shot
models. Additionally, the semantic tokenization method achieved a 5-point
accuracy improvement over the trained baseline.