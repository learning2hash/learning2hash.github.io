---
layout: publication
title: Improving Code Example Recommendations On Informal Documentation Using BERT And Query-aware LSH A Comparative Study
authors: Rahmani Sajjad, Naghshzan Amirhossein, Guerrouj Latifa
conference: "Arxiv"
year: 2023
bibkey: rahmani2023improving
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2305.03017"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Our research investigates the recommendation of code examples to aid software
developers, a practice that saves developers significant time by providing
ready-to-use code snippets. The focus of our study is Stack Overflow, a
commonly used resource for coding discussions and solutions, particularly in
the context of the Java programming language. We applied BERT, a powerful Large
Language Model (LLM) that enables us to transform code examples into numerical
vectors by extracting their semantic information. Once these numerical
representations are prepared, we identify Approximate Nearest Neighbors (ANN)
using Locality-Sensitive Hashing (LSH). Our research employed two variants of
LSH: Random Hyperplane-based LSH and Query-Aware LSH. We rigorously compared
these two approaches across four parameters: HitRate, Mean Reciprocal Rank
(MRR), Average Execution Time, and Relevance. Our study revealed that the
Query-Aware (QA) approach showed superior performance over the Random
Hyperplane-based (RH) method. Specifically, it exhibited a notable improvement
of 20\% to 35\% in HitRate for query pairs compared to the RH approach.
Furthermore, the QA approach proved significantly more time-efficient, with its
speed in creating hashing tables and assigning data samples to buckets being at
least four times faster. It can return code examples within milliseconds,
whereas the RH approach typically requires several seconds to recommend code
examples. Due to the superior performance of the QA approach, we tested it
against PostFinder and FaCoY, the state-of-the-art baselines. Our QA method
showed comparable efficiency proving its potential for effective code
recommendation.
