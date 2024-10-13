---
layout: publication
title: Hashing Embeddings Of Optimal Dimension With Applications To Linear Least Squares
authors: Cartis Coralia, Fiala Jan, Shao Zhen
conference: "Arxiv"
year: 2021
bibkey: cartis2021hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.11815"}
tags: ['ARXIV', 'Independent']
---
<p>The aim of this paper is two-fold: firstly, to present subspace
embedding properties for <span class="math inline">\(s\)</span>-hashing
sketching matrices, with <span class="math inline">\(s\geq 1\)</span>,
that are optimal in the projection dimension <span
class="math inline">\(m\)</span> of the sketch, namely, <span
class="math inline">\(m=\mathcal{O}(d)\)</span>, where <span
class="math inline">\(d\)</span> is the dimension of the subspace. A
diverse set of results are presented that address the case when the
input matrix has sufficiently low coherence (thus removing the <span
class="math inline">\(\log^2 d\)</span> factor dependence in <span
class="math inline">\(m\)</span>, in the low-coherence result of
Bourgain et al (2015) at the expense of a smaller coherence
requirement); how this coherence changes with the number <span
class="math inline">\(s\)</span> of column nonzeros (allowing a scaling
of <span class="math inline">\(\sqrt{s}\)</span> of the coherence
bound), or is reduced through suitable transformations (when considering
hashed – instead of subsampled – coherence reducing transformations such
as randomised Hadamard). Secondly, we apply these general hashing
sketching results to the special case of Linear Least Squares (LLS), and
develop Ski-LLS, a generic software package for these problems, that
builds upon and improves the Blendenpik solver on dense input and the
(sequential) LSRN performance on sparse problems. In addition to the
hashing sketching improvements, we add suitable linear algebra tools for
rank-deficient and for sparse problems that lead Ski-LLS to outperform
not only sketching-based routines on randomly generated input, but also
state of the art direct solver SPQR and iterative code HSL on certain
subsets of the sparse Florida matrix collection; namely, on least
squares problems that are significantly overdetermined, or moderately
sparse, or difficult.</p>
