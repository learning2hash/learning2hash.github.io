---
layout: publication
title: Enhancing Clustering Representations With Positive Proximity And Cluster Dispersion
  Learning
authors: Abhishek Kumar, Dong-gyu Lee
conference: Information Sciences
year: 2024
bibkey: kumar2023enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.00731'}]
tags: []
short_authors: Abhishek Kumar, Dong-gyu Lee
---
Contemporary deep clustering approaches often rely on either contrastive or
non-contrastive techniques to acquire effective representations for clustering
tasks. Contrastive methods leverage negative pairs to achieve homogenous
representations but can introduce class collision issues, potentially
compromising clustering performance. On the contrary, non-contrastive
techniques prevent class collisions but may produce non-uniform representations
that lead to clustering collapse. In this work, we propose a novel end-to-end
deep clustering approach named PIPCDR, designed to harness the strengths of
both approaches while mitigating their limitations. PIPCDR incorporates a
positive instance proximity loss and a cluster dispersion regularizer. The
positive instance proximity loss ensures alignment between augmented views of
instances and their sampled neighbors, enhancing within-cluster compactness by
selecting genuinely positive pairs within the embedding space. Meanwhile, the
cluster dispersion regularizer maximizes inter-cluster distances while
minimizing within-cluster compactness, promoting uniformity in the learned
representations. PIPCDR excels in producing well-separated clusters, generating
uniform representations, avoiding class collision issues, and enhancing
within-cluster compactness. We extensively validate the effectiveness of PIPCDR
within an end-to-end Majorize-Minimization framework, demonstrating its
competitive performance on moderate-scale clustering benchmark datasets and
establishing new state-of-the-art results on large-scale datasets.