---
layout: publication
title: 'Tencent Text-video Retrieval: Hierarchical Cross-modal Interactions With Multi-level
  Representations'
authors: Jie Jiang, Shaobo Min, Weijie Kong, Dihong Gong, Hongfa Wang, Zhifeng Li,
  Wei Liu
conference: IEEE Access
year: 2022
bibkey: jiang2022tencent
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.03382'}]
tags: ["Multimodal Retrieval", "Self-Supervised", "Video Retrieval"]
short_authors: Jiang et al.
---
Text-Video Retrieval plays an important role in multi-modal understanding and
has attracted increasing attention in recent years. Most existing methods focus
on constructing contrastive pairs between whole videos and complete caption
sentences, while overlooking fine-grained cross-modal relationships, e.g.,
clip-phrase or frame-word. In this paper, we propose a novel method, named
Hierarchical Cross-Modal Interaction (HCMI), to explore multi-level cross-modal
relationships among video-sentence, clip-phrase, and frame-word for text-video
retrieval. Considering intrinsic semantic frame relations, HCMI performs
self-attention to explore frame-level correlations and adaptively cluster
correlated frames into clip-level and video-level representations. In this way,
HCMI constructs multi-level video representations for frame-clip-video
granularities to capture fine-grained video content, and multi-level text
representations at word-phrase-sentence granularities for the text modality.
With multi-level representations for video and text, hierarchical contrastive
learning is designed to explore fine-grained cross-modal relationships, i.e.,
frame-word, clip-phrase, and video-sentence, which enables HCMI to achieve a
comprehensive semantic comparison between video and text modalities. Further
boosted by adaptive label denoising and marginal sample enhancement, HCMI
achieves new state-of-the-art results on various benchmarks, e.g., Rank@1 of
55.0%, 58.2%, 29.7%, 52.1%, and 57.3% on MSR-VTT, MSVD, LSMDC, DiDemo, and
ActivityNet, respectively.