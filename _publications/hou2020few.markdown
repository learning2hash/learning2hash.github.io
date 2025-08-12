---
layout: publication
title: Few-shot Learning For Multi-label Intent Detection
authors: Yutai Hou, Yongkui Lai, Yushan Wu, Wanxiang Che, Ting Liu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: hou2020few
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.05256'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Hou et al.
---
In this paper, we study the few-shot multi-label classification for user
intent detection. For multi-label intent detection, state-of-the-art work
estimates label-instance relevance scores and uses a threshold to select
multiple associated intent labels. To determine appropriate thresholds with
only a few examples, we first learn universal thresholding experience on
data-rich domains, and then adapt the thresholds to certain few-shot domains
with a calibration based on nonparametric learning. For better calculation of
label-instance relevance score, we introduce label name embedding as anchor
points in representation space, which refines representations of different
classes to be well-separated from each other. Experiments on two datasets show
that the proposed model significantly outperforms strong baselines in both
one-shot and five-shot settings.