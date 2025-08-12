---
layout: publication
title: 'Repmlpnet: Hierarchical Vision MLP With Re-parameterized Locality'
authors: Xiaohan Ding, Honghao Chen, Xiangyu Zhang, Jungong Han, Guiguang Ding
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: ding2021repmlpnet
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.11081'}]
tags: ["CVPR"]
short_authors: Ding et al.
---
Compared to convolutional layers, fully-connected (FC) layers are better at
modeling the long-range dependencies but worse at capturing the local patterns,
hence usually less favored for image recognition. In this paper, we propose a
methodology, Locality Injection, to incorporate local priors into an FC layer
via merging the trained parameters of a parallel conv kernel into the FC
kernel. Locality Injection can be viewed as a novel Structural
Re-parameterization method since it equivalently converts the structures via
transforming the parameters. Based on that, we propose a multi-layer-perceptron
(MLP) block named RepMLP Block, which uses three FC layers to extract features,
and a novel architecture named RepMLPNet. The hierarchical design distinguishes
RepMLPNet from the other concurrently proposed vision MLPs. As it produces
feature maps of different levels, it qualifies as a backbone model for
downstream tasks like semantic segmentation. Our results reveal that 1)
Locality Injection is a general methodology for MLP models; 2) RepMLPNet has
favorable accuracy-efficiency trade-off compared to the other MLPs; 3)
RepMLPNet is the first MLP that seamlessly transfer to Cityscapes semantic
segmentation. The code and models are available at
https://github.com/DingXiaoH/RepMLP.