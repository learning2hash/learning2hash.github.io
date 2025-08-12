---
layout: publication
title: Hierarchical Representation Based Query-specific Prototypical Network For Few-shot
  Image Classification
authors: Yaohui Li, Huaxiong Li, Haoxing Chen, Chunlin Chen
conference: Arxiv
year: 2021
bibkey: li2021hierarchical
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.11384'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Li et al.
---
Few-shot image classification aims at recognizing unseen categories with a
small number of labeled training data. Recent metric-based frameworks tend to
represent a support class by a fixed prototype (e.g., the mean of the support
category) and make classification according to the similarities between query
instances and support prototypes. However, discriminative dominant regions may
locate uncertain areas of images and have various scales, which leads to the
misaligned metric. Besides, a fixed prototype for one support category cannot
fit for all query instances to accurately reflect their distances with this
category, which lowers the efficiency of metric. Therefore, query-specific
dominant regions in support samples should be extracted for a high-quality
metric. To address these problems, we propose a Hierarchical Representation
based Query-Specific Prototypical Network (QPN) to tackle the limitations by
generating a region-level prototype for each query sample, which achieves both
positional and dimensional semantic alignment simultaneously. Extensive
experiments conducted on five benchmark datasets (including three fine-grained
datasets) show that our proposed method outperforms the current
state-of-the-art methods.