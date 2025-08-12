---
layout: publication
title: Content And Salient Semantics Collaboration For Cloth-changing Person Re-identification
authors: Qizao Wang, Xuelin Qian, Bin Li, Lifeng Chen, Yanwei Fu, Xiangyang Xue
conference: Arxiv
year: 2024
bibkey: wang2024content
citations: 1
additional_links: [{name: Code, url: 'https://github.com/QizaoWang/CSSC-CCReID'},
  {name: Paper, url: 'https://arxiv.org/abs/2405.16597'}]
tags: []
short_authors: Wang et al.
---
Cloth-changing person re-identification aims at recognizing the same person
with clothing changes across non-overlapping cameras. Advanced methods either
resort to identity-related auxiliary modalities (e.g., sketches, silhouettes,
and keypoints) or clothing labels to mitigate the impact of clothes. However,
relying on unpractical and inflexible auxiliary modalities or annotations
limits their real-world applicability. In this paper, we promote cloth-changing
person re-identification by leveraging abundant semantics present within
pedestrian images, without the need for any auxiliaries. Specifically, we first
propose a unified Semantics Mining and Refinement (SMR) module to extract
robust identity-related content and salient semantics, mitigating interference
from clothing appearances effectively. We further propose the Content and
Salient Semantics Collaboration (CSSC) framework to collaborate and leverage
various semantics, facilitating cross-parallel semantic interaction and
refinement. Our proposed method achieves state-of-the-art performance on three
cloth-changing benchmarks, demonstrating its superiority over advanced
competitors. The code is available at https://github.com/QizaoWang/CSSC-CCReID.