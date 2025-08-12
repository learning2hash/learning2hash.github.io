---
layout: publication
title: 'Xisort: Deterministic Sorting Via IEEE-754 Total Ordering And Entropy Minimization'
authors: Faruk Alpay
conference: Arxiv
year: 2025
bibkey: alpay2025xisort
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.11927'}]
tags: ["Tools & Libraries"]
short_authors: Faruk Alpay
---
We introduce XiSort, a deterministic and reproducible sorting algorithm for floating-point sequences based on IEEE-754 total ordering and entropy minimization. XiSort guarantees bit-for-bit stability across runs and platforms by resolving tie-breaking via information-theoretic and symbolic methods. The algorithm supports both in-memory and external (out-of-core) operation, offering consistent performance on large datasets. We formalize a curved variant of the sorting metric that integrates into the Alpay Algebra framework, treating XiSort as a recursive operator with provable convergence and symbolic idempotence. This model preserves state-space closure while minimizing local disorder, interpretable as symbolic entropy. Empirical benchmarks demonstrate that XiSort achieves competitive throughput (e.g., sorting 10^8 doubles in approximately 12 seconds in-memory, and 100 GB at around 100 MB/s on SSDs), with applications in scientific computing, high-frequency finance, and reproducible numerical workflows. The results position XiSort as a principled tool for stable data alignment, symbolic preprocessing, and cross-platform float ordering.
  Keywords: deterministic sorting, IEEE-754, entropy minimization, symbolic algebra, reproducibility, external memory, Alpay Algebra, data pipelines