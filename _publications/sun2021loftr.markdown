---
layout: publication
title: 'Loftr: Detector-free Local Feature Matching With Transformers'
authors: Jiaming Sun, Zehong Shen, Yuang Wang, Hujun Bao, Xiaowei Zhou
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: sun2021loftr
citations: 937
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.00680'}]
tags: ["CVPR"]
short_authors: Sun et al.
---
We present a novel method for local image feature matching. Instead of
performing image feature detection, description, and matching sequentially, we
propose to first establish pixel-wise dense matches at a coarse level and later
refine the good matches at a fine level. In contrast to dense methods that use
a cost volume to search correspondences, we use self and cross attention layers
in Transformer to obtain feature descriptors that are conditioned on both
images. The global receptive field provided by Transformer enables our method
to produce dense matches in low-texture areas, where feature detectors usually
struggle to produce repeatable interest points. The experiments on indoor and
outdoor datasets show that LoFTR outperforms state-of-the-art methods by a
large margin. LoFTR also ranks first on two public benchmarks of visual
localization among the published methods.