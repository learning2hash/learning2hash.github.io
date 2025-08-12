---
layout: publication
title: 'Nerd++: Improved 3d-mirror Symmetry Learning From A Single Image'
authors: Yancong Lin, Silvia-Laura Pintea, Jan van Gemert
conference: Arxiv
year: 2021
bibkey: lin2021nerd
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.12579'}]
tags: ["Efficiency"]
short_authors: Yancong Lin, Silvia-Laura Pintea, Jan van Gemert
---
Many objects are naturally symmetric, and this symmetry can be exploited to
infer unseen 3D properties from a single 2D image. Recently, NeRD is proposed
for accurate 3D mirror plane estimation from a single image. Despite the
unprecedented accuracy, it relies on large annotated datasets for training and
suffers from slow inference. Here we aim to improve its data and compute
efficiency. We do away with the computationally expensive 4D feature volumes
and instead explicitly compute the feature correlation of the pixel
correspondences across depth, thus creating a compact 3D volume. We also design
multi-stage spherical convolutions to identify the optimal mirror plane on the
hemisphere, whose inductive bias offers gains in data-efficiency. Experiments
on both synthetic and real-world datasets show the benefit of our proposed
changes for improved data efficiency and inference speed.