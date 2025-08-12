---
layout: publication
title: Deep Self-convolutional Activations Descriptor For Dense Cross-modal Correspondence
authors: Seungryong Kim, Dongbo Min, Stephen Lin, Kwanghoon Sohn
conference: Arxiv
year: 2016
bibkey: kim2016deep
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.06327'}]
tags: ["Robustness"]
short_authors: Kim et al.
---
We present a novel descriptor, called deep self-convolutional activations
(DeSCA), designed for establishing dense correspondences between images taken
under different imaging modalities, such as different spectral ranges or
lighting conditions. Motivated by descriptors based on local self-similarity
(LSS), we formulate a novel descriptor by leveraging LSS in a deep
architecture, leading to better discriminative power and greater robustness to
non-rigid image deformations than state-of-the-art cross-modality descriptors.
The DeSCA first computes self-convolutions over a local support window for
randomly sampled patches, and then builds self-convolution activations by
performing an average pooling through a hierarchical formulation within a deep
convolutional architecture. Finally, the feature responses on the
self-convolution activations are encoded through a spatial pyramid pooling in a
circular configuration. In contrast to existing convolutional neural networks
(CNNs) based descriptors, the DeSCA is training-free (i.e., randomly sampled
patches are utilized as the convolution kernels), is robust to cross-modal
imaging, and can be densely computed in an efficient manner that significantly
reduces computational redundancy. The state-of-the-art performance of DeSCA on
challenging cases of cross-modal image pairs is demonstrated through extensive
experiments.