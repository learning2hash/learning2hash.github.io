---
layout: publication
title: Constructing Minimal Perfect Hash Functions Using SAT Technology
authors: Sean Weaver, Marijn Heule
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: weaver2019constructing
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.10099'}]
tags: ["AAAI", "Hashing Methods"]
short_authors: Sean Weaver, Marijn Heule
---
Minimal perfect hash functions (MPHFs) are used to provide efficient access
to values of large dictionaries (sets of key-value pairs). Discovering new
algorithms for building MPHFs is an area of active research, especially from
the perspective of storage efficiency. The information-theoretic limit for
MPHFs is 1/(ln 2) or roughly 1.44 bits per key. The current best practical
algorithms range between 2 and 4 bits per key. In this article, we propose two
SAT-based constructions of MPHFs. Our first construction yields MPHFs near the
information-theoretic limit. For this construction, current state-of-the-art
SAT solvers can handle instances where the dictionaries contain up to 40
elements, thereby outperforming the existing (brute-force) methods. Our second
construction uses XOR-SAT filters to realize a practical approach with
long-term storage of approximately 1.83 bits per key.