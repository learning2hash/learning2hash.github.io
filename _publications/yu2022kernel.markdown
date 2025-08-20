---
layout: publication
title: Kernel Quantization For Efficient Network Compression
authors: Zhongzhi Yu, Yemin Shi, Tiejun Huang, Yizhou Yu
conference: IEEE Access
year: 2022
bibkey: yu2022kernel
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.05148'}]
tags: [Quantization, Tools & Libraries, Evaluation]
short_authors: Yu et al.
---
This paper presents a novel network compression framework Kernel Quantization
(KQ), targeting to efficiently convert any pre-trained full-precision
convolutional neural network (CNN) model into a low-precision version without
significant performance loss. Unlike existing methods struggling with weight
bit-length, KQ has the potential in improving the compression ratio by
considering the convolution kernel as the quantization unit. Inspired by the
evolution from weight pruning to filter pruning, we propose to quantize in both
kernel and weight level. Instead of representing each weight parameter with a
low-bit index, we learn a kernel codebook and replace all kernels in the
convolution layer with corresponding low-bit indexes. Thus, KQ can represent
the weight tensor in the convolution layer with low-bit indexes and a kernel
codebook with limited size, which enables KQ to achieve significant compression
ratio. Then, we conduct a 6-bit parameter quantization on the kernel codebook
to further reduce redundancy. Extensive experiments on the ImageNet
classification task prove that KQ needs 1.05 and 1.62 bits on average in VGG
and ResNet18, respectively, to represent each parameter in the convolution
layer and achieves the state-of-the-art compression ratio with little accuracy
loss.