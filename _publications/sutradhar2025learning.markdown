---
layout: publication
title: Learning Filter-aware Distance Metrics For Nearest Neighbor Search With Multiple
  Filters
authors: Ananya Sutradhar, Suryansh Gupta, Ravishankar Krishnaswamy, Haiyang Xu, Aseem
  Rastogi, Gopal Srinivasa
conference: Arxiv
year: 2025
bibkey: sutradhar2025learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2511.04073'}]
tags: ["Datasets", "Distance Metric Learning", "Graph Based ANN", "Similarity Search", "Tools & Libraries"]
short_authors: Sutradhar et al.
---
Filtered Approximate Nearest Neighbor (ANN) search retrieves the closest vectors for a query vector from a dataset. It enforces that a specified set of discrete labels \(S\) for the query must be included in the labels of each retrieved vector. Existing graph-based methods typically incorporate filter awareness by assigning fixed penalties or prioritizing nodes based on filter satisfaction. However, since these methods use fixed, data in- dependent penalties, they often fail to generalize across datasets with diverse label and vector distributions. In this work, we propose a principled alternative that learns the optimal trade-off between vector distance and filter match directly from the data, rather than relying on fixed penalties. We formulate this as a constrained linear optimization problem, deriving weights that better reflect the underlying filter distribution and more effectively address the filtered ANN search problem. These learned weights guide both the search process and index construction, leading to graph structures that more effectively capture the underlying filter distribution and filter semantics. Our experiments demonstrate that adapting the distance function to the data significantly im- proves accuracy by 5-10% over fixed-penalty methods, providing a more flexible and generalizable framework for the filtered ANN search problem.