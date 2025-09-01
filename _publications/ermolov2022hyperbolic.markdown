---
layout: publication
title: 'Hyperbolic Vision Transformers: Combining Improvements In Metric Learning'
authors: Aleksandr Ermolov, Leyla Mirvakhabova, Valentin Khrulkov, Nicu Sebe, Ivan
  Oseledets
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: ermolov2022hyperbolic
citations: 65
additional_links: [{name: Code, url: 'https://github.com/htdt/hyp_metric.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.10833'}]
tags: ["CVPR", "Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Ermolov et al.
---
Metric learning aims to learn a highly discriminative model encouraging the
embeddings of similar classes to be close in the chosen metrics and pushed
apart for dissimilar ones. The common recipe is to use an encoder to extract
embeddings and a distance-based loss function to match the representations --
usually, the Euclidean distance is utilized. An emerging interest in learning
hyperbolic data embeddings suggests that hyperbolic geometry can be beneficial
for natural data. Following this line of work, we propose a new
hyperbolic-based model for metric learning. At the core of our method is a
vision transformer with output embeddings mapped to hyperbolic space. These
embeddings are directly optimized using modified pairwise cross-entropy loss.
We evaluate the proposed model with six different formulations on four datasets
achieving the new state-of-the-art performance. The source code is available at
https://github.com/htdt/hyp_metric.