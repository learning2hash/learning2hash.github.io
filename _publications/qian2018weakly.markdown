---
layout: publication
title: Weakly Supervised Scene Parsing With Point-based Distance Metric Learning
authors: Rui Qian, Yunchao Wei, Honghui Shi, Jiachen Li, Jiaying Liu, Thomas Huang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2019
bibkey: qian2018weakly
citations: 72
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.02233'}]
tags: ["AAAI", "Distance Metric Learning"]
short_authors: Qian et al.
---
Semantic scene parsing is suffering from the fact that pixel-level
annotations are hard to be collected. To tackle this issue, we propose a
Point-based Distance Metric Learning (PDML) in this paper. PDML does not
require dense annotated masks and only leverages several labeled points that
are much easier to obtain to guide the training process. Concretely, we
leverage semantic relationship among the annotated points by encouraging the
feature representations of the intra- and inter-category points to keep
consistent, i.e. points within the same category should have more similar
feature representations compared to those from different categories. We
formulate such a characteristic into a simple distance metric loss, which
collaborates with the point-wise cross-entropy loss to optimize the deep neural
networks. Furthermore, to fully exploit the limited annotations, distance
metric learning is conducted across different training images instead of simply
adopting an image-dependent manner. We conduct extensive experiments on two
challenging scene parsing benchmarks of PASCAL-Context and ADE 20K to validate
the effectiveness of our PDML, and competitive mIoU scores are achieved.