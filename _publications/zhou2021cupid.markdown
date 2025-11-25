---
layout: publication
title: 'CUPID: Adaptive Curation Of Pre-training Data For Video-and-language Representation
  Learning'
authors: Luowei Zhou, Jingjing Liu, Yu Cheng, Zhe Gan, Lei Zhang
conference: Arxiv
year: 2021
bibkey: zhou2021cupid
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.00285'}]
tags: ["Evaluation", "Video Retrieval"]
short_authors: Zhou et al.
---
This work concerns video-language pre-training and representation learning.
In this now ubiquitous training scheme, a model first performs pre-training on
paired videos and text (e.g., video clips and accompanied subtitles) from a
large uncurated source corpus, before transferring to specific downstream
tasks. This two-stage training process inevitably raises questions about the
generalization ability of the pre-trained model, which is particularly
pronounced when a salient domain gap exists between source and target data
(e.g., instructional cooking videos vs. movies). In this paper, we first bring
to light the sensitivity of pre-training objectives (contrastive vs.
reconstructive) to domain discrepancy. Then, we propose a simple yet effective
framework, CUPID, to bridge this domain gap by filtering and adapting source
data to the target data, followed by domain-focused pre-training. Comprehensive
experiments demonstrate that pre-training on a considerably small subset of
domain-focused data can effectively close the source-target domain gap and
achieve significant performance gain, compared to random sampling or even
exploiting the full pre-training dataset. CUPID yields new state-of-the-art
performance across multiple video-language and video tasks, including
text-to-video retrieval [72, 37], video question answering [36], and video
captioning [72], with consistent performance lift over different pre-training
methods.