---
layout: publication
title: 'Revisiting \(k\)-nearest Neighbor Graph Construction On High-dimensional Data
  : Experiments And Analyses'
authors: Liu Yingfan, Cheng Hong, Cui Jiangtao
conference: Arxiv
year: 2021
bibkey: yingfan2021revisiting
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.02234'}]
tags: [Evaluation, Tools & Libraries, Similarity Search, Graph-based ANN]
short_authors: Liu Yingfan, Cheng Hong, Cui Jiangtao
---
The \(k\)-nearest neighbor graph (KNNG) on high-dimensional data is a data
structure widely used in many applications such as similarity search, dimension
reduction and clustering. Due to its increasing popularity, several methods
under the same framework have been proposed in the past decade. This framework
contains two steps, i.e. building an initial KNNG (denoted as \texttt\{INIT\})
and then refining it by neighborhood propagation (denoted as \texttt\{NBPG\}).
However, there remain several questions to be answered. First, it lacks a
comprehensive experimental comparison among representative solutions in the
literature. Second, some recently proposed indexing structures, e.g., SW and
HNSW, have not been used or tested for building an initial KNNG. Third, the
relationship between the data property and the effectiveness of \texttt\{NBPG\}
is still not clear. To address these issues, we comprehensively compare the
representative approaches on real-world high-dimensional data sets to provide
practical and insightful suggestions for users. As the first attempt, we take
SW and HNSW as the alternatives of \texttt\{INIT\} in our experiments. Moreover,
we investigate the effectiveness of \texttt\{NBPG\} and find the strong
correlation between the huness phenomenon and the performance of \texttt\{NBPG\}.