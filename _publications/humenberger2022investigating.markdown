---
layout: publication
title: Investigating The Role Of Image Retrieval For Visual Localization -- An Exhaustive
  Benchmark
authors: "Martin Humenberger, Yohann Cabon, No\xE9 Pion, Philippe Weinzaepfel, Donghwan\
  \ Lee, Nicolas Gu\xE9rin, Torsten Sattler, Gabriela Csurka"
conference: International Journal of Computer Vision
year: 2022
bibkey: humenberger2022investigating
citations: 28
additional_links: [{name: Code, url: 'https://github.com/naver/kapture-localization'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.15761'}]
tags: [Evaluation, Image Retrieval, Datasets]
short_authors: Humenberger et al.
---
Visual localization, i.e., camera pose estimation in a known scene, is a core
component of technologies such as autonomous driving and augmented reality.
State-of-the-art localization approaches often rely on image retrieval
techniques for one of two purposes: (1) provide an approximate pose estimate or
(2) determine which parts of the scene are potentially visible in a given query
image. It is common practice to use state-of-the-art image retrieval algorithms
for both of them. These algorithms are often trained for the goal of retrieving
the same landmark under a large range of viewpoint changes which often differs
from the requirements of visual localization. In order to investigate the
consequences for visual localization, this paper focuses on understanding the
role of image retrieval for multiple visual localization paradigms. First, we
introduce a novel benchmark setup and compare state-of-the-art retrieval
representations on multiple datasets using localization performance as metric.
Second, we investigate several definitions of "ground truth" for image
retrieval. Using these definitions as upper bounds for the visual localization
paradigms, we show that there is still sgnificant room for improvement. Third,
using these tools and in-depth analysis, we show that retrieval performance on
classical landmark retrieval or place recognition tasks correlates only for
some but not all paradigms to localization performance. Finally, we analyze the
effects of blur and dynamic scenes in the images. We conclude that there is a
need for retrieval approaches specifically designed for localization paradigms.
Our benchmark and evaluation protocols are available at
https://github.com/naver/kapture-localization.