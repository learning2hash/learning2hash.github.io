---
layout: publication
title: 'Supergf: Unifying Local And Global Features For Visual Localization'
authors: Wenzheng Song, Ran Yan, Boshu Lei, Takayuki Okatani
conference: Arxiv
year: 2022
bibkey: song2022supergf
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.13105'}]
tags: ["Efficiency", "Image Retrieval"]
short_authors: Song et al.
---
Advanced visual localization techniques encompass image retrieval challenges
and 6 Degree-of-Freedom (DoF) camera pose estimation, such as hierarchical
localization. Thus, they must extract global and local features from input
images. Previous methods have achieved this through resource-intensive or
accuracy-reducing means, such as combinatorial pipelines or multi-task
distillation. In this study, we present a novel method called SuperGF, which
effectively unifies local and global features for visual localization, leading
to a higher trade-off between localization accuracy and computational
efficiency. Specifically, SuperGF is a transformer-based aggregation model that
operates directly on image-matching-specific local features and generates
global features for retrieval. We conduct experimental evaluations of our
method in terms of both accuracy and efficiency, demonstrating its advantages
over other methods. We also provide implementations of SuperGF using various
types of local features, including dense and sparse learning-based or
hand-crafted descriptors.