---
layout: publication
title: 'Narrating The Video: Boosting Text-video Retrieval Via Comprehensive Utilization
  Of Frame-level Captions'
authors: Chan Hur, Jeong-Hun Hong, Dong-Hun Lee, Dabin Kang, Semin Myeong, Sang-Hyo
  Park, Hyeyoung Park
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: hur2025narrating
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.05186'}]
tags: [Video Retrieval, Evaluation, Datasets, CVPR, Tools & Libraries]
short_authors: Hur et al.
---
In recent text-video retrieval, the use of additional captions from
vision-language models has shown promising effects on the performance. However,
existing models using additional captions often have struggled to capture the
rich semantics, including temporal changes, inherent in the video. In addition,
incorrect information caused by generative models can lead to inaccurate
retrieval. To address these issues, we propose a new framework, Narrating the
Video (NarVid), which strategically leverages the comprehensive information
available from frame-level captions, the narration. The proposed NarVid
exploits narration in multiple ways: 1) feature enhancement through cross-modal
interactions between narration and video, 2) query-aware adaptive filtering to
suppress irrelevant or incorrect information, 3) dual-modal matching score by
adding query-video similarity and query-narration similarity, and 4)
hard-negative loss to learn discriminative features from multiple perspectives
using the two similarities from different views. Experimental results
demonstrate that NarVid achieves state-of-the-art performance on various
benchmark datasets.