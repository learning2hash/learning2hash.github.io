---
layout: publication
title: 'SDC - Stacked Dilated Convolution: A Unified Descriptor Network For Dense
  Matching Tasks'
authors: "Ren\xE9 Schuster, Oliver Wasenm\xFCller, Christian Unger, Didier Stricker"
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: schuster2019sdc
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.03076'}]
tags: ["CVPR"]
short_authors: Schuster et al.
---
Dense pixel matching is important for many computer vision tasks such as
disparity and flow estimation. We present a robust, unified descriptor network
that considers a large context region with high spatial variance. Our network
has a very large receptive field and avoids striding layers to maintain spatial
resolution. These properties are achieved by creating a novel neural network
layer that consists of multiple, parallel, stacked dilated convolutions (SDC).
Several of these layers are combined to form our SDC descriptor network. In our
experiments, we show that our SDC features outperform state-of-the-art feature
descriptors in terms of accuracy and robustness. In addition, we demonstrate
the superior performance of SDC in state-of-the-art stereo matching, optical
flow and scene flow algorithms on several famous public benchmarks.