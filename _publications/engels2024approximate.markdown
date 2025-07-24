---
layout: publication
title: Approximate Nearest Neighbor Search With Window Filters
authors: Joshua Engels, Benjamin Landrum, Shangdi Yu, Laxman Dhulipala, Julian Shun
conference: Arxiv
year: 2024
bibkey: engels2024approximate
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.00943'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Tools & Libraries", "Tree Based ANN"]
short_authors: Engels et al.
---
We define and investigate the problem of \\(\textit\{c-approximate window
search\}\\): approximate nearest neighbor search where each point in the dataset
has a numeric label, and the goal is to find nearest neighbors to queries
within arbitrary label ranges. Many semantic search problems, such as image and
document search with timestamp filters, or product search with cost filters,
are natural examples of this problem. We propose and theoretically analyze a
modular tree-based framework for transforming an index that solves the
traditional c-approximate nearest neighbor problem into a data structure that
solves window search. On standard nearest neighbor benchmark datasets equipped
with random label values, adversarially constructed embeddings, and image
search embeddings with real timestamps, we obtain up to a \\(75\times\\) speedup
over existing solutions at the same level of recall.