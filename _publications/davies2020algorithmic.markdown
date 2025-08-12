---
layout: publication
title: An Algorithmic Framework For Colouring Locally Sparse Graphs
authors: "Ewan Davies, Ross J. Kang, Fran\xE7ois Pirot, Jean-S\xE9bastien Sereni"
conference: Arxiv
year: 2020
bibkey: davies2020algorithmic
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.07151'}]
tags: []
short_authors: Davies et al.
---
We develop an algorithmic framework for graph colouring that reduces the
problem to verifying a local probabilistic property of the independent sets.
  With this we give, for any fixed \(k\ge 3\) and \(\epsilon>0\), a randomised
polynomial-time algorithm for colouring graphs of maximum degree \(\Delta\) in
which each vertex is contained in at most \(t\) copies of a cycle of length \(k\),
where \(1/2\le t\le \Delta^\frac\{2\epsilon\}\{1+2\epsilon\}/(log\Delta)^2\),
with \(\lfloor(1+\epsilon)\Delta/log(\Delta/\sqrt t)\rfloor\) colours.
  This generalises and improves upon several notable results including those of
Kim (1995) and Alon, Krivelevich and Sudakov (1999), and more recent ones of
Molloy (2019) and Achlioptas, Iliopoulos and Sinclair (2019). This bound on the
chromatic number is tight up to an asymptotic factor \(2\) and it coincides with
a famous algorithmic barrier to colouring random graphs.