---
layout: publication
title: 'Spcolor: Semantic Prior Guided Exemplar-based Image Colorization'
authors: Siqi Chen, Xueming Li, Xianlin Zhang, Mingdao Wang, Yu Zhang, Yue Zhang
conference: Arxiv
year: 2023
bibkey: chen2023spcolor
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.06255'}]
tags: []
short_authors: Chen et al.
---
Exemplar-based image colorization aims to colorize a target grayscale image
based on a color reference image, and the key is to establish accurate
pixel-level semantic correspondence between these two images. Previous methods
search for correspondence across the entire reference image, and this type of
global matching is easy to get mismatch. We summarize the difficulties in two
aspects: (1) When the reference image only contains a part of objects related
to target image, improper correspondence will be established in unrelated
regions. (2) It is prone to get mismatch in regions where the shape or texture
of the object is easily confused. To overcome these issues, we propose SPColor,
a semantic prior guided exemplar-based image colorization framework. Different
from previous methods, SPColor first coarsely classifies pixels of the
reference and target images to several pseudo-classes under the guidance of
semantic prior, then the correspondences are only established locally between
the pixels in the same class via the newly designed semantic prior guided
correspondence network. In this way, improper correspondence between different
semantic classes is explicitly excluded, and the mismatch is obviously
alleviated. Besides, to better reserve the color from reference, a similarity
masked perceptual loss is designed. Noting that the carefully designed SPColor
utilizes the semantic prior provided by an unsupervised segmentation model,
which is free for additional manual semantic annotations. Experiments
demonstrate that our model outperforms recent state-of-the-art methods both
quantitatively and qualitatively on public dataset.