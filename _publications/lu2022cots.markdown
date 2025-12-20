---
layout: publication
title: 'COTS: Collaborative Two-stream Vision-language Pre-training Model For Cross-modal
  Retrieval'
authors: Haoyu Lu, Nanyi Fei, Yuqi Huo, Yizhao Gao, Zhiwu Lu, Ji-Rong Wen
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: lu2022cots
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.07441'}]
tags: ["Datasets", "Efficiency", "Multimodal Retrieval", "Text Retrieval", "Video Retrieval"]
short_authors: Lu et al.
---
Large-scale single-stream pre-training has shown dramatic performance in
image-text retrieval. Regrettably, it faces low inference efficiency due to
heavy attention layers. Recently, two-stream methods like CLIP and ALIGN with
high inference efficiency have also shown promising performance, however, they
only consider instance-level alignment between the two streams (thus there is
still room for improvement). To overcome these limitations, we propose a novel
COllaborative Two-Stream vision-language pretraining model termed COTS for
image-text retrieval by enhancing cross-modal interaction. In addition to
instance level alignment via momentum contrastive learning, we leverage two
extra levels of cross-modal interactions in our COTS: (1) Token-level
interaction - a masked visionlanguage modeling (MVLM) learning objective is
devised without using a cross-stream network module, where variational
autoencoder is imposed on the visual encoder to generate visual tokens for each
image. (2) Task-level interaction - a KL-alignment learning objective is
devised between text-to-image and image-to-text retrieval tasks, where the
probability distribution per task is computed with the negative queues in
momentum contrastive learning. Under a fair comparison setting, our COTS
achieves the highest performance among all two-stream methods and comparable
performance (but with 10,800X faster in inference) w.r.t. the latest
single-stream methods. Importantly, our COTS is also applicable to
text-to-video retrieval, yielding new state-ofthe-art on the widely-used
MSR-VTT dataset.