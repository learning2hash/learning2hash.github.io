---
layout: publication
title: Multi-shot Person Re-identification Through Set Distance With Visual Distributional
  Representation
authors: Ting-Yao Hu, Xiaojun Chang, Alexander G. Hauptmann
conference: Proceedings of the 2019 on International Conference on Multimedia Retrieval
year: 2019
bibkey: hu2018multi
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.01119'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Ting-Yao Hu, Xiaojun Chang, Alexander G. Hauptmann
---
Person re-identification aims to identify a specific person at distinct times
and locations. It is challenging because of occlusion, illumination, and
viewpoint change in camera views. Recently, multi-shot person re-id task
receives more attention since it is closer to real-world application. A key
point of a good algorithm for multi-shot person re-id is the temporal
aggregation of the person appearance features. While most of the current
approaches apply pooling strategies and obtain a fixed-size vector
representation, these may lose the matching evidence between examples. In this
work, we propose the idea of visual distributional representation, which
interprets an image set as samples drawn from an unknown distribution in
appearance feature space. Based on the supervision signals from a downstream
task of interest, the method reshapes the appearance feature space and further
learns the unknown distribution of each image set. In the context of multi-shot
person re-id, we apply this novel concept along with Wasserstein distance and
learn a distributional set distance function between two image sets. In this
way, the proper alignment between two image sets can be discovered naturally in
a non-parametric manner. Our experiment results on two public datasets show the
advantages of our proposed method compared to other state-of-the-art
approaches.