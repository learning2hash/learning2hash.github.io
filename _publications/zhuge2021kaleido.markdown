---
layout: publication
title: 'Kaleido-bert: Vision-language Pre-training On Fashion Domain'
authors: Mingchen Zhuge, Dehong Gao, Deng-Ping Fan, Linbo Jin, Ben Chen, Haoming Zhou,
  Minghui Qiu, Ling Shao
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: zhuge2021kaleido
citations: 105
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.16110'}]
tags: ["CVPR", "Image Retrieval", "Self-Supervised", "Text Retrieval"]
short_authors: Zhuge et al.
---
We present a new vision-language (VL) pre-training model dubbed Kaleido-BERT,
which introduces a novel kaleido strategy for fashion cross-modality
representations from transformers. In contrast to random masking strategy of
recent VL models, we design alignment guided masking to jointly focus more on
image-text semantic relations. To this end, we carry out five novel tasks,
i.e., rotation, jigsaw, camouflage, grey-to-color, and blank-to-color for
self-supervised VL pre-training at patches of different scale. Kaleido-BERT is
conceptually simple and easy to extend to the existing BERT framework, it
attains new state-of-the-art results by large margins on four downstream tasks,
including text retrieval (R@1: 4.03% absolute improvement), image retrieval
(R@1: 7.13% abs imv.), category recognition (ACC: 3.28% abs imv.), and fashion
captioning (Bleu4: 1.2 abs imv.). We validate the efficiency of Kaleido-BERT on
a wide range of e-commerical websites, demonstrating its broader potential in
real-world applications.