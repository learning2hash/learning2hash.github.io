---
layout: publication
title: 'Aerial Scene Parsing: From Tile-level Scene Classification To Pixel-wise Semantic
  Labeling'
authors: Yang Long, Gui-Song Xia, Liangpei Zhang, Gong Cheng, Deren Li
conference: Arxiv
year: 2022
bibkey: long2022aerial
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.01953'}]
tags: ["Datasets", "Evaluation"]
short_authors: Long et al.
---
Given an aerial image, aerial scene parsing (ASP) targets to interpret the
semantic structure of the image content, e.g., by assigning a semantic label to
every pixel of the image. With the popularization of data-driven methods, the
past decades have witnessed promising progress on ASP by approaching the
problem with the schemes of tile-level scene classification or
segmentation-based image analysis, when using high-resolution aerial images.
However, the former scheme often produces results with tile-wise boundaries,
while the latter one needs to handle the complex modeling process from pixels
to semantics, which often requires large-scale and well-annotated image samples
with pixel-wise semantic labels. In this paper, we address these issues in ASP,
with perspectives from tile-level scene classification to pixel-wise semantic
labeling. Specifically, we first revisit aerial image interpretation by a
literature review. We then present a large-scale scene classification dataset
that contains one million aerial images termed Million-AID. With the presented
dataset, we also report benchmarking experiments using classical convolutional
neural networks (CNNs). Finally, we perform ASP by unifying the tile-level
scene classification and object-based image analysis to achieve pixel-wise
semantic labeling. Intensive experiments show that Million-AID is a challenging
yet useful dataset, which can serve as a benchmark for evaluating newly
developed algorithms. When transferring knowledge from Million-AID, fine-tuning
CNN models pretrained on Million-AID perform consistently better than those
pretrained ImageNet for aerial scene classification. Moreover, our designed
hierarchical multi-task learning method achieves the state-of-the-art
pixel-wise classification on the challenging GID, bridging the tile-level scene
classification toward pixel-wise semantic labeling for aerial image
interpretation.