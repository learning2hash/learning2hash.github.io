---
layout: publication
title: 'Pruning Algorithms For Low-dimensional Non-metric K-nn Search: A Case Study'
authors: Leonid Boytsov, Eric Nyberg
conference: Lecture Notes in Computer Science
year: 2019
bibkey: boytsov2019pruning
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.03539'}]
tags: ["Similarity Search", "Tree Based ANN"]
short_authors: Leonid Boytsov, Eric Nyberg
---
We focus on low-dimensional non-metric search, where tree-based approaches
permit efficient and accurate retrieval while having short indexing time. These
methods rely on space partitioning and require a pruning rule to avoid visiting
unpromising parts. We consider two known data-driven approaches to extend these
rules to non-metric spaces: TriGen and a piece-wise linear approximation of the
pruning rule. We propose and evaluate two adaptations of TriGen to
non-symmetric similarities (TriGen does not support non-symmetric distances).
We also evaluate a hybrid of TriGen and the piece-wise linear approximation
pruning. We find that this hybrid approach is often more effective than either
of the pruning rules. We make our software publicly available.