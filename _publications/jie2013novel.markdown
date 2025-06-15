---
layout: publication
title: 'A Novel Block-dct And PCA Based Image Perceptual Hashing Algorithm'
authors: Zeng Jie
conference: "Arxiv"
year: 2013
citations: 18
bibkey: jie2013novel
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1306.4079'}
tags: ['Hashing Fundamentals', 'Hashing Methods', 'Indexing', 'Applications']
---
Image perceptual hashing finds applications in content indexing, large-scale
image database management, certification and authentication and digital
watermarking. We propose a Block-DCT and PCA based image perceptual hash in
this article and explore the algorithm in the application of tamper detection.
The main idea of the algorithm is to integrate color histogram and DCT
coefficients of image blocks as perceptual feature, then to compress perceptual
features as inter-feature with PCA, and to threshold to create a robust hash.
The robustness and discrimination properties of the proposed algorithm are
evaluated in detail. Our algorithms first construct a secondary image, derived
from input image by pseudo-randomly extracting features that approximately
capture semi-global geometric characteristics. From the secondary image (which
does not perceptually resemble the input), we further extract the final
features which can be used as a hash value (and can be further suitably
quantized). In this paper, we use spectral matrix invariants as embodied by
Singular Value Decomposition. Surprisingly, formation of the secondary image
turns out be quite important since it not only introduces further robustness,
but also enhances the security properties. Indeed, our experiments reveal that
our hashing algorithms extract most of the geometric information from the
images and hence are robust to severe perturbations (e.g. up to %50 cropping by
area with 20 degree rotations) on images while avoiding misclassification.
Experimental results show that the proposed image perceptual hash algorithm can
effectively address the tamper detection problem with advantageous robustness
and discrimination.
