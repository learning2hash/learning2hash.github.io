---
layout: publication
title: 'Vidla: Video-language Alignment At Scale'
authors: Mamshad Nayeem Rizve, Fan Fei, Jayakrishnan Unnikrishnan, Son Tran, Benjamin
  Z. Yao, Belinda Zeng, Mubarak Shah, Trishul Chilimbi
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: rizve2024vidla
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.14870'}]
tags: [Scalability, Evaluation, CVPR, Datasets]
short_authors: Rizve et al.
---
In this paper, we propose VidLA, an approach for video-language alignment at
scale. There are two major limitations of previous video-language alignment
approaches. First, they do not capture both short-range and long-range temporal
dependencies and typically employ complex hierarchical deep network
architectures that are hard to integrate with existing pretrained image-text
foundation models. To effectively address this limitation, we instead keep the
network architecture simple and use a set of data tokens that operate at
different temporal resolutions in a hierarchical manner, accounting for the
temporally hierarchical nature of videos. By employing a simple two-tower
architecture, we are able to initialize our video-language model with
pretrained image-text foundation models, thereby boosting the final
performance. Second, existing video-language alignment works struggle due to
the lack of semantically aligned large-scale training data. To overcome it, we
leverage recent LLMs to curate the largest video-language dataset to date with
better visual grounding. Furthermore, unlike existing video-text datasets which
only contain short clips, our dataset is enriched with video clips of varying
durations to aid our temporally hierarchical data tokens in extracting better
representations at varying temporal scales. Overall, empirical results show
that our proposed approach surpasses state-of-the-art methods on multiple
retrieval benchmarks, especially on longer videos, and performs competitively
on classification benchmarks.