---
layout: publication
title: Utilizing Low-dimensional Molecular Embeddings For Rapid Chemical Similarity
  Search
authors: Kathryn E. Kirchoff, James Wellnitz, Joshua E. Hochuli, Travis Maxfield,
  Konstantin I. Popov, Shawn Gomez, Alexander Tropsha
conference: Lecture Notes in Computer Science
year: 2024
bibkey: kirchoff2024utilizing
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.07970'}]
tags: ["Datasets", "Evaluation", "Similarity Search", "Tools & Libraries"]
short_authors: Kirchoff et al.
---
Nearest neighbor-based similarity searching is a common task in chemistry,
with notable use cases in drug discovery. Yet, some of the most commonly used
approaches for this task still leverage a brute-force approach. In practice
this can be computationally costly and overly time-consuming, due in part to
the sheer size of modern chemical databases. Previous computational
advancements for this task have generally relied on improvements to hardware or
dataset-specific tricks that lack generalizability. Approaches that leverage
lower-complexity searching algorithms remain relatively underexplored. However,
many of these algorithms are approximate solutions and/or struggle with typical
high-dimensional chemical embeddings. Here we evaluate whether a combination of
low-dimensional chemical embeddings and a k-d tree data structure can achieve
fast nearest neighbor queries while maintaining performance on standard
chemical similarity search benchmarks. We examine different dimensionality
reductions of standard chemical embeddings as well as a learned,
structurally-aware embedding -- SmallSA -- for this task. With this framework,
searches on over one billion chemicals execute in less than a second on a
single CPU core, five orders of magnitude faster than the brute-force approach.
We also demonstrate that SmallSA achieves competitive performance on chemical
similarity benchmarks.