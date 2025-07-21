---
layout: publication
title: Segmentation of Objects by Hashing
authors: "Curt\xF3 et al."
conference: IEEE Transactions on Multimedia
year: 2018
bibkey: "curt\xF32017segmentation"
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.08160'}]
tags: ["Hashing-Methods"]
---
We propose a novel approach to address the problem of Simultaneous Detection
and Segmentation introduced in [Hariharan et al 2014]. Using the hierarchical
structures first presented in [Arbel\'aez et al 2011] we use an efficient and
accurate procedure that exploits the feature information of the hierarchy using
Locality Sensitive Hashing. We build on recent work that utilizes convolutional
neural networks to detect bounding boxes in an image [Ren et al 2015] and then
use the top similar hierarchical region that best fits each bounding box after
hashing, we call this approach C&Z Segmentation. We then refine our final
segmentation results by automatic hierarchical pruning. C&Z Segmentation
introduces a train-free alternative to Hypercolumns [Hariharan et al 2015]. We
conduct extensive experiments on PASCAL VOC 2012 segmentation dataset, showing
that C&Z gives competitive state-of-the-art segmentations of objects.