---
layout: publication
title: 'Locality-sensitive Hashing For Efficient Hard Negative Sampling In Contrastive Learning'
authors: Fabian Deuser et al.
conference: "Arxiv"
year: 2025
citations: 0
bibkey: deuser2025locality
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2505.17844'}
tags: ['Deep', 'Retrieval Models', 'Unimodal', 'Datasets', 'Vector Indexing', 'Supervised', 'Hashing']
---
Contrastive learning is a representational learning paradigm in which a neural network maps data elements to feature vectors. It improves the feature space by forming lots with an anchor and examples that are either positive or negative based on class similarity. Hard negative examples, which are close to the anchor in the feature space but from a different class, improve learning performance. Finding such examples of high quality efficiently in large, high-dimensional datasets is computationally challenging. In this paper, we propose a GPU-friendly Locality-Sensitive Hashing (LSH) scheme that quantizes real-valued feature vectors into binary representations for approximate nearest neighbor search. We investigate its theoretical properties and evaluate it on several datasets from textual and visual domain. Our approach achieves comparable or better performance while requiring significantly less computation than existing hard negative mining strategies.
