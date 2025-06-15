---
layout: publication
title: 'Improving LSH Via Tensorized Random Projection'
authors: Bhisham Dev Verma, Rameshwar Pratap
conference: "Arxiv"
year: 2024
citations: 0
bibkey: verma2024improving
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2402.07189'}
tags: ['Independent', 'Unimodal', 'Shallow', 'Hashing', 'Applications']
---
Locality sensitive hashing (LSH) is a fundamental algorithmic toolkit used by
data scientists for approximate nearest neighbour search problems that have
been used extensively in many large scale data processing applications such as
near duplicate detection, nearest neighbour search, clustering, etc. In this
work, we aim to propose faster and space efficient locality sensitive hash
functions for Euclidean distance and cosine similarity for tensor data.
Typically, the naive approach for obtaining LSH for tensor data involves first
reshaping the tensor into vectors, followed by applying existing LSH methods
for vector data \\(E2LSH\\) and \\(SRP\\). However, this approach becomes impractical
for higher order tensors because the size of the reshaped vector becomes
exponential in the order of the tensor. Consequently, the size of LSH
parameters increases exponentially. To address this problem, we suggest two
methods for LSH for Euclidean distance and cosine similarity, namely
\\(CP-E2LSH\\), \\(TT-E2LSH\\), and \\(CP-SRP\\), \\(TT-SRP\\), respectively, building on \\(CP\\)
and tensor train \\((TT)\\) decompositions techniques. Our approaches are space
efficient and can be efficiently applied to low rank \\(CP\\) or \\(TT\\) tensors. We
provide a rigorous theoretical analysis of our proposal on their correctness
and efficacy.
