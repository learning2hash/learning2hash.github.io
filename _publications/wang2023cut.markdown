---
layout: publication
title: Cut And Learn For Unsupervised Object Detection And Instance Segmentation
authors: Xudong Wang, Rohit Girdhar, Stella X. Yu, Ishan Misra
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: wang2023cut
citations: 104
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.11320'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Wang et al.
---
We propose Cut-and-LEaRn (CutLER), a simple approach for training
unsupervised object detection and segmentation models. We leverage the property
of self-supervised models to 'discover' objects without supervision and amplify
it to train a state-of-the-art localization model without any human labels.
CutLER first uses our proposed MaskCut approach to generate coarse masks for
multiple objects in an image and then learns a detector on these masks using
our robust loss function. We further improve the performance by self-training
the model on its predictions. Compared to prior work, CutLER is simpler,
compatible with different detection architectures, and detects multiple
objects. CutLER is also a zero-shot unsupervised detector and improves
detection performance AP50 by over 2.7 times on 11 benchmarks across domains
like video frames, paintings, sketches, etc. With finetuning, CutLER serves as
a low-shot detector surpassing MoCo-v2 by 7.3% APbox and 6.6% APmask on COCO
when training with 5% labels.