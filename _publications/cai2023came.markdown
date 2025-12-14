---
layout: publication
title: 'CAME: Competitively Learning A Mixture-of-experts Model For First-stage Retrieval'
authors: Yinqiong Cai, Yixing Fan, Keping Bi, Jiafeng Guo, Wei Chen, Ruqing Zhang,
  Xueqi Cheng
conference: Arxiv
year: 2023
bibkey: cai2023came
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.02834'}]
tags: [Evaluation, Datasets]
short_authors: Cai et al.
---
The first-stage retrieval aims to retrieve a subset of candidate documents
from a huge collection both effectively and efficiently. Since various matching
patterns can exist between queries and relevant documents, previous work tries
to combine multiple retrieval models to find as many relevant results as
possible. The constructed ensembles, whether learned independently or jointly,
do not care which component model is more suitable to an instance during
training. Thus, they cannot fully exploit the capabilities of different types
of retrieval models in identifying diverse relevance patterns. Motivated by
this observation, in this paper, we propose a Mixture-of-Experts (MoE) model
consisting of representative matching experts and a novel competitive learning
mechanism to let the experts develop and enhance their expertise during
training. Specifically, our MoE model shares the bottom layers to learn common
semantic representations and uses differently structured upper layers to
represent various types of retrieval experts. Our competitive learning
mechanism has two stages: (1) a standardized learning stage to train the
experts equally to develop their capabilities to conduct relevance matching;
(2) a specialized learning stage where the experts compete with each other on
every training instance and get rewards and updates according to their
performance to enhance their expertise on certain types of samples.
Experimental results on three retrieval benchmark datasets show that our method
significantly outperforms the state-of-the-art baselines.