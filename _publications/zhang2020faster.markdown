---
layout: publication
title: Faster Binary Embeddings For Preserving Euclidean Distances
authors: Jinjie Zhang, Rayan Saab
conference: Arxiv
year: 2020
citations: 1
bibkey: zhang2020faster
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.00712'}]
tags: [Tools and Libraries, Evaluation Metrics, Quantization]
---
We propose a fast, distance-preserving, binary embedding algorithm to
transform a high-dimensional dataset \\(\mathcal\{T\}\subseteq\mathbb\{R\}^n\\) into
binary sequences in the cube \\(\\{\pm 1\\}^m\\). When \\(\mathcal\{T\}\\) consists of
well-spread (i.e., non-sparse) vectors, our embedding method applies a stable
noise-shaping quantization scheme to \\(A x\\) where \\(A\in\mathbb\{R\}^\{m\times n\}\\)
is a sparse Gaussian random matrix. This contrasts with most binary embedding
methods, which usually use \\(x\mapsto \mathrm\{sign\}(Ax)\\) for the embedding.
Moreover, we show that Euclidean distances among the elements of \\(\mathcal\{T\}\\)
are approximated by the \\(\ell_1\\) norm on the images of \\(\\{\pm 1\\}^m\\) under a
fast linear transformation. This again contrasts with standard methods, where
the Hamming distance is used instead. Our method is both fast and memory
efficient, with time complexity \\(O(m)\\) and space complexity \\(O(m)\\). Further, we
prove that the method is accurate and its associated error is comparable to
that of a continuous valued Johnson-Lindenstrauss embedding plus a quantization
error that admits a polynomial decay as the embedding dimension \\(m\\) increases.
Thus the length of the binary codes required to achieve a desired accuracy is
quite small, and we show it can even be compressed further without compromising
the accuracy. To illustrate our results, we test the proposed method on natural
images and show that it achieves strong performance.