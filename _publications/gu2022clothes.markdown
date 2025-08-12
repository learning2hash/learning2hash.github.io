---
layout: publication
title: Clothes-changing Person Re-identification With RGB Modality Only
authors: Xinqian Gu, Hong Chang, Bingpeng Ma, Shutao Bai, Shiguang Shan, Xilin Chen
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: gu2022clothes
citations: 124
additional_links: [{name: Code, url: 'https://github.com/guxinqian/Simple-CCReID'},
  {name: Paper, url: 'https://arxiv.org/abs/2204.06890'}]
tags: ["CVPR"]
short_authors: Gu et al.
---
The key to address clothes-changing person re-identification (re-id) is to
extract clothes-irrelevant features, e.g., face, hairstyle, body shape, and
gait. Most current works mainly focus on modeling body shape from
multi-modality information (e.g., silhouettes and sketches), but do not make
full use of the clothes-irrelevant information in the original RGB images. In
this paper, we propose a Clothes-based Adversarial Loss (CAL) to mine
clothes-irrelevant features from the original RGB images by penalizing the
predictive power of re-id model w.r.t. clothes. Extensive experiments
demonstrate that using RGB images only, CAL outperforms all state-of-the-art
methods on widely-used clothes-changing person re-id benchmarks. Besides,
compared with images, videos contain richer appearance and additional temporal
information, which can be used to model proper spatiotemporal patterns to
assist clothes-changing re-id. Since there is no publicly available
clothes-changing video re-id dataset, we contribute a new dataset named CCVID
and show that there exists much room for improvement in modeling spatiotemporal
information. The code and new dataset are available at:
https://github.com/guxinqian/Simple-CCReID.