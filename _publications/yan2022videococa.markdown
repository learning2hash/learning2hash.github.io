---
layout: publication
title: 'Videococa: Video-text Modeling With Zero-shot Transfer From Contrastive Captioners'
authors: Shen Yan, Tao Zhu, Zirui Wang, Yuan Cao, Mi Zhang, Soham Ghosh, Yonghui Wu,
  Jiahui Yu
conference: Arxiv
year: 2022
bibkey: yan2022videococa
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.04979'}]
tags: ["Few Shot & Zero Shot", "Video Retrieval"]
short_authors: Yan et al.
---
We explore an efficient approach to establish a foundational video-text
model. We present VideoCoCa that maximally reuses a pretrained image-text
contrastive captioner (CoCa) model and adapt it to video-text tasks with
minimal extra training. While previous works adapt image-text models with
various cross-frame fusion modules, we find that the generative attentional
pooling and contrastive attentional pooling layers in CoCa are instantly
adaptable to flattened frame embeddings, yielding state-of-the-art results on
zero-shot video classification and zero-shot text-to-video retrieval.
Furthermore, we explore lightweight finetuning on top of VideoCoCa, and achieve
strong results on video question-answering and video captioning.