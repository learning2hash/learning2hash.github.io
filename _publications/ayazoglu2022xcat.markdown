---
layout: publication
title: XCAT -- Lightweight Quantized Single Image Super-resolution Using Heterogeneous
  Group Convolutions And Cross Concatenation
authors: Mustafa Ayazoglu, Bahri Batuhan Bilecen
conference: Lecture Notes in Computer Science
year: 2023
bibkey: ayazoglu2022xcat
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.14655'}]
tags: ["Quantization"]
short_authors: Mustafa Ayazoglu, Bahri Batuhan Bilecen
---
We propose a lightweight, single image super-resolution network for mobile
devices, named XCAT. XCAT introduces Heterogeneous Group Convolution Blocks
with Cross Concatenations (HXBlock). The heterogeneous split of the input
channels to the group convolution blocks reduces the number of operations, and
cross concatenation allows for information flow between the intermediate input
tensors of cascaded HXBlocks. Cross concatenations inside HXBlocks can also
avoid using more expensive operations like 1x1 convolutions. To further prev
ent expensive tensor copy operations, XCAT utilizes non-trainable convolution
kernels to apply up sampling operations. Designed with integer quantization in
mind, XCAT also utilizes several techniques on training, like intensity-based
data augmentation. Integer quantized XCAT operates in real time on Mali-G71 MP2
GPU with 320ms, and on Synaptics Dolphin NPU with 30ms (NCHW) and 8.8ms (NHWC),
suitable for real-time applications.