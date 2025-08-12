---
layout: publication
title: Correspondence Networks With Adaptive Neighbourhood Consensus
authors: Shuda Li, Kai Han, Theo W. Costain, Henry Howard-Jenkins, Victor Prisacariu
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: li2020correspondence
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.12059'}]
tags: ["CVPR"]
short_authors: Li et al.
---
In this paper, we tackle the task of establishing dense visual
correspondences between images containing objects of the same category. This is
a challenging task due to large intra-class variations and a lack of dense
pixel level annotations. We propose a convolutional neural network
architecture, called adaptive neighbourhood consensus network (ANC-Net), that
can be trained end-to-end with sparse key-point annotations, to handle this
challenge. At the core of ANC-Net is our proposed non-isotropic 4D convolution
kernel, which forms the building block for the adaptive neighbourhood consensus
module for robust matching. We also introduce a simple and efficient
multi-scale self-similarity module in ANC-Net to make the learned feature
robust to intra-class variations. Furthermore, we propose a novel orthogonal
loss that can enforce the one-to-one matching constraint. We thoroughly
evaluate the effectiveness of our method on various benchmarks, where it
substantially outperforms state-of-the-art methods.