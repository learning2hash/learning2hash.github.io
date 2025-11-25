---
layout: publication
title: 'TVPR: Text-to-video Person Retrieval And A New Benchmark'
authors: Xu Zhang, Fan Ni, Guan-Nan Dong, Aichun Zhu, Jianhui Wu, Mingcheng Ni, Hui
  Liu
conference: The 32nd ACM International Conference on Multimedia. 2024 10105-10113
year: 2023
bibkey: zhang2023tvpr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.07184'}]
tags: ["Datasets", "Multimodal Retrieval", "Video Retrieval"]
short_authors: Zhang et al.
---
Most existing methods for text-based person retrieval focus on text-to-image
person retrieval. Nevertheless, due to the lack of dynamic information provided
by isolated frames, the performance is hampered when the person is obscured or
variable motion details are missed in isolated frames. To overcome this, we
propose a novel Text-to-Video Person Retrieval (TVPR) task. Since there is no
dataset or benchmark that describes person videos with natural language, we
construct a large-scale cross-modal person video dataset containing detailed
natural language annotations, termed as Text-to-Video Person Re-identification
(TVPReid) dataset. In this paper, we introduce a Multielement Feature Guided
Fragments Learning (MFGF) strategy, which leverages the cross-modal text-video
representations to provide strong text-visual and text-motion matching
information to tackle uncertain occlusion conflicting and variable motion
details. Specifically, we establish two potential cross-modal spaces for text
and video feature collaborative learning to progressively reduce the semantic
difference between text and video. To evaluate the effectiveness of the
proposed MFGF, extensive experiments have been conducted on TVPReid dataset. To
the best of our knowledge, MFGF is the first successful attempt to use video
for text-based person retrieval task and has achieved state-of-the-art
performance on TVPReid dataset. The TVPReid dataset will be publicly available
to benefit future research.