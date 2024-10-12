---
layout: publication
title: Deskew-lsh Based Code-to-code Recommendation Engine
authors: Silavong Fran, Moran, Georgiadis, Saphal, Otter
conference: "Arxiv"
year: 2024
bibkey: silavong2024deskew
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2111.04473"}
tags: ['ARXIV', 'Deep Learning', 'Independent', 'LSH']
---
Machine learning on source code (MLOnCode) is a popular research field that has been driven by the availability of large-scale code repositories and the development of powerful probabilistic and deep learning models for mining source code. Code-to-code recommendation is a task in MLOnCode that aims to recommend relevant, diverse and concise code snippets that usefully extend the code currently being written by a developer in their development environment (IDE). Code-to-code recommendation engines hold the promise of increasing developer productivity by reducing context switching from the IDE and increasing code-reuse. Existing code-to-code recommendation engines do not scale gracefully to large codebases, exhibiting a linear growth in query time as the code repository increases in size. In addition, existing code-to-code recommendation engines fail to account for the global statistics of code repositories in the ranking function, such as the distribution of code snippet lengths, leading to sub-optimal retrieval results. We address both of these weaknesses with \emph&amp;\#123;Senatus&amp;\#125;, a new code-to-code recommendation engine. At the core of Senatus is \emph&amp;\#123;De-Skew&amp;\#125; LSH a new locality sensitive hashing (LSH) algorithm that indexes the data for fast (sub-linear time) retrieval while also counteracting the skewness in the snippet length distribution using novel abstract syntax tree-based feature scoring and selection algorithms. We evaluate Senatus via automatic evaluation and with an expert developer user study and find the recommendations to be of higher quality than competing baselines, while achieving faster search. For example, on the CodeSearchNet dataset we show that Senatus improves performance by 6.7&#37; F1 and query time 16x is faster compared to Facebook Aroma on the task of code-to-code recommendation.
