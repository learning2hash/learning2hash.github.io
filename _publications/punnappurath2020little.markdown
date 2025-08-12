---
layout: publication
title: 'A Little Bit More: Bitplane-wise Bit-depth Recovery'
authors: Abhijith Punnappurath, Michael S. Brown
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2021
bibkey: punnappurath2020little
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.01091'}]
tags: ["Quantization"]
short_authors: Abhijith Punnappurath, Michael S. Brown
---
Imaging sensors digitize incoming scene light at a dynamic range of 10--12
bits (i.e., 1024--4096 tonal values). The sensor image is then processed
onboard the camera and finally quantized to only 8 bits (i.e., 256 tonal
values) to conform to prevailing encoding standards. There are a number of
important applications, such as high-bit-depth displays and photo editing,
where it is beneficial to recover the lost bit depth. Deep neural networks are
effective at this bit-depth reconstruction task. Given the quantized
low-bit-depth image as input, existing deep learning methods employ a
single-shot approach that attempts to either (1) directly estimate the
high-bit-depth image, or (2) directly estimate the residual between the high-
and low-bit-depth images. In contrast, we propose a training and inference
strategy that recovers the residual image bitplane-by-bitplane. Our
bitplane-wise learning framework has the advantage of allowing for multiple
levels of supervision during training and is able to obtain state-of-the-art
results using a simple network architecture. We test our proposed method
extensively on several image datasets and demonstrate an improvement from 0.5dB
to 2.3dB PSNR over prior methods depending on the quantization level.