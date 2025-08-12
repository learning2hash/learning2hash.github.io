---
layout: publication
title: Vectorized Character Counting For Faster Pattern Matching
authors: Roman Snytsar
conference: Proceedings of the 12th International Joint Conference on Biomedical Engineering
  Systems and Technologies
year: 2019
bibkey: snytsar2018vectorized
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.06127'}]
tags: []
short_authors: Roman Snytsar
---
Many modern sequence alignment tools implement fast string matching using the
space efficient data structure called FM-index. The succinct nature of this
data structure presents unique challenges for the algorithm designers. In this
paper, we explore the opportunities for parallelization of the exact and
inexact matches and present an efficient SIMD solution for the Occ portion of
the algorithm. Our implementation computes all eight Occ values required for
the inexact match algorithm step in a single pass. We showcase the algorithm
performance in a multi-core genome aligner and discuss effects of the memory
prefetch.