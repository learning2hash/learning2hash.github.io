---
layout: publication
title: Multi-instance Multi-scale CNN For Medical Image Classification
authors: Shaohua Li, Yong Liu, Xiuchao Sui, Cheng Chen, Gabriel Tjio, Daniel Shu Wei
  Ting, Rick Siow Mong Goh
conference: Lecture Notes in Computer Science
year: 2019
bibkey: li2019multi
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.02413'}]
tags: []
short_authors: Li et al.
---
Deep learning for medical image classification faces three major challenges:
1) the number of annotated medical images for training are usually small; 2)
regions of interest (ROIs) are relatively small with unclear boundaries in the
whole medical images, and may appear in arbitrary positions across the x,y (and
also z in 3D images) dimensions. However often only labels of the whole images
are annotated, and localized ROIs are unavailable; and 3) ROIs in medical
images often appear in varying sizes (scales). We approach these three
challenges with a Multi-Instance Multi-Scale (MIMS) CNN: 1) We propose a
multi-scale convolutional layer, which extracts patterns of different receptive
fields with a shared set of convolutional kernels, so that scale-invariant
patterns are captured by this compact set of kernels. As this layer contains
only a small number of parameters, training on small datasets becomes feasible;
2) We propose a "top-k pooling" to aggregate the feature maps in varying scales
from multiple spatial dimensions, allowing the model to be trained using weak
annotations within the multiple instance learning (MIL) framework. Our method
is shown to perform well on three classification tasks involving two 3D and two
2D medical image datasets.