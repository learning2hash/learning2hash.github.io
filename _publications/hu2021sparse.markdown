---
layout: publication
title: Sparse Graph Based Sketching For Fast Numerical Linear Algebra
authors: Dong Hu, Shashanka Ubaru, Alex Gittens, Kenneth L. Clarkson, Lior Horesh,
  Vassilis Kalantzis
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2021
bibkey: hu2021sparse
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.05758'}]
tags: ["ICASSP"]
short_authors: Hu et al.
---
In recent years, a variety of randomized constructions of sketching matrices
have been devised, that have been used in fast algorithms for numerical linear
algebra problems, such as least squares regression, low-rank approximation, and
the approximation of leverage scores. A key property of sketching matrices is
that of subspace embedding. In this paper, we study sketching matrices that are
obtained from bipartite graphs that are sparse, i.e., have left degree~s that
is small. In particular, we explore two popular classes of sparse graphs,
namely, expander graphs and magical graphs. For a given subspace \(\mathcal\{U\}
\subseteq \mathbb\{R\}^n\) of dimension \(k\), we show that the magical graph with
left degree \(s=2\) yields a \((1\pm \epsilon)\) \(\{\ell\}_2\)-subspace embedding for
\(\mathcal\{U\}\), if the number of right vertices (the sketch size) \(m =
\mathcal\{O\}(\{k^2\}/\{\epsilon^2\})\). The expander graph with \(s =
\mathcal\{O\}(\{log k\}/\{\epsilon\})\) yields a subspace embedding for \(m =
\mathcal\{O\}(\{k log k\}/\{\epsilon^2\})\). We also discuss the construction of
sparse sketching matrices with reduced randomness using expanders based on
error-correcting codes. Empirical results on various synthetic and real
datasets show that these sparse graph sketching matrices work very well in
practice.