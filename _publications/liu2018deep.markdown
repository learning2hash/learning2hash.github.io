---
layout: publication
title: Deep Image Compression Via End-to-end Learning
authors: Haojie Liu, Tong Chen, Qiu Shen, Tao Yue, Zhan Ma
conference: Arxiv
year: 2018
bibkey: liu2018deep
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.01496'}]
tags: ["Datasets", "Quantization", "Robustness"]
short_authors: Liu et al.
---
We present a lossy image compression method based on deep convolutional
neural networks (CNNs), which outperforms the existing BPG, WebP, JPEG2000 and
JPEG as measured via multi-scale structural similarity (MS-SSIM), at the same
bit rate. Currently, most of the CNNs based approaches train the network using
a L2 loss between the reconstructions and the ground-truths in the pixel
domain, which leads to over-smoothing results and visual quality degradation
especially at a very low bit rate. Therefore, we improve the subjective quality
with the combination of a perception loss and an adversarial loss additionally.
To achieve better rate-distortion optimization (RDO), we also introduce an
easy-to-hard transfer learning when adding quantization error and rate
constraint. Finally, we evaluate our method on public Kodak and the Test
Dataset P/M released by the Computer Vision Lab of ETH Zurich, resulting in
averaged 7.81% and 19.1% BD-rate reduction over BPG, respectively.