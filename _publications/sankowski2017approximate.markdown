---
layout: publication
title: Approximate Nearest Neighbors Search Without False Negatives For \(l_2\) For
  \(c>\sqrt{\log\log{n}}\)
authors: Sankowski Piotr, Wygocki Piotr
conference: Arxiv
year: 2017
bibkey: sankowski2017approximate
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.06395'}]
tags: ["Efficiency", "Large-Scale Search", "Scalability", "Similarity Search"]
short_authors: Sankowski Piotr, Wygocki Piotr
---
In this paper, we report progress on answering the open problem presented by
Pagh~[14], who considered the nearest neighbor search without false negatives
for the Hamming distance. We show new data structures for solving the
\\(c\\)-approximate nearest neighbors problem without false negatives for Euclidean
high dimensional space \\(\mathcal\{R\}^d\\). These data structures work for any \\(c =
\omega(\sqrt\{log\{log\{n\}\}\})\\), where \\(n\\) is the number of points in the input
set, with poly-logarithmic query time and polynomial preprocessing time. This
improves over the known algorithms, which require \\(c\\) to be \\(Ω(\sqrt\{d\})\\).
  This improvement is obtained by applying a sequence of reductions, which are
interesting on their own. First, we reduce the problem to \\(d\\) instances of
dimension logarithmic in \\(n\\). Next, these instances are reduced to a number of
\\(c\\)-approximate nearest neighbor search instances in \\(\big(\mathbb\{R\}^k\big)^L\\)
space equipped with metric \\(m(x,y) = \max_\{1 \le i \le L\}(\lVert x_i -
y_i\rVert_2)\\).