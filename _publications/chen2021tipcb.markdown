---
layout: publication
title: 'TIPCB: A Simple But Effective Part-based Convolutional Baseline For Text-based
  Person Search'
authors: Yuhao Chen, Guoqing Zhang, Yujiang Lu, Zhenxing Wang, Yuhui Zheng, Ruili
  Wang
conference: Neurocomputing
year: 2022
bibkey: chen2021tipcb
citations: 117
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2105.11628'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Tools & Libraries"]
short_authors: Chen et al.
---
Text-based person search is a sub-task in the field of image retrieval, which
aims to retrieve target person images according to a given textual description.
The significant feature gap between two modalities makes this task very
challenging. Many existing methods attempt to utilize local alignment to
address this problem in the fine-grained level. However, most relevant methods
introduce additional models or complicated training and evaluation strategies,
which are hard to use in realistic scenarios. In order to facilitate the
practical application, we propose a simple but effective end-to-end learning
framework for text-based person search named TIPCB (i.e., Text-Image Part-based
Convolutional Baseline). Firstly, a novel dual-path local alignment network
structure is proposed to extract visual and textual local representations, in
which images are segmented horizontally and texts are aligned adaptively. Then,
we propose a multi-stage cross-modal matching strategy, which eliminates the
modality gap from three feature levels, including low level, local level and
global level. Extensive experiments are conducted on the widely-used benchmark
dataset (CUHK-PEDES) and verify that our method outperforms the
state-of-the-art methods by 3.69%, 2.95% and 2.31% in terms of Top-1, Top-5 and
Top-10. Our code has been released in https://github.com/OrangeYHChen/TIPCB.