---
layout: publication
title: Grounding Descriptions In Images Informs Zero-shot Visual Recognition
authors: Shaunak Halbe, Junjiao Tian, K J Joseph, James Seale Smith, Katherine Stevo,
  Vineeth N Balasubramanian, Zsolt Kira
conference: Arxiv
year: 2024
bibkey: halbe2024grounding
citations: 0
additional_links: [{name: Code, url: 'https://github.com/shaunak27/grain-clip'}, {
    name: Paper, url: 'https://arxiv.org/abs/2412.04429'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Halbe et al.
---
Vision-language models (VLMs) like CLIP have been cherished for their ability
to perform zero-shot visual recognition on open-vocabulary concepts. This is
achieved by selecting the object category whose textual representation bears
the highest similarity with the query image. While successful in some domains,
this method struggles with identifying fine-grained entities as well as
generalizing to unseen concepts that are not captured by the training
distribution. Recent works attempt to mitigate these challenges by integrating
category descriptions at test time, albeit yielding modest improvements. We
attribute these limited gains to a fundamental misalignment between image and
description representations, which is rooted in the pretraining structure of
CLIP. In this paper, we propose GRAIN, a new pretraining strategy aimed at
aligning representations at both fine and coarse levels simultaneously. Our
approach learns to jointly ground textual descriptions in image regions along
with aligning overarching captions with global image representations. To drive
this pre-training, we leverage frozen Multimodal Large Language Models (MLLMs)
to derive large-scale synthetic annotations. We demonstrate the enhanced
zero-shot performance of our model compared to current state-of-the art methods
across 11 diverse image classification datasets. Additionally, we introduce
Products-2023, a newly curated, manually labeled dataset featuring novel
concepts, and showcase our model's ability to recognize these concepts by
benchmarking on it. Significant improvements achieved by our model on other
downstream tasks like retrieval further highlight the superior quality of
representations learned by our approach. Code available at
https://github.com/shaunak27/grain-clip .