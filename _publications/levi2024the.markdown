---
layout: publication
title: The Double-ellipsoid Geometry Of CLIP
authors: Meir Yossef Levi, Guy Gilboa
conference: Proceedings of the 42nd International Conference on Machine Learning (ICML)
  2025
year: 2024
bibkey: levi2024the
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.14517'}]
tags: ["Datasets", "Distance Metric Learning", "ICML"]
short_authors: Meir Yossef Levi, Guy Gilboa
---
Contrastive Language-Image Pre-Training (CLIP) is highly instrumental in machine learning applications within a large variety of domains. We investigate the geometry of this embedding, which is still not well understood. We examine the raw unnormalized embedding and show that text and image reside on linearly separable ellipsoid shells, not centered at the origin. We explain the benefits of having this structure, allowing to better embed instances according to their uncertainty during contrastive training. Frequent concepts in the dataset yield more false negatives, inducing greater uncertainty. A new notion of conformity is introduced, which measures the average cosine similarity of an instance to any other instance within a representative data set. We show this measure can be accurately estimated by simply computing the cosine similarity to the modality mean vector. Furthermore, we find that CLIP's modality gap optimizes the matching of the conformity distributions of image and text.