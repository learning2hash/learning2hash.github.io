---
layout: publication
title: 'DDS-NAS: Dynamic Data Selection Within Neural Architecture Search Via On-line
  Hard Example Mining Applied To Image Classification'
authors: Matt Poyser, Toby P. Breckon
conference: Pattern Recognition
year: 2025
bibkey: poyser2025dds
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.14667'}]
tags: ["CVPR", "Datasets", "Evaluation", "Scalability", "Tree Based ANN"]
short_authors: Matt Poyser, Toby P. Breckon
---
In order to address the scalability challenge within Neural Architecture Search (NAS), we speed up NAS training via dynamic hard example mining within a curriculum learning framework. By utilizing an autoencoder that enforces an image similarity embedding in latent space, we construct an efficient kd-tree structure to order images by furthest neighbour dissimilarity in a low-dimensional embedding. From a given query image from our subsample dataset, we can identify the most dissimilar image within the global dataset in logarithmic time. Via curriculum learning, we then dynamically re-formulate an unbiased subsample dataset for NAS optimisation, upon which the current NAS solution architecture performs poorly. We show that our DDS-NAS framework speeds up gradient-based NAS strategies by up to 27x without loss in performance. By maximising the contribution of each image sample during training, we reduce the duration of a NAS training cycle and the number of iterations required for convergence.