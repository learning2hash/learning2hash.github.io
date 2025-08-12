---
layout: publication
title: 'Movieclip: Visual Scene Recognition In Movies'
authors: Digbalay Bose, Rajat Hebbar, Krishna Somandepalli, Haoyang Zhang, Yin Cui,
  Kree Cole-mclaughlin, Huisheng Wang, Shrikanth Narayanan
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: bose2022movieclip
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.11065'}]
tags: ["Datasets"]
short_authors: Bose et al.
---
Longform media such as movies have complex narrative structures, with events
spanning a rich variety of ambient visual scenes. Domain specific challenges
associated with visual scenes in movies include transitions, person coverage,
and a wide array of real-life and fictional scenarios. Existing visual scene
datasets in movies have limited taxonomies and don't consider the visual scene
transition within movie clips. In this work, we address the problem of visual
scene recognition in movies by first automatically curating a new and extensive
movie-centric taxonomy of 179 scene labels derived from movie scripts and
auxiliary web-based video datasets. Instead of manual annotations which can be
expensive, we use CLIP to weakly label 1.12 million shots from 32K movie clips
based on our proposed taxonomy. We provide baseline visual models trained on
the weakly labeled dataset called MovieCLIP and evaluate them on an independent
dataset verified by human raters. We show that leveraging features from models
pretrained on MovieCLIP benefits downstream tasks such as multi-label scene and
genre classification of web videos and movie trailers.