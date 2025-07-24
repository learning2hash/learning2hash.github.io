---
layout: publication
title: 'Arnet: Self-supervised FG-SBIR With Unified Sample Feature Alignment And Multi-scale
  Token Recycling'
authors: Jianan Jiang, Hao Tang, Zhilin Jiang, Weiren Yu, di Wu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: jiang2024arnet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.11551'}]
tags: ["AAAI", "Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval", "Scalability", "Self-Supervised", "Supervised"]
short_authors: Jiang et al.
---
Fine-Grained Sketch-Based Image Retrieval (FG-SBIR) aims to minimize the
distance between sketches and corresponding images in the embedding space.
However, scalability is hindered by the growing complexity of solutions, mainly
due to the abstract nature of fine-grained sketches. In this paper, we propose
an effective approach to narrow the gap between the two domains. It mainly
facilitates unified mutual information sharing both intra- and inter-samples,
rather than treating them as a single feature alignment problem between
modalities. Specifically, our approach includes: (i) Employing dual
weight-sharing networks to optimize alignment within the sketch and image
domain, which also effectively mitigates model learning saturation issues. (ii)
Introducing an objective optimization function based on contrastive loss to
enhance the model's ability to align features in both intra- and inter-samples.
(iii) Presenting a self-supervised Multi-Scale Token Recycling (MSTR) Module
featured by recycling discarded patch tokens in multi-scale features, further
enhancing representation capability and retrieval performance. Our framework
achieves excellent results on CNN- and ViT-based backbones. Extensive
experiments demonstrate its superiority over existing methods. We also
introduce Cloths-V1, the first professional fashion sketch-image dataset,
utilized to validate our method and will be beneficial for other applications.