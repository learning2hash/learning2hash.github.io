---
layout: publication
title: Let Them Have CAKES A Cutting-edge Algorithm For Scalable Efficient And Exact Search On Big Data
authors: Prior Morgan E., Howard Thomas J. Iii, Mclaughlin Oliver, Ferguson Terrence, Ishaq Najib, Daniels Noah M.
conference: "Arxiv"
year: 2023
bibkey: prior2023let
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2309.05491"}
tags: ['ARXIV']
---
The ongoing Big Data explosion has created a demand for efficient and scalable algorithms for similarity search. Most recent work has focused on \textit\{approximate\} \{\{ '\{\{' \}\}k\{\{ '\}\}' \}\}-NN search, and while this may be sufficient for some applications, \textit\{exact\} \{\{ '\{\{' \}\}k\{\{ '\}\}' \}\}-NN search would be ideal for many applications. We present CAKES, a set of three novel, exact algorithms for \{\{ '\{\{' \}\}k\{\{ '\}\}' \}\}-NN search. CAKES's algorithms are generic over \textit\{any\} distance function, and they \textit\{do not\} scale with the cardinality or embedding dimension of the dataset, but rather with its metric entropy and fractal dimension. We test these claims on datasets from the ANN-Benchmarks suite under commonly-used distance functions, as well as on a genomic dataset with Levenshtein distance and a radio-frequency dataset with Dynamic Time Warping distance. We demonstrate that CAKES exhibits near-constant scaling with cardinality on data conforming to the manifold hypothesis, and has perfect recall on data in \textit\{metric\} spaces. We also demonstrate that CAKES exhibits significantly higher recall than state-of-the-art \{\{ '\{\{' \}\}k\{\{ '\}\}' \}\}-NN search algorithms when the distance function is not a metric. Additionally, we show that indexing and tuning time for CAKES is an order of magnitude, or more, faster than state-of-the-art approaches. We conclude that CAKES is a highly efficient and scalable algorithm for exact \{\{ '\{\{' \}\}k\{\{ '\}\}' \}\}-NN search on Big Data. We provide a Rust implementation of CAKES.
