---
layout: publication
title: 'Infinity Search: Approximate Vector Search With Projections On Q-metric Spaces'
authors: Pariente et al.
conference: Pattern Recognition Letters
year: 2025
bibkey: pariente2025infinity
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.06557'}]
tags: [DATASETS, Evaluation, Distance Metric Learning]
---
Despite the ubiquity of vector search applications, prevailing search algorithms overlook the metric structure of vector embeddings, treating it as a constraint rather than exploiting its underlying properties. In this paper, we demonstrate that in \\(q\\)-metric spaces, metric trees can leverage a stronger version of the triangle inequality to reduce comparisons for exact search. Notably, as \\(q\\) approaches infinity, the search complexity becomes logarithmic. Therefore, we propose a novel projection method that embeds vector datasets with arbitrary dissimilarity measures into \\(q\\)-metric spaces while preserving the nearest neighbor. We propose to learn an approximation of this projection to efficiently transform query points to a space where euclidean distances satisfy the desired properties. Our experimental results with text and image vector embeddings show that learning \\(q\\)-metric approximations enables classic metric tree algorithms -- which typically underperform with high-dimensional data -- to achieve competitive performance against state-of-the-art search methods.