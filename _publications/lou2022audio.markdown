---
layout: publication
title: Audio-text Retrieval In Context
authors: Siyu Lou, Xuenan Xu, Mengyue Wu, Kai Yu
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: lou2022audio
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.13645'}]
tags: ["Datasets", "Evaluation", "ICASSP", "Text Retrieval"]
short_authors: Lou et al.
---
Audio-text retrieval based on natural language descriptions is a challenging
task. It involves learning cross-modality alignments between long sequences
under inadequate data conditions. In this work, we investigate several audio
features as well as sequence aggregation methods for better audio-text
alignment. Moreover, through a qualitative analysis we observe that semantic
mapping is more important than temporal relations in contextual retrieval.
Using pre-trained audio features and a descriptor-based aggregation method, we
build our contextual audio-text retrieval system. Specifically, we utilize
PANNs features pre-trained on a large sound event dataset and NetRVLAD pooling,
which directly works with averaged descriptors. Experiments are conducted on
the AudioCaps and CLOTHO datasets, and results are compared with the previous
state-of-the-art system. With our proposed system, a significant improvement
has been achieved on bidirectional audio-text retrieval, on all metrics
including recall, median and mean rank.