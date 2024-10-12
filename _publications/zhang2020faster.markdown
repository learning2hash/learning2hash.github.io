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
We propose a fast, distance-preserving, binary embedding algorithm to transform a high-dimensional dataset \{&#37; raw &#37;\}\\(\mathcal\{T\}\subseteq\mathbb\{R\}^n\\)\{&#37; endraw &#37;\} into binary sequences in the cube \{&#37; raw &#37;\}\\(\\{\pm 1\\}^m\\)\{&#37; endraw &#37;\}. When \{&#37; raw &#37;\}\\(\mathcal\{T\}\\)\{&#37; endraw &#37;\} consists of well-spread (i.e., non-sparse) vectors, our embedding method applies a stable noise-shaping quantization scheme to \{&#37; raw &#37;\}\\(A x\\)\{&#37; endraw &#37;\} where \{&#37; raw &#37;\}\\(A\in\mathbb\{R\}^\{m\times n\}\\)\{&#37; endraw &#37;\} is a sparse Gaussian random matrix. This contrasts with most binary embedding methods, which usually use \{&#37; raw &#37;\}\\(x\mapsto \mathrm\{sign\}(Ax)\\)\{&#37; endraw &#37;\} for the embedding. Moreover, we show that Euclidean distances among the elements of \{&#37; raw &#37;\}\\(\mathcal\{T\}\\)\{&#37; endraw &#37;\} are approximated by the \{&#37; raw &#37;\}\\(\ell\_1\\)\{&#37; endraw &#37;\} norm on the images of \{&#37; raw &#37;\}\\(\\{\pm 1\\}^m\\)\{&#37; endraw &#37;\} under a fast linear transformation. This again contrasts with standard methods, where the Hamming distance is used instead. Our method is both fast and memory efficient, with time complexity \{&#37; raw &#37;\}\\(O(m)\\)\{&#37; endraw &#37;\} and space complexity \{&#37; raw &#37;\}\\(O(m)\\)\{&#37; endraw &#37;\}. Further, we prove that the method is accurate and its associated error is comparable to that of a continuous valued Johnson-Lindenstrauss embedding plus a quantization error that admits a polynomial decay as the embedding dimension \{&#37; raw &#37;\}\\(m\\)\{&#37; endraw &#37;\} increases. Thus the length of the binary codes required to achieve a desired accuracy is quite small, and we show it can even be compressed further without compromising the accuracy. To illustrate our results, we test the proposed method on natural images and show that it achieves strong performance.
