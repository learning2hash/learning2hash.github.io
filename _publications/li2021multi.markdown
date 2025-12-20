---
layout: publication
title: Multi-scale 2D Representation Learning For Weakly-supervised Moment Retrieval
authors: Ding Li, Rui Wu, Yongqiang Tang, Zhizhong Zhang, Wensheng Zhang
conference: Arxiv
year: 2021
bibkey: li2021multi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.02741'}]
tags: ["Datasets", "Evaluation", "Supervised"]
short_authors: Li et al.
---
Video moment retrieval aims to search the moment most relevant to a given
language query. However, most existing methods in this community often require
temporal boundary annotations which are expensive and time-consuming to label.
Hence weakly supervised methods have been put forward recently by only using
coarse video-level label. Despite effectiveness, these methods usually process
moment candidates independently, while ignoring a critical issue that the
natural temporal dependencies between candidates in different temporal scales.
To cope with this issue, we propose a Multi-scale 2D Representation Learning
method for weakly supervised video moment retrieval. Specifically, we first
construct a two-dimensional map for each temporal scale to capture the temporal
dependencies between candidates. Two dimensions in this map indicate the start
and end time points of these candidates. Then, we select top-K candidates from
each scale-varied map with a learnable convolutional neural network. With a
newly designed Moments Evaluation Module, we obtain the alignment scores of the
selected candidates. At last, the similarity between captions and language
query is served as supervision for further training the candidates' selector.
Experiments on two benchmark datasets Charades-STA and ActivityNet Captions
demonstrate that our approach achieves superior performance to state-of-the-art
results.