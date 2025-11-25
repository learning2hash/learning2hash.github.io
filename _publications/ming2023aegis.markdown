---
layout: publication
title: 'Aegis-net: Attention-guided Multi-level Feature Aggregation For Indoor Place
  Recognition'
authors: Yuhang Ming, Jian Ma, Xingrui Yang, Weichen Dai, Yong Peng, Wanzeng Kong
conference: Arxiv
year: 2023
bibkey: ming2023aegis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.09538'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ming et al.
---
We present AEGIS-Net, a novel indoor place recognition model that takes in
RGB point clouds and generates global place descriptors by aggregating
lower-level color, geometry features and higher-level implicit semantic
features. However, rather than simple feature concatenation, self-attention
modules are employed to select the most important local features that best
describe an indoor place. Our AEGIS-Net is made of a semantic encoder, a
semantic decoder and an attention-guided feature embedding. The model is
trained in a 2-stage process with the first stage focusing on an auxiliary
semantic segmentation task and the second one on the place recognition task. We
evaluate our AEGIS-Net on the ScanNetPR dataset and compare its performance
with a pre-deep-learning feature-based method and five state-of-the-art
deep-learning-based methods. Our AEGIS-Net achieves exceptional performance and
outperforms all six methods.