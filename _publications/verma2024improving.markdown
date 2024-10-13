---
layout: publication
title: Improving LSH Via Tensorized Random Projection
authors: Verma Bhisham Dev, Pratap Rameshwar
conference: "Arxiv"
year: 2024
bibkey: verma2024improving
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2402.07189"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>Locality sensitive hashing (LSH) is a fundamental algorithmic toolkit
used by data scientists for approximate nearest neighbour search
problems that have been used extensively in many large scale data
processing applications such as near duplicate detection, nearest
neighbour search, clustering, etc. In this work, we aim to propose
faster and space efficient locality sensitive hash functions for
Euclidean distance and cosine similarity for tensor data. Typically, the
naive approach for obtaining LSH for tensor data involves first
reshaping the tensor into vectors, followed by applying existing LSH
methods for vector data <span class="math inline">\(E2LSH\)</span> and
<span class="math inline">\(SRP\)</span>. However, this approach becomes
impractical for higher order tensors because the size of the reshaped
vector becomes exponential in the order of the tensor. Consequently, the
size of LSH parameters increases exponentially. To address this problem,
we suggest two methods for LSH for Euclidean distance and cosine
similarity, namely <span class="math inline">\(CP-E2LSH\)</span>, <span
class="math inline">\(TT-E2LSH\)</span>, and <span
class="math inline">\(CP-SRP\)</span>, <span
class="math inline">\(TT-SRP\)</span>, respectively, building on <span
class="math inline">\(CP\)</span> and tensor train <span
class="math inline">\((TT)\)</span> decompositions techniques. Our
approaches are space efficient and can be efficiently applied to low
rank <span class="math inline">\(CP\)</span> or <span
class="math inline">\(TT\)</span> tensors. We provide a rigorous
theoretical analysis of our proposal on their correctness and
efficacy.</p>
