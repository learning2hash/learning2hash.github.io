---
layout: publication
title: Correlation Verification for Image Retrieval
authors: Lee et al.
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: lee2022correlation
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.01458'}]
tags: ["CVPR", "Image-Retrieval"]
---
Geometric verification is considered a de facto solution for the re-ranking
task in image retrieval. In this study, we propose a novel image retrieval
re-ranking network named Correlation Verification Networks (CVNet). Our
proposed network, comprising deeply stacked 4D convolutional layers, gradually
compresses dense feature correlation into image similarity while learning
diverse geometric matching patterns from various image pairs. To enable
cross-scale matching, it builds feature pyramids and constructs cross-scale
feature correlations within a single inference, replacing costly multi-scale
inferences. In addition, we use curriculum learning with the hard negative
mining and Hide-and-Seek strategy to handle hard samples without losing
generality. Our proposed re-ranking network shows state-of-the-art performance
on several retrieval benchmarks with a significant margin (+12.6% in mAP on
ROxford-Hard+1M set) over state-of-the-art methods. The source code and models
are available online: https://github.com/sungonce/CVNet.