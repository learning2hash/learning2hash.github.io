---
layout: publication
title: Multi-granularity Association Learning Framework For On-the-fly Fine-grained
  Sketch-based Image Retrieval
authors: Dawei Dai, Xiaoyu Tang, Shuyin Xia, Yingge Liu, Guoyin Wang, Zizhong Chen
conference: Arxiv
year: 2022
bibkey: dai2022multi
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.05007'}]
tags: []
short_authors: Dai et al.
---
Fine-grained sketch-based image retrieval (FG-SBIR) addresses the problem of
retrieving a particular photo in a given query sketch. However, its widespread
applicability is limited by the fact that it is difficult to draw a complete
sketch for most people, and the drawing process often takes time. In this
study, we aim to retrieve the target photo with the least number of strokes
possible (incomplete sketch), named on-the-fly FG-SBIR (Bhunia et al. 2020),
which starts retrieving at each stroke as soon as the drawing begins. We
consider that there is a significant correlation among these incomplete
sketches in the sketch drawing episode of each photo. To learn more efficient
joint embedding space shared between the photo and its incomplete sketches, we
propose a multi-granularity association learning framework that further
optimizes the embedding space of all incomplete sketches. Specifically, based
on the integrity of the sketch, we can divide a complete sketch episode into
several stages, each of which corresponds to a simple linear mapping layer.
Moreover, our framework guides the vector space representation of the current
sketch to approximate that of its later sketches to realize the retrieval
performance of the sketch with fewer strokes to approach that of the sketch
with more strokes. In the experiments, we proposed more realistic challenges,
and our method achieved superior early retrieval efficiency over the
state-of-the-art methods and alternative baselines on two publicly available
fine-grained sketch retrieval datasets.