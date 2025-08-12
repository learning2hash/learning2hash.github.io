---
layout: publication
title: Hyper-convolutions Via Implicit Kernels For Medical Imaging
authors: Tianyu Ma, Alan Q. Wang, Adrian V. Dalca, Mert R. Sabuncu
conference: Medical Image Analysis
year: 2023
bibkey: ma2022hyper
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.02701'}]
tags: ["Evaluation", "Robustness"]
short_authors: Ma et al.
---
The convolutional neural network (CNN) is one of the most commonly used
architectures for computer vision tasks. The key building block of a CNN is the
convolutional kernel that aggregates information from the pixel neighborhood
and shares weights across all pixels. A standard CNN's capacity, and thus its
performance, is directly related to the number of learnable kernel weights,
which is determined by the number of channels and the kernel size (support). In
this paper, we present the \textit\{hyper-convolution\}, a novel building block
that implicitly encodes the convolutional kernel using spatial coordinates.
Hyper-convolutions decouple kernel size from the total number of learnable
parameters, enabling a more flexible architecture design. We demonstrate in our
experiments that replacing regular convolutions with hyper-convolutions can
improve performance with less parameters, and increase robustness against
noise. We provide our code here:
*https://github.com/tym002/Hyper-Convolution*