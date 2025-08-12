---
layout: publication
title: Sparse Dimensionality Reduction Revisited
authors: "Mikael M\xF8ller H\xF8gsgaard, Lion Kamma, Kasper Green Larsen, Jelani Nelson,\
  \ Chris Schwiegelshohn"
conference: Arxiv
year: 2023
bibkey: "h\xF8gsgaard2023sparse"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.06165'}]
tags: []
short_authors: "H\xF8gsgaard et al."
---
The sparse Johnson-Lindenstrauss transform is one of the central techniques
in dimensionality reduction. It supports embedding a set of \(n\) points in
\(\mathbb\{R\}^d\) into \(m=O(\epsilon^\{-2\} \lg n)\) dimensions while preserving
all pairwise distances to within \(1 \pm \epsilon\). Each input point \(x\) is
embedded to \(Ax\), where \(A\) is an \(m \times d\) matrix having \(s\) non-zeros per
column, allowing for an embedding time of \(O(s \|x\|_0)\).
  Since the sparsity of \(A\) governs the embedding time, much work has gone into
improving the sparsity \(s\). The current state-of-the-art by Kane and Nelson
(JACM'14) shows that \(s = O(\epsilon ^\{-1\} \lg n)\) suffices. This is almost
matched by a lower bound of \(s = Ω(\epsilon ^\{-1\} \lg
n/\lg(1/\epsilon))\) by Nelson and Nguyen (STOC'13). Previous work thus
suggests that we have near-optimal embeddings.
  In this work, we revisit sparse embeddings and identify a loophole in the
lower bound. Concretely, it requires \(d \geq n\), which in many applications is
unrealistic. We exploit this loophole to give a sparser embedding when \(d =
o(n)\), achieving \(s = O(\epsilon^\{-1\}(\lg n/\lg(1/\epsilon)+\lg^\{2/3\}n
\lg^\{1/3\} d))\). We also complement our analysis by strengthening the lower
bound of Nelson and Nguyen to hold also when \(d \ll n\), thereby matching the
first term in our new sparsity upper bound. Finally, we also improve the
sparsity of the best oblivious subspace embeddings for optimal embedding
dimensionality.