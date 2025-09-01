---
layout: publication
title: 'Roargraph: A Projected Bipartite Graph For Efficient Cross-modal Approximate
  Nearest Neighbor Search'
authors: Meng Chen, Kai Zhang, Zhenying He, Yinan Jing, X. Sean Wang
conference: Proceedings of the VLDB Endowment
year: 2024
bibkey: chen2024roargraph
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.08933'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Recommender Systems"]
short_authors: Chen et al.
---
Approximate Nearest Neighbor Search (ANNS) is a fundamental and critical
component in many applications, including recommendation systems and large
language model-based applications. With the advancement of multimodal neural
models, which transform data from different modalities into a shared
high-dimensional space as feature vectors, cross-modal ANNS aims to use the
data vector from one modality (e.g., texts) as the query to retrieve the most
similar items from another (e.g., images or videos). However, there is an
inherent distribution gap between embeddings from different modalities, and
cross-modal queries become Out-of-Distribution (OOD) to the base data.
Consequently, state-of-the-art ANNS approaches suffer poor performance for OOD
workloads. In this paper, we quantitatively analyze the properties of the OOD
workloads to gain an understanding of their ANNS efficiency. Unlike
single-modal workloads, we reveal OOD queries spatially deviate from base data,
and the k-nearest neighbors of an OOD query are distant from each other in the
embedding space. The property breaks the assumptions of existing ANNS
approaches and mismatches their design for efficient search. With insights from
the OOD workloads, we propose pRojected bipartite Graph (RoarGraph), an
efficient ANNS graph index built under the guidance of query distribution.
Extensive experiments show that RoarGraph significantly outperforms
state-of-the-art approaches on modern cross-modal datasets, achieving up to
3.56x faster search speed at a 90% recall rate for OOD queries.