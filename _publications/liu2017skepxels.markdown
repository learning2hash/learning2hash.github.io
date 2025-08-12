---
layout: publication
title: 'Skepxels: Spatio-temporal Image Representation Of Human Skeleton Joints For
  Action Recognition'
authors: Jian Liu, Naveed Akhtar, Ajmal Mian
conference: Arxiv
year: 2017
bibkey: liu2017skepxels
citations: 69
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.05941'}]
tags: []
short_authors: Jian Liu, Naveed Akhtar, Ajmal Mian
---
Human skeleton joints are popular for action analysis since they can be
easily extracted from videos to discard background noises. However, current
skeleton representations do not fully benefit from machine learning with CNNs.
We propose "Skepxels" a spatio-temporal representation for skeleton sequences
to fully exploit the "local" correlations between joints using the 2D
convolution kernels of CNN. We transform skeleton videos into images of
flexible dimensions using Skepxels and develop a CNN-based framework for
effective human action recognition using the resulting images. Skepxels encode
rich spatio-temporal information about the skeleton joints in the frames by
maximizing a unique distance metric, defined collaboratively over the distinct
joint arrangements used in the skeletal image. Moreover, they are flexible in
encoding compound semantic notions such as location and speed of the joints.
The proposed action recognition exploits the representation in a hierarchical
manner by first capturing the micro-temporal relations between the skeleton
joints with the Skepxels and then exploiting their macro-temporal relations by
computing the Fourier Temporal Pyramids over the CNN features of the skeletal
images. We extend the Inception-ResNet CNN architecture with the proposed
method and improve the state-of-the-art accuracy by 4.4% on the large scale NTU
human activity dataset. On the medium-sized N-UCLA and UTH-MHAD datasets, our
method outperforms the existing results by 5.7% and 9.3% respectively.