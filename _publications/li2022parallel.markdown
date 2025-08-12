---
layout: publication
title: Parallel Pre-trained Transformers (PPT) For Synthetic Data-based Instance Segmentation
authors: Ming Li, Jie Wu, Jinhang Cai, Jie Qin, Yuxi Ren, Xuefeng Xiao, Min Zheng,
  Rui Wang, Xin Pan
conference: Arxiv
year: 2022
bibkey: li2022parallel
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.10845'}]
tags: []
short_authors: Li et al.
---
Recently, Synthetic data-based Instance Segmentation has become an
exceedingly favorable optimization paradigm since it leverages simulation
rendering and physics to generate high-quality image-annotation pairs. In this
paper, we propose a Parallel Pre-trained Transformers (PPT) framework to
accomplish the synthetic data-based Instance Segmentation task. Specifically,
we leverage the off-the-shelf pre-trained vision Transformers to alleviate the
gap between natural and synthetic data, which helps to provide good
generalization in the downstream synthetic data scene with few samples.
Swin-B-based CBNet V2, SwinL-based CBNet V2 and Swin-L-based Uniformer are
employed for parallel feature learning, and the results of these three models
are fused by pixel-level Non-maximum Suppression (NMS) algorithm to obtain more
robust results. The experimental results reveal that PPT ranks first in the
CVPR2022 AVA Accessibility Vision and Autonomy Challenge, with a 65.155% mAP.