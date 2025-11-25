---
layout: publication
title: 'Separating The "chirp" From The "chat": Self-supervised Visual Grounding Of
  Sound And Language'
authors: Mark Hamilton, Andrew Zisserman, John R. Hershey, William T. Freeman
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: hamilton2024separating
citations: 5
additional_links: [{name: Code, url: 'https://aka.ms/denseav\'}, {name: Paper, url: 'https://arxiv.org/abs/2406.05629'}]
tags: ["CVPR", "Datasets", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Hamilton et al.
---
We present DenseAV, a novel dual encoder grounding architecture that learns
high-resolution, semantically meaningful, and audio-visually aligned features
solely through watching videos. We show that DenseAV can discover the
``meaning'' of words and the ``location'' of sounds without explicit
localization supervision. Furthermore, it automatically discovers and
distinguishes between these two types of associations without supervision. We
show that DenseAV's localization abilities arise from a new multi-head feature
aggregation operator that directly compares dense image and audio
representations for contrastive learning. In contrast, many other systems that
learn ``global'' audio and video representations cannot localize words and
sound. Finally, we contribute two new datasets to improve the evaluation of AV
representations through speech and sound prompted semantic segmentation. On
these and other datasets we show DenseAV dramatically outperforms the prior art
on speech and sound prompted semantic segmentation. DenseAV outperforms the
previous state-of-the-art, ImageBind, on cross-modal retrieval using fewer than
half of the parameters. Project Page:
\href\{https://aka.ms/denseav\}\{https://aka.ms/denseav\}