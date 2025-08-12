---
layout: publication
title: 'FAPIS: A Few-shot Anchor-free Part-based Instance Segmenter'
authors: Khoi Nguyen, Sinisa Todorovic
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: nguyen2021fapis
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.00073'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Khoi Nguyen, Sinisa Todorovic
---
This paper is about few-shot instance segmentation, where training and test
image sets do not share the same object classes. We specify and evaluate a new
few-shot anchor-free part-based instance segmenter FAPIS. Our key novelty is in
explicit modeling of latent object parts shared across training object classes,
which is expected to facilitate our few-shot learning on new classes in
testing. We specify a new anchor-free object detector aimed at scoring and
regressing locations of foreground bounding boxes, as well as estimating
relative importance of latent parts within each box. Also, we specify a new
network for delineating and weighting latent parts for the final instance
segmentation within every detected bounding box. Our evaluation on the
benchmark COCO-20i dataset demonstrates that we significantly outperform the
state of the art.