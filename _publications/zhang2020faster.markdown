---
layout: publication
title: Faster Binary Embeddings For Preserving Euclidean Distances
authors: Zhang Jinjie, Saab Rayan
conference: "Arxiv"
year: 2020
bibkey: zhang2020faster
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2010.00712"}
tags: ['ARXIV', 'Independent', 'Quantisation']
---
<p>We propose a fast, distance-preserving, binary embedding algorithm to
transform a high-dimensional dataset <span
class="math inline">\(\mathcal{T}\subseteq\mathbb{R}^n\)</span> into
binary sequences in the cube <span class="math inline">\(\{\pm
1\}^m\)</span>. When <span class="math inline">\(\mathcal{T}\)</span>
consists of well-spread (i.e., non-sparse) vectors, our embedding method
applies a stable noise-shaping quantization scheme to <span
class="math inline">\(A x\)</span> where <span
class="math inline">\(A\in\mathbb{R}^{m\times n}\)</span> is a sparse
Gaussian random matrix. This contrasts with most binary embedding
methods, which usually use <span class="math inline">\(x\mapsto
\mathrm{sign}(Ax)\)</span> for the embedding. Moreover, we show that
Euclidean distances among the elements of <span
class="math inline">\(\mathcal{T}\)</span> are approximated by the <span
class="math inline">\(\ell_1\)</span> norm on the images of <span
class="math inline">\(\{\pm 1\}^m\)</span> under a fast linear
transformation. This again contrasts with standard methods, where the
Hamming distance is used instead. Our method is both fast and memory
efficient, with time complexity <span
class="math inline">\(O(m)\)</span> and space complexity <span
class="math inline">\(O(m)\)</span>. Further, we prove that the method
is accurate and its associated error is comparable to that of a
continuous valued Johnson-Lindenstrauss embedding plus a quantization
error that admits a polynomial decay as the embedding dimension <span
class="math inline">\(m\)</span> increases. Thus the length of the
binary codes required to achieve a desired accuracy is quite small, and
we show it can even be compressed further without compromising the
accuracy. To illustrate our results, we test the proposed method on
natural images and show that it achieves strong performance.</p>
