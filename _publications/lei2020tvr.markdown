---
layout: publication
title: 'TVR: A Large-scale Dataset For Video-subtitle Moment Retrieval'
authors: Jie Lei, Licheng Yu, Tamara L. Berg, Mohit Bansal
conference: Lecture Notes in Computer Science
year: 2020
bibkey: lei2020tvr
citations: 174
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.09099'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Lei et al.
---
We introduce TV show Retrieval (TVR), a new multimodal retrieval dataset. TVR
requires systems to understand both videos and their associated subtitle
(dialogue) texts, making it more realistic. The dataset contains 109K queries
collected on 21.8K videos from 6 TV shows of diverse genres, where each query
is associated with a tight temporal window. The queries are also labeled with
query types that indicate whether each of them is more related to video or
subtitle or both, allowing for in-depth analysis of the dataset and the methods
that built on top of it. Strict qualification and post-annotation verification
tests are applied to ensure the quality of the collected data. Further, we
present several baselines and a novel Cross-modal Moment Localization (XML )
network for multimodal moment retrieval tasks. The proposed XML model uses a
late fusion design with a novel Convolutional Start-End detector (ConvSE),
surpassing baselines by a large margin and with better efficiency, providing a
strong starting point for future work. We have also collected additional
descriptions for each annotated moment in TVR to form a new multimodal
captioning dataset with 262K captions, named TV show Caption (TVC). Both
datasets are publicly available. TVR: https://tvr.cs.unc.edu, TVC:
https://tvr.cs.unc.edu/tvc.html.