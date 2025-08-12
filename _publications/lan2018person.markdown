---
layout: publication
title: Person Search By Multi-scale Matching
authors: Xu Lan, Xiatian Zhu, Shaogang Gong
conference: Lecture Notes in Computer Science
year: 2018
bibkey: lan2018person
citations: 159
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.08582'}]
tags: []
short_authors: Xu Lan, Xiatian Zhu, Shaogang Gong
---
We consider the problem of person search in unconstrained scene images.
Existing methods usually focus on improving the person detection accuracy to
mitigate negative effects imposed by misalignment, mis-detections, and false
alarms resulted from noisy people auto-detection. In contrast to previous
studies, we show that sufficiently reliable person instance cropping is
achievable by slightly improved state-of-the-art deep learning object detectors
(e.g. Faster-RCNN), and the under-studied multi-scale matching problem in
person search is a more severe barrier. In this work, we address this
multi-scale person search challenge by proposing a Cross-Level Semantic
Alignment (CLSA) deep learning approach capable of learning more discriminative
identity feature representations in a unified end-to-end model. This is
realised by exploiting the in-network feature pyramid structure of a deep
neural network enhanced by a novel cross pyramid-level semantic alignment loss
function. This favourably eliminates the need for constructing a
computationally expensive image pyramid and a complex multi-branch network
architecture. Extensive experiments show the modelling advantages and
performance superiority of CLSA over the state-of-the-art person search and
multi-scale matching methods on two large person search benchmarking datasets:
CUHK-SYSU and PRW.