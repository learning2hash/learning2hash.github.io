---
layout: publication
title: Hybrid Losses For Hierarchical Embedding Learning
authors: Haokun Tian, Stefan Lattner, Brian McFee, Charalampos Saitis
conference: Arxiv
year: 2025
bibkey: tian2025hybrid
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.12796'}]
tags: []
short_authors: Tian et al.
---
In traditional supervised learning, the cross-entropy loss treats all
incorrect predictions equally, ignoring the relevance or proximity of wrong
labels to the correct answer. By leveraging a tree hierarchy for fine-grained
labels, we investigate hybrid losses, such as generalised triplet and
cross-entropy losses, to enforce similarity between labels within a multi-task
learning framework. We propose metrics to evaluate the embedding space
structure and assess the model's ability to generalise to unseen classes, that
is, to infer similar classes for data belonging to unseen categories. Our
experiments on OrchideaSOL, a four-level hierarchical instrument sound dataset
with nearly 200 detailed categories, demonstrate that the proposed hybrid
losses outperform previous works in classification, retrieval, embedding space
structure, and generalisation.