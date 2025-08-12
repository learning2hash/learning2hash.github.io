---
layout: publication
title: Feature Pyramid Encoding Network For Real-time Semantic Segmentation
authors: Mengyu Liu, Hujun Yin
conference: Arxiv
year: 2019
bibkey: liu2019feature
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.08599'}]
tags: ["Efficiency"]
short_authors: Mengyu Liu, Hujun Yin
---
Although current deep learning methods have achieved impressive results for
semantic segmentation, they incur high computational costs and have a huge
number of parameters. For real-time applications, inference speed and memory
usage are two important factors. To address the challenge, we propose a
lightweight feature pyramid encoding network (FPENet) to make a good trade-off
between accuracy and speed. Specifically, we use a feature pyramid encoding
block to encode multi-scale contextual features with depthwise dilated
convolutions in all stages of the encoder. A mutual embedding upsample module
is introduced in the decoder to aggregate the high-level semantic features and
low-level spatial details efficiently. The proposed network outperforms
existing real-time methods with fewer parameters and improved inference speed
on the Cityscapes and CamVid benchmark datasets. Specifically, FPENet achieves
68.0% mean IoU on the Cityscapes test set with only 0.4M parameters and 102
FPS speed on an NVIDIA TITAN V GPU.