---
layout: publication
title: 'Mask To Reconstruct: Cooperative Semantics Completion For Video-text Retrieval'
authors: Han Fang, Zhifei Yang, Xianghao Zang, Chao Ban, Hao Sun
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: fang2023mask
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.07910'}]
tags: ["Evaluation", "Multimodal Retrieval", "Text Retrieval", "Video Retrieval"]
short_authors: Fang et al.
---
Recently, masked video modeling has been widely explored and significantly
improved the model's understanding ability of visual regions at a local level.
However, existing methods usually adopt random masking and follow the same
reconstruction paradigm to complete the masked regions, which do not leverage
the correlations between cross-modal content. In this paper, we present Mask
for Semantics Completion (MASCOT) based on semantic-based masked modeling.
Specifically, after applying attention-based video masking to generate
high-informed and low-informed masks, we propose Informed Semantics Completion
to recover masked semantics information. The recovery mechanism is achieved by
aligning the masked content with the unmasked visual regions and corresponding
textual context, which makes the model capture more text-related details at a
patch level. Additionally, we shift the emphasis of reconstruction from
irrelevant backgrounds to discriminative parts to ignore regions with
low-informed masks. Furthermore, we design dual-mask co-learning to incorporate
video cues under different masks and learn more aligned video representation.
Our MASCOT performs state-of-the-art performance on four major text-video
retrieval benchmarks, including MSR-VTT, LSMDC, ActivityNet, and DiDeMo.
Extensive ablation studies demonstrate the effectiveness of the proposed
schemes.