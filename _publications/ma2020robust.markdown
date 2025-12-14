---
layout: publication
title: Robust Line Segments Matching Via Graph Convolution Networks
authors: Quanmeng Ma, Guang Jiang, Dianzhi Lai
conference: Arxiv
year: 2020
bibkey: ma2020robust
citations: 9
additional_links: [{name: Code, url: 'https://github.com/mameng1/GraphLineMatching'},
  {name: Paper, url: 'https://arxiv.org/abs/2004.04993'}]
tags: [Evaluation, Graph-based ANN]
short_authors: Quanmeng Ma, Guang Jiang, Dianzhi Lai
---
Line matching plays an essential role in structure from motion (SFM) and
simultaneous localization and mapping (SLAM), especially in low-textured and
repetitive scenes. In this paper, we present a new method of using a graph
convolution network to match line segments in a pair of images, and we design a
graph-based strategy of matching line segments with relaxing to an optimal
transport problem. In contrast to hand-crafted line matching algorithms, our
approach learns local line segment descriptor and the matching simultaneously
through end-to-end training. The results show our method outperforms the
state-of-the-art techniques, and especially, the recall is improved from 45.28%
to 70.47% under a similar presicion. The code of our work is available at
https://github.com/mameng1/GraphLineMatching.