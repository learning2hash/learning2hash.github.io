---
layout: publication
title: No Annotations For Object Detection In Art Through Stable Diffusion
authors: Patrick Ramos, Nicolas Gonthier, Selina Khan, Yuta Nakashima, Noa Garcia
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2025
bibkey: ramos2024no
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.06286'}]
tags: []
short_authors: Ramos et al.
---
Object detection in art is a valuable tool for the digital humanities, as it
allows for faster identification of objects in artistic and historical images
compared to humans. However, annotating such images poses significant
challenges due to the need for specialized domain expertise. We present NADA
(no annotations for detection in art), a pipeline that leverages diffusion
models' art-related knowledge for object detection in paintings without the
need for full bounding box supervision. Our method, which supports both
weakly-supervised and zero-shot scenarios and does not require any fine-tuning
of its pretrained components, consists of a class proposer based on large
vision-language models and a class-conditioned detector based on Stable
Diffusion. NADA is evaluated on two artwork datasets, ArtDL 2.0 and IconArt,
outperforming prior work in weakly-supervised detection, while being the first
work for zero-shot object detection in art. Code is available at
https://github.com/patrick-john-ramos/nada