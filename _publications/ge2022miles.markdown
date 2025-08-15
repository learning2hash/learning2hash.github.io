---
layout: publication
title: 'MILES: Visual BERT Pre-training With Injected Language Semantics For Video-text
  Retrieval'
authors: Yuying Ge, Yixiao Ge, Xihui Liu, Alex Jinpeng Wang, Jianping Wu, Ying Shan,
  Xiaohu Qie, Ping Luo
conference: Lecture Notes in Computer Science
year: 2022
bibkey: ge2022miles
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.12408'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Text Retrieval", "Video Retrieval"]
short_authors: Ge et al.
---
Dominant pre-training work for video-text retrieval mainly adopt the
"dual-encoder" architectures to enable efficient retrieval, where two separate
encoders are used to contrast global video and text representations, but ignore
detailed local semantics. The recent success of image BERT pre-training with
masked visual modeling that promotes the learning of local visual context,
motivates a possible solution to address the above limitation. In this work, we
for the first time investigate masked visual modeling in video-text
pre-training with the "dual-encoder" architecture. We perform Masked visual
modeling with Injected LanguagE Semantics (MILES) by employing an extra
snapshot video encoder as an evolving "tokenizer" to produce reconstruction
targets for masked video patch prediction. Given the corrupted video, the video
encoder is trained to recover text-aligned features of the masked patches via
reasoning with the visible regions along the spatial and temporal dimensions,
which enhances the discriminativeness of local visual features and the
fine-grained cross-modality alignment. Our method outperforms state-of-the-art
methods for text-to-video retrieval on four datasets with both zero-shot and
fine-tune evaluation protocols. Our approach also surpasses the baseline models
significantly on zero-shot action recognition, which can be cast as
video-to-text retrieval.