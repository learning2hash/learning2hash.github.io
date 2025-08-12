---
layout: publication
title: 'Rf-net: An End-to-end Image Matching Network Based On Receptive Field'
authors: Xuelun Shen, Cheng Wang, Xin Li, Zenglei Yu, Jonathan Li, Chenglu Wen, Ming
  Cheng, Zijian He
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: shen2019rf
citations: 101
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.00604'}]
tags: ["CVPR"]
short_authors: Shen et al.
---
This paper proposes a new end-to-end trainable matching network based on
receptive field, RF-Net, to compute sparse correspondence between images.
Building end-to-end trainable matching framework is desirable and challenging.
The very recent approach, LF-Net, successfully embeds the entire feature
extraction pipeline into a jointly trainable pipeline, and produces the
state-of-the-art matching results. This paper introduces two modifications to
the structure of LF-Net. First, we propose to construct receptive feature maps,
which lead to more effective keypoint detection. Second, we introduce a general
loss function term, neighbor mask, to facilitate training patch selection. This
results in improved stability in descriptor training. We trained RF-Net on the
open dataset HPatches, and compared it with other methods on multiple benchmark
datasets. Experiments show that RF-Net outperforms existing state-of-the-art
methods.