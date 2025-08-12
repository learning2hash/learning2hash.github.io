---
layout: publication
title: Terminal Embeddings
authors: Michael Elkin, Arnold Filtser, Ofer Neiman
conference: Theoretical Computer Science
year: 2017
bibkey: elkin2016terminal
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.02321'}]
tags: []
short_authors: Michael Elkin, Arnold Filtser, Ofer Neiman
---
In this paper we study \{\em terminal embeddings\}, in which one is given a
finite metric \\((X,d_X)\\) (or a graph \\(G=(V,E)\\)) and a subset \\(K \subseteq X\\) of
its points are designated as \{\em terminals\}. The objective is to embed the
metric into a normed space, while approximately preserving all distances among
pairs that contain a terminal. We devise such embeddings in various settings,
and conclude that even though we have to preserve \\(\approx|K|\cdot |X|\\) pairs,
the distortion depends only on \\(|K|\\), rather than on \\(|X|\\).
  We also strengthen this notion, and consider embeddings that approximately
preserve the distances between \{\em all\} pairs, but provide improved distortion
for pairs containing a terminal. Surprisingly, we show that such embeddings
exist in many settings, and have optimal distortion bounds both with respect to
\\(X \times X\\) and with respect to \\(K \times X\\).
  Moreover, our embeddings have implications to the areas of Approximation and
Online Algorithms. In particular, [ALN08] devised an \\(\tilde\{O\}(\sqrt\{log
r\})\\)-approximation algorithm for sparsest-cut instances with \\(r\\) demands.
Building on their framework, we provide an \\(\tilde\{O\}(\sqrt\{log
|K|\})\\)-approximation for sparsest-cut instances in which each demand is
incident on one of the vertices of \\(K\\) (aka, terminals). Since \\(|K| \le r\\), our
bound generalizes that of [ALN08].