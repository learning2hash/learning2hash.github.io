---
layout: publication
title: 'Lower Memory Oblivious (tensor) Subspace Embeddings With Fewer Random Bits:
  Modewise Methods For Least Squares'
authors: M. A. Iwen, D. Needell, E. Rebrova, A. Zare
conference: SIAM Journal on Matrix Analysis and Applications
year: 2021
bibkey: iwen2019lower
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.08294'}]
tags: ["Memory Efficiency"]
short_authors: Iwen et al.
---
In this paper new general modewise Johnson-Lindenstrauss (JL) subspace
embeddings are proposed that are both considerably faster to generate and
easier to store than traditional JL embeddings when working with extremely
large vectors and/or tensors.
  Corresponding embedding results are then proven for two different types of
low-dimensional (tensor) subspaces. The first of these new subspace embedding
results produces improved space complexity bounds for embeddings of rank-\\(r\\)
tensors whose CP decompositions are contained in the span of a fixed (but
unknown) set of \\(r\\) rank-one basis tensors. In the traditional vector setting
this first result yields new and very general near-optimal oblivious subspace
embedding constructions that require fewer random bits to generate than
standard JL embeddings when embedding subspaces of \\(\mathbb\{C\}^N\\) spanned by
basis vectors with special Kronecker structure. The second result proven herein
provides new fast JL embeddings of arbitrary \\(r\\)-dimensional subspaces
\\(\mathcal\{S\} \subset \mathbb\{C\}^N\\) which also require fewer random bits (and so
are easier to store - i.e., require less space) than standard fast JL embedding
methods in order to achieve small \\(\epsilon\\)-distortions. These new oblivious
subspace embedding results work by \\((i)\\) effectively folding any given vector
in \\(\mathcal\{S\}\\) into a (not necessarily low-rank) tensor, and then \\((ii)\\)
embedding the resulting tensor into \\(\mathbb\{C\}^m\\) for \\(m \leq C r log^c(N) /
\epsilon^2\\).
  Applications related to compression and fast compressed least squares
solution methods are also considered, including those used for fitting low-rank
CP decompositions, and the proposed JL embedding results are shown to work well
numerically in both settings.