---
layout: publication
title: 'Movienet-ps: A Large-scale Person Search Dataset In The Wild'
authors: Jie Qin, Peng Zheng, Yichao Yan, Rong Quan, Xiaogang Cheng, Bingbing Ni
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: qin2021movienet
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.02500'}]
tags: ["Datasets", "ICASSP", "Scalability"]
short_authors: Qin et al.
---
Person search aims to jointly localize and identify a query person from
natural, uncropped images, which has been actively studied over the past few
years. In this paper, we delve into the rich context information globally and
locally surrounding the target person, which we refer to as scene and group
context, respectively. Unlike previous works that treat the two types of
context individually, we exploit them in a unified global-local context network
(GLCNet) with the intuitive aim of feature enhancement. Specifically, re-ID
embeddings and context features are simultaneously learned in a multi-stage
fashion, ultimately leading to enhanced, discriminative features for person
search. We conduct the experiments on two person search benchmarks (i.e.,
CUHK-SYSU and PRW) as well as extend our approach to a more challenging setting
(i.e., character search on MovieNet). Extensive experimental results
demonstrate the consistent improvement of the proposed GLCNet over the
state-of-the-art methods on all three datasets. Our source codes, pre-trained
models, and the new dataset are publicly available at:
https://github.com/ZhengPeng7/GLCNet.