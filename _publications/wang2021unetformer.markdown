---
layout: publication
title: 'Unetformer: A Unet-like Transformer For Efficient Semantic Segmentation Of
  Remote Sensing Urban Scene Imagery'
authors: Libo Wang, Rui Li, Ce Zhang, Shenghui Fang, Chenxi Duan, Xiaoliang Meng,
  Peter M. Atkinson
conference: ISPRS Journal of Photogrammetry and Remote Sensing
year: 2022
bibkey: wang2021unetformer
citations: 585
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.08937'}]
tags: ["Efficiency"]
short_authors: Wang et al.
---
Semantic segmentation of remotely sensed urban scene images is required in a
wide range of practical applications, such as land cover mapping, urban change
detection, environmental protection, and economic assessment.Driven by rapid
developments in deep learning technologies, the convolutional neural network
(CNN) has dominated semantic segmentation for many years. CNN adopts
hierarchical feature representation, demonstrating strong capabilities for
local information extraction. However, the local property of the convolution
layer limits the network from capturing the global context. Recently, as a hot
topic in the domain of computer vision, Transformer has demonstrated its great
potential in global information modelling, boosting many vision-related tasks
such as image classification, object detection, and particularly semantic
segmentation. In this paper, we propose a Transformer-based decoder and
construct a UNet-like Transformer (UNetFormer) for real-time urban scene
segmentation. For efficient segmentation, the UNetFormer selects the
lightweight ResNet18 as the encoder and develops an efficient global-local
attention mechanism to model both global and local information in the decoder.
Extensive experiments reveal that our method not only runs faster but also
produces higher accuracy compared with state-of-the-art lightweight models.
Specifically, the proposed UNetFormer achieved 67.8% and 52.4% mIoU on the
UAVid and LoveDA datasets, respectively, while the inference speed can achieve
up to 322.4 FPS with a 512x512 input on a single NVIDIA GTX 3090 GPU. In
further exploration, the proposed Transformer-based decoder combined with a
Swin Transformer encoder also achieves the state-of-the-art result (91.3% F1
and 84.1% mIoU) on the Vaihingen dataset. The source code will be freely
available at https://github.com/WangLibo1995/GeoSeg.