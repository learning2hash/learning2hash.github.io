---
layout: publication
title: 'Per-vis: Person Retrieval In Video Surveillance Using Semantic Description'
authors: Parshwa Shah, Arpit Garg, Vandit Gajjar
conference: 2021 IEEE Winter Conference on Applications of Computer Vision Workshops
  (WACVW)
year: 2021
bibkey: shah2020per
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.02408'}]
tags: []
short_authors: Parshwa Shah, Arpit Garg, Vandit Gajjar
---
A person is usually characterized by descriptors like age, gender, height,
cloth type, pattern, color, etc. Such descriptors are known as attributes
and/or soft-biometrics. They link the semantic gap between a person's
description and retrieval in video surveillance. Retrieving a specific person
with the query of semantic description has an important application in video
surveillance. Using computer vision to fully automate the person retrieval task
has been gathering interest within the research community. However, the
Current, trend mainly focuses on retrieving persons with image-based queries,
which have major limitations for practical usage. Instead of using an image
query, in this paper, we study the problem of person retrieval in video
surveillance with a semantic description. To solve this problem, we develop a
deep learning-based cascade filtering approach (PeR-ViS), which uses Mask R-CNN
[14] (person detection and instance segmentation) and DenseNet-161 [16]
(soft-biometric classification). On the standard person retrieval dataset of
SoftBioSearch [6], we achieve 0.566 Average IoU and 0.792 %w \\(IoU > 0.4\\),
surpassing the current state-of-the-art by a large margin. We hope our simple,
reproducible, and effective approach will help ease future research in the
domain of person retrieval in video surveillance. The source code and
pretrained weights available at https://parshwa1999.github.io/PeR-ViS/.