---
layout: publication
title: Attributable Visual Similarity Learning
authors: Borui Zhang, Wenzhao Zheng, Jie Zhou, Jiwen Lu
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: zhang2022attributable
citations: 13
additional_links: [{name: Code, url: 'https://github.com/zbr17/AVSL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.14932'}]
tags: ["CVPR", "Distance Metric Learning", "Image Retrieval", "Similarity Search"]
short_authors: Zhang et al.
---
This paper proposes an attributable visual similarity learning (AVSL)
framework for a more accurate and explainable similarity measure between
images. Most existing similarity learning methods exacerbate the
unexplainability by mapping each sample to a single point in the embedding
space with a distance metric (e.g., Mahalanobis distance, Euclidean distance).
Motivated by the human semantic similarity cognition, we propose a generalized
similarity learning paradigm to represent the similarity between two images
with a graph and then infer the overall similarity accordingly. Furthermore, we
establish a bottom-up similarity construction and top-down similarity inference
framework to infer the similarity based on semantic hierarchy consistency. We
first identify unreliable higher-level similarity nodes and then correct them
using the most coherent adjacent lower-level similarity nodes, which
simultaneously preserve traces for similarity attribution. Extensive
experiments on the CUB-200-2011, Cars196, and Stanford Online Products datasets
demonstrate significant improvements over existing deep similarity learning
methods and verify the interpretability of our framework. Code is available at
https://github.com/zbr17/AVSL.