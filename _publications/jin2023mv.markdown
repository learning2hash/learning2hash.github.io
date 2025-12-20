---
layout: publication
title: 'Mv-adapter: Multimodal Video Transfer Learning For Video Text Retrieval'
authors: Xiaojie Jin, Bowen Zhang, Weibo Gong, Kai Xu, Xueqing Deng, Peng Wang, Zhao
  Zhang, Xiaohui Shen, Jiashi Feng
conference: Arxiv
year: 2023
bibkey: jin2023mv
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.07868'}]
tags: ["Evaluation", "Memory Efficiency", "Text Retrieval"]
short_authors: Jin et al.
---
State-of-the-art video-text retrieval (VTR) methods typically involve fully
fine-tuning a pre-trained model (e.g. CLIP) on specific datasets. However, this
can result in significant storage costs in practical applications as a separate
model per task must be stored. To address this issue, we present our pioneering
work that enables parameter-efficient VTR using a pre-trained model, with only
a small number of tunable parameters during training. Towards this goal, we
propose a new method dubbed Multimodal Video Adapter (MV-Adapter) for
efficiently transferring the knowledge in the pre-trained CLIP from image-text
to video-text. Specifically, MV-Adapter utilizes bottleneck structures in both
video and text branches, along with two novel components. The first is a
Temporal Adaptation Module that is incorporated in the video branch to
introduce global and local temporal contexts. We also train weights
calibrations to adjust to dynamic variations across frames. The second is Cross
Modality Tying that generates weights for video/text branches through sharing
cross modality factors, for better aligning between modalities. Thanks to above
innovations, MV-Adapter can achieve comparable or better performance than
standard full fine-tuning with negligible parameters overhead. Notably,
MV-Adapter consistently outperforms various competing methods in V2T/T2V tasks
with large margins on five widely used VTR benchmarks (MSR-VTT, MSVD, LSMDC,
DiDemo, and ActivityNet).