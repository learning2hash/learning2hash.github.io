---
layout: publication
title: Retrieval And Localization With Observation Constraints
authors: Yuhao Zhou, Huanhuan Fan, Shuang Gao, Yuchen Yang, Xudong Zhang, Jijunnan
  Li, Yandong Guo
conference: 2021 IEEE International Conference on Robotics and Automation (ICRA)
year: 2021
bibkey: zhou2021retrieval
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.08516'}]
tags: ["Datasets", "ICRA", "Image Retrieval"]
short_authors: Zhou et al.
---
Accurate visual re-localization is very critical to many artificial
intelligence applications, such as augmented reality, virtual reality, robotics
and autonomous driving. To accomplish this task, we propose an integrated
visual re-localization method called RLOCS by combining image retrieval,
semantic consistency and geometry verification to achieve accurate estimations.
The localization pipeline is designed as a coarse-to-fine paradigm. In the
retrieval part, we cascade the architecture of ResNet101-GeM-ArcFace and employ
DBSCAN followed by spatial verification to obtain a better initial coarse pose.
We design a module called observation constraints, which combines geometry
information and semantic consistency for filtering outliers. Comprehensive
experiments are conducted on open datasets, including retrieval on R-Oxford5k
and R-Paris6k, semantic segmentation on Cityscapes, localization on Aachen
Day-Night and InLoc. By creatively modifying separate modules in the total
pipeline, our method achieves many performance improvements on the challenging
localization benchmarks.