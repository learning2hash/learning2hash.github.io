---
layout: publication
title: Benchmarking Image Retrieval For Visual Localization
authors: "No\xE9 Pion, Martin Humenberger, Gabriela Csurka, Yohann Cabon, Torsten\
  \ Sattler"
conference: 2020 International Conference on 3D Vision (3DV)
year: 2020
bibkey: pion2020benchmarking
citations: 4
additional_links: [{name: Code, url: 'https://github.com/naver/kapture-localization'},
  {name: Paper, url: 'https://arxiv.org/abs/2011.11946'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Robustness"]
short_authors: Pion et al.
---
Visual localization, i.e., camera pose estimation in a known scene, is a core
component of technologies such as autonomous driving and augmented reality.
State-of-the-art localization approaches often rely on image retrieval
techniques for one of two tasks: (1) provide an approximate pose estimate or
(2) determine which parts of the scene are potentially visible in a given query
image. It is common practice to use state-of-the-art image retrieval algorithms
for these tasks. These algorithms are often trained for the goal of retrieving
the same landmark under a large range of viewpoint changes. However, robustness
to viewpoint changes is not necessarily desirable in the context of visual
localization. This paper focuses on understanding the role of image retrieval
for multiple visual localization tasks. We introduce a benchmark setup and
compare state-of-the-art retrieval representations on multiple datasets. We
show that retrieval performance on classical landmark retrieval/recognition
tasks correlates only for some but not all tasks to localization performance.
This indicates a need for retrieval approaches specifically designed for
localization tasks. Our benchmark and evaluation protocols are available at
https://github.com/naver/kapture-localization.