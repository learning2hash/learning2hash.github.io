---
layout: publication
title: Wavelet Feature Maps Compression For Image-to-image Cnns
authors: Shahaf E. Finder, Yair Zohav, Maor Ashkenazi, Eran Treister
conference: Arxiv
year: 2022
bibkey: finder2022wavelet
citations: 9
additional_links: [{name: Code, url: 'https://github.com/BGUCompSci/WaveletCompressedConvolution'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.12268'}]
tags: []
short_authors: Finder et al.
---
Convolutional Neural Networks (CNNs) are known for requiring extensive
computational resources, and quantization is among the best and most common
methods for compressing them. While aggressive quantization (i.e., less than
4-bits) performs well for classification, it may cause severe performance
degradation in image-to-image tasks such as semantic segmentation and depth
estimation. In this paper, we propose Wavelet Compressed Convolution (WCC) -- a
novel approach for high-resolution activation maps compression integrated with
point-wise convolutions, which are the main computational cost of modern
architectures. To this end, we use an efficient and hardware-friendly
Haar-wavelet transform, known for its effectiveness in image compression, and
define the convolution on the compressed activation map. We experiment with
various tasks that benefit from high-resolution input. By combining WCC with
light quantization, we achieve compression rates equivalent to 1-4bit
activation quantization with relatively small and much more graceful
degradation in performance. Our code is available at
https://github.com/BGUCompSci/WaveletCompressedConvolution.