---
layout: publication
title: Fractal Dimension Invariant Filtering And Its Cnn-based Implementation
authors: Hongteng Xu, Junchi Yan, Nils Persson, Weiyao Lin, Hongyuan Zha
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: xu2016fractal
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.06036'}]
tags: ["CVPR"]
short_authors: Xu et al.
---
Fractal analysis has been widely used in computer vision, especially in
texture image processing and texture analysis. The key concept of fractal-based
image model is the fractal dimension, which is invariant to bi-Lipschitz
transformation of image, and thus capable of representing intrinsic structural
information of image robustly. However, the invariance of fractal dimension
generally does not hold after filtering, which limits the application of
fractal-based image model. In this paper, we propose a novel fractal dimension
invariant filtering (FDIF) method, extending the invariance of fractal
dimension to filtering operations. Utilizing the notion of local
self-similarity, we first develop a local fractal model for images. By adding a
nonlinear post-processing step behind anisotropic filter banks, we demonstrate
that the proposed filtering method is capable of preserving the local
invariance of the fractal dimension of image. Meanwhile, we show that the FDIF
method can be re-instantiated approximately via a CNN-based architecture, where
the convolution layer extracts anisotropic structure of image and the nonlinear
layer enhances the structure via preserving local fractal dimension of image.
The proposed filtering method provides us with a novel geometric interpretation
of CNN-based image model. Focusing on a challenging image processing task ---
detecting complicated curves from the texture-like images, the proposed method
obtains superior results to the state-of-art approaches.