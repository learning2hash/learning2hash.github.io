---
layout: publication
title: 'Snapmix: Semantically Proportional Mixing For Augmenting Fine-grained Data'
authors: Shaoli Huang, Xinchao Wang, Dacheng Tao
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: huang2020snapmix
citations: 94
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.04846'}]
tags: ["AAAI", "Datasets"]
short_authors: Shaoli Huang, Xinchao Wang, Dacheng Tao
---
Data mixing augmentation has proved effective in training deep models. Recent
methods mix labels mainly based on the mixture proportion of image pixels. As
the main discriminative information of a fine-grained image usually resides in
subtle regions, methods along this line are prone to heavy label noise in
fine-grained recognition. We propose in this paper a novel scheme, termed as
Semantically Proportional Mixing (SnapMix), which exploits class activation map
(CAM) to lessen the label noise in augmenting fine-grained data. SnapMix
generates the target label for a mixed image by estimating its intrinsic
semantic composition, and allows for asymmetric mixing operations and ensures
semantic correspondence between synthetic images and target labels. Experiments
show that our method consistently outperforms existing mixed-based approaches
on various datasets and under different network depths. Furthermore, by
incorporating the mid-level features, the proposed SnapMix achieves top-level
performance, demonstrating its potential to serve as a solid baseline for
fine-grained recognition. Our code is available at
https://github.com/Shaoli-Huang/SnapMix.git.