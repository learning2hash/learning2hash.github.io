---
layout: publication
title: Referring Expression Instance Retrieval And A Strong End-to-end Baseline
authors: Xiangzhao Hao, Kuan Zhu, Hongyu Guo, Haiyun Guo, Ning Jiang, Quan Lu, Ming
  Tang, Jinqiao Wang
conference: Proceedings of the 33rd ACM International Conference on Multimedia
year: 2025
bibkey: hao2025referring
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.18246'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Scalability"]
short_authors: Hao et al.
---
Using natural language to query visual information is a fundamental need in real-world applications. Text-Image Retrieval (TIR) retrieves a target image from a gallery based on an image-level description, while Referring Expression Comprehension (REC) localizes a target object within a given image using an instance-level description. However, real-world applications often present more complex demands. Users typically query an instance-level description across a large gallery and expect to receive both relevant image and the corresponding instance location. In such scenarios, TIR struggles with fine-grained descriptions and object-level localization, while REC is limited in its ability to efficiently search large galleries and lacks an effective ranking mechanism. In this paper, we introduce a new task called \textbf\{Referring Expression Instance Retrieval (REIR)\}, which supports both instance-level retrieval and localization based on fine-grained referring expressions. First, we propose a large-scale benchmark for REIR, named REIRCOCO, constructed by prompting advanced vision-language models to generate high-quality referring expressions for instances in the MSCOCO and RefCOCO datasets. Second, we present a baseline method, Contrastive Language-Instance Alignment with Relation Experts (CLARE), which employs a dual-stream architecture to address REIR in an end-to-end manner. Given a referring expression, the textual branch encodes it into a query embedding. The visual branch detects candidate objects and extracts their instance-level visual features. The most similar candidate to the query is selected for bounding box prediction. CLARE is first trained on object detection and REC datasets to establish initial grounding capabilities, then optimized via Contrastive Language-Instance Alignment (CLIA) for improved retrieval across images. We will release our code and benchmark publicly.