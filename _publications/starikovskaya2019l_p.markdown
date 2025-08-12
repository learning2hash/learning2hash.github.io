---
layout: publication
title: \(l_p\) Pattern Matching In A Stream
authors: "Tatiana Starikovskaya, Michal Svagerka, Przemys\u0142aw Uzna\u0144ski"
conference: Arxiv
year: 2019
bibkey: starikovskaya2019l_p
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.04405'}]
tags: ["Scalability"]
short_authors: "Tatiana Starikovskaya, Michal Svagerka, Przemys\u0142aw Uzna\u0144\
  ski"
---
We consider the problem of computing distance between a pattern of length \(n\)
and all \(n\)-length subwords of a text in the streaming model. In the streaming
setting, only the Hamming distance (\(L_0\)) has been studied. It is known that
computing the exact Hamming distance between a pattern and a streaming text
requires \(Ω(n)\) space (folklore). Therefore, to develop sublinear-space
solutions, one must relax their requirements. One possibility to do so is to
compute only the distances bounded by a threshold \(k\), see~[SODA'19, Clifford,
Kociumaka, Porat] and references therein. The motivation for this variant of
this problem is that we are interested in subwords of the text that are similar
to the pattern, i.e. in subwords such that the distance between them and the
pattern is relatively small. On the other hand, the main application of the
streaming setting is processing large-scale data, such as biological data.
Recent advances in hardware technology allow generating such data at a very
high speed, but unfortunately, the produced data may contain about 10% of
noise~[Biol. Direct.'07, Klebanov and Yakovlev]. To analyse such data, it is
not sufficient to consider small distances only. A possible workaround for this
issue is the \((1\pm\epsilon)\)-approximation. This line of research was
initiated in [ICALP'16, Clifford and Starikovskaya] who gave a
\((1\pm\epsilon)\)-approximation algorithm with
space~\(\tilde\{O\}(\epsilon^\{-5\}\sqrt\{n\})\). In this work, we show a suite of
new streaming algorithms for computing the Hamming, \(L_1\), \(L_2\) and general
\(L_p\) (\(0 < p < 2\)) distances between the pattern and the text. Our results
significantly extend over the previous result in this setting. In particular,
for the Hamming distance and for the \(L_p\) distance when \(0 < p \le 1\) we show
a streaming algorithm that uses \(\tilde\{O\}(\epsilon^\{-2\}\sqrt\{n\})\) space for
polynomial-size alphabets.