---
layout: publication
title: The Vc-dimension Of Similarity Hypotheses Spaces
authors: Mark Herbster, Paul Rubenstein, James Townsend
conference: Arxiv
year: 2015
bibkey: herbster2015vc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.07143'}]
tags: ["Distance Metric Learning", "Similarity Search"]
short_authors: Mark Herbster, Paul Rubenstein, James Townsend
---
Given a set \(X\) and a function \(h:X\longrightarrow\\{0,1\\}\) which labels each
element of \(X\) with either \(0\) or \(1\), we may define a function \(h^\{(s)\}\) to
measure the similarity of pairs of points in \(X\) according to \(h\).
Specifically, for \(h\in \\{0,1\\}^X\) we define \(h^\{(s)\}\in \\{0,1\\}^\{X\times X\}\)
by \(h^\{(s)\}(w,x):= \mathbb\{1\}[h(w) = h(x)]\). This idea can be extended to a set
of functions, or hypothesis space \(\mathcal\{H\} \subseteq \\{0,1\\}^X\) by defining
a similarity hypothesis space \(\mathcal\{H\}^\{(s)\}:=\\{h^\{(s)\}:h\in\mathcal\{H\}\\}\).
We show that \(\{\{vc-dimension\}\}(\mathcal\{H\}^\{(s)\}) \in
\Theta(\{\{vc-dimension\}\}(\mathcal\{H\}))\).