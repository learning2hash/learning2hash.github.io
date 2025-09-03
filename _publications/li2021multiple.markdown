---
layout: publication
title: Multiple Convolutional Features In Siamese Networks For Object Tracking
authors: Zhenxi Li, Guillaume-Alexandre Bilodeau, Wassim Bouachir
conference: Machine Vision and Applications
year: 2021
bibkey: li2021multiple
citations: 6
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2103.01222'}]
tags: ["Evaluation", "Tools & Libraries"]
short_authors: Zhenxi Li, Guillaume-Alexandre Bilodeau, Wassim Bouachir
---
Siamese trackers demonstrated high performance in object tracking due to
their balance between accuracy and speed. Unlike classification-based CNNs,
deep similarity networks are specifically designed to address the image
similarity problem, and thus are inherently more appropriate for the tracking
task. However, Siamese trackers mainly use the last convolutional layers for
similarity analysis and target search, which restricts their performance. In
this paper, we argue that using a single convolutional layer as feature
representation is not an optimal choice in a deep similarity framework. We
present a Multiple Features-Siamese Tracker (MFST), a novel tracking algorithm
exploiting several hierarchical feature maps for robust tracking. Since
convolutional layers provide several abstraction levels in characterizing an
object, fusing hierarchical features allows to obtain a richer and more
efficient representation of the target. Moreover, we handle the target
appearance variations by calibrating the deep features extracted from two
different CNN models. Based on this advanced feature representation, our method
achieves high tracking accuracy, while outperforming the standard siamese
tracker on object tracking benchmarks. The source code and trained models are
available at https://github.com/zhenxili96/MFST.