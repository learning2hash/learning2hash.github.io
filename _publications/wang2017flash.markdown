---
layout: publication
title: FLASH Randomized Algorithms Accelerated Over CPU-GPU For Ultra-high Dimensional Similarity Search
authors: Wang Yiqiu, Shrivastava Anshumali, Wang Jonathan, Ryu Junghee
conference: "Arxiv"
year: 2017
bibkey: wang2017flash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1709.01190"}
tags: ['ARXIV', 'Graph', 'Independent', 'LSH']
---
<p>We present FLASH (ast SH lgorithm for imilarity search accelerated
with PC), a similarity search system for ultra-high dimensional datasets
on a single machine, that does not require similarity computations and
is tailored for high-performance computing platforms. By leveraging a
LSH style randomized indexing procedure and combining it with several
principled techniques, such as reservoir sampling, recent advances in
one-pass minwise hashing, and count based estimations, we reduce the
computational and parallelization costs of similarity search, while
retaining sound theoretical guarantees. We evaluate FLASH on several
real, high-dimensional datasets from different domains, including text,
malicious URL, click-through prediction, social networks, etc. Our
experiments shed new light on the difficulties associated with datasets
having several million dimensions. Current state-of-the-art
implementations either fail on the presented scale or are orders of
magnitude slower than FLASH. FLASH is capable of computing an
approximate k-NN graph, from scratch, over the full webspam dataset (1.3
billion nonzeros) in less than 10 seconds. Computing a full k-NN graph
in less than 10 seconds on the webspam dataset, using brute-force (<span
class="math inline">\(n^2D\)</span>), will require at least 20
teraflops. We provide CPU and GPU implementations of FLASH for
replicability of our results.</p>
