---
layout: publication
title: Efficient Centroid-linkage Clustering
authors: "Mohammadhossein Bateni, Laxman Dhulipala, Willem Fletcher, Kishen N Gowda,\
  \ D Ellis Hershkowitz, Rajesh Jayaram, Jakub \u0141\u0105cki"
conference: Arxiv
year: 2024
bibkey: bateni2024efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.05066'}]
tags: ["Efficiency", "Tools & Libraries"]
short_authors: Bateni et al.
---
We give an efficient algorithm for Centroid-Linkage Hierarchical
Agglomerative Clustering (HAC), which computes a \(c\)-approximate clustering in
roughly \(n^\{1+O(1/c^2)\}\) time. We obtain our result by combining a new
Centroid-Linkage HAC algorithm with a novel fully dynamic data structure for
nearest neighbor search which works under adaptive updates.
  We also evaluate our algorithm empirically. By leveraging a state-of-the-art
nearest-neighbor search library, we obtain a fast and accurate Centroid-Linkage
HAC algorithm. Compared to an existing state-of-the-art exact baseline, our
implementation maintains the clustering quality while delivering up to a
\(36\times\) speedup due to performing fewer distance comparisons.