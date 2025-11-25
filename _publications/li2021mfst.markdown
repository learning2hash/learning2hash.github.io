---
layout: publication
title: 'MFST: Multi-features Siamese Tracker'
authors: Zhenxi Li, Guillaume-Alexandre Bilodeau, Wassim Bouachir
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: li2021mfst
citations: 1
additional_links: [{name: Code, url: 'https://github.com/zhenxili96/MFST'}, {name: Paper,
    url: 'https://arxiv.org/abs/2103.00810'}]
tags: ["Similarity Search"]
short_authors: Zhenxi Li, Guillaume-Alexandre Bilodeau, Wassim Bouachir
---
Siamese trackers have recently achieved interesting results due to their
balance between accuracy and speed. This success is mainly due to the fact that
deep similarity networks were specifically designed to address the image
similarity problem. Therefore, they are inherently more appropriate than
classical CNNs for the tracking task. However, Siamese trackers rely on the
last convolutional layers for similarity analysis and target search, which
restricts their performance. In this paper, we argue that using a single
convolutional layer as feature representation is not the optimal choice within
the deep similarity framework, as multiple convolutional layers provide several
abstraction levels in characterizing an object. Starting from this motivation,
we present the Multi-Features Siamese Tracker (MFST), a novel tracking
algorithm exploiting several hierarchical feature maps for robust deep
similarity tracking. MFST proceeds by fusing hierarchical features to ensure a
richer and more efficient representation. Moreover, we handle appearance
variation by calibrating deep features extracted from two different CNN models.
Based on this advanced feature representation, our algorithm achieves high
tracking accuracy, while outperforming several state-of-the-art trackers,
including standard Siamese trackers. The code and trained models are available
at https://github.com/zhenxili96/MFST.