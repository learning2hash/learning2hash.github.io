---
layout: publication
title: 'Binary Embedding: Fundamental Limits And Fast Algorithm'
authors: Yi Xinyang, Caramanis Constantine, Price Eric
conference: Arxiv
year: 2015
bibkey: yi2015binary
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.05746'}]
tags: ["Compact Codes", "Efficiency", "Hashing Methods", "Quantization", "Similarity Search"]
short_authors: Yi Xinyang, Caramanis Constantine, Price Eric
---
Binary embedding is a nonlinear dimension reduction methodology where high
dimensional data are embedded into the Hamming cube while preserving the
structure of the original space. Specifically, for an arbitrary \\(N\\) distinct
points in \\(\mathbb\{S\}^\{p-1\}\\), our goal is to encode each point using
\\(m\\)-dimensional binary strings such that we can reconstruct their geodesic
distance up to \\(\delta\\) uniform distortion. Existing binary embedding
algorithms either lack theoretical guarantees or suffer from running time
\\(O\big(mp\big)\\). We make three contributions: (1) we establish a lower bound
that shows any binary embedding oblivious to the set of points requires \\(m =
Ω(\frac\{1\}\{\delta^2\}log\{N\})\\) bits and a similar lower bound for
non-oblivious embeddings into Hamming distance; (2) [DELETED, see comment]; (3)
we also provide an analytic result about embedding a general set of points \\(K
\subseteq \mathbb\{S\}^\{p-1\}\\) with even infinite size. Our theoretical findings
are supported through experiments on both synthetic and real data sets.