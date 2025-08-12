---
layout: publication
title: Improved Sublinear-time Edit Distance For Preprocessed Strings
authors: Karl Bringmann, Alejandro Cassis, Nick Fischer, Vasileios Nakos
conference: Arxiv
year: 2022
bibkey: bringmann2022improved
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.14137'}]
tags: ["Efficiency"]
short_authors: Bringmann et al.
---
We study the problem of approximating the edit distance of two strings in
sublinear time, in a setting where one or both string(s) are preprocessed, as
initiated by Goldenberg, Rubinstein, Saha (STOC '20). Specifically, in the \((k,
K)\)-gap edit distance problem, the goal is to distinguish whether the edit
distance of two strings is at most \(k\) or at least \(K\). We obtain the following
results:
  * After preprocessing one string in time \(n^\{1+o(1)\}\), we can solve \((k, k
\cdot n^\{o(1)\})\)-gap edit distance in time \((n/k + k) \cdot n^\{o(1)\}\).
  * After preprocessing both strings separately in time \(n^\{1+o(1)\}\), we can
solve \((k, k \cdot n^\{o(1)\})\)-gap edit distance in time \(k \cdot n^\{o(1)\}\).
  Both results improve upon some previously best known result, with respect to
either the gap or the query time or the preprocessing time.
  Our algorithms build on the framework by Andoni, Krauthgamer and Onak (FOCS
'10) and the recent sublinear-time algorithm by Bringmann, Cassis, Fischer and
Nakos (STOC '22). We replace many complicated parts in their algorithm by
faster and simpler solutions which exploit the preprocessing.