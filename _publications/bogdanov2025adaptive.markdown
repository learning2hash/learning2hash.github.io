---
layout: publication
title: Adaptive Robustness Of Hypergrid Johnson-lindenstrauss
authors: Andrej Bogdanov, Alon Rosen, Neekon Vafa, Vinod Vaikuntanathan
conference: Arxiv
year: 2025
bibkey: bogdanov2025adaptive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.09331'}]
tags: ["Hashing Methods", "Robustness"]
short_authors: Bogdanov et al.
---
Johnson and Lindenstrauss (Contemporary Mathematics, 1984) showed that for \(n
> m\), a scaled random projection \(\mathbf\{A\}\) from \(\mathbb\{R\}^n\) to
\(\mathbb\{R\}^m\) is an approximate isometry on any set \(S\) of size at most
exponential in \(m\). If \(S\) is larger, however, its points can contract
arbitrarily under \(\mathbf\{A\}\). In particular, the hypergrid \(([-B, B] \cap
\mathbb\{Z\})^n\) is expected to contain a point that is contracted by a factor of
\(\kappa_\{\mathsf\{stat\}\} = \Theta(B)^\{-1/\alpha\}\), where \(\alpha = m/n\).
  We give evidence that finding such a point exhibits a
statistical-computational gap precisely up to \(\kappa_\{\mathsf\{comp\}\} =
\widetilde\{\Theta\}(\sqrt\{\alpha\}/B)\). On the algorithmic side, we design an
online algorithm achieving \(\kappa_\{\mathsf\{comp\}\}\), inspired by a discrepancy
minimization algorithm of Bansal and Spencer (Random Structures & Algorithms,
2020). On the hardness side, we show evidence via a multiple overlap gap
property (mOGP), which in particular captures online algorithms; and a
reduction-based lower bound, which shows hardness under standard worst-case
lattice assumptions.
  As a cryptographic application, we show that the rounded
Johnson-Lindenstrauss embedding is a robust property-preserving hash function
(Boyle, Lavigne and Vaikuntanathan, TCC 2019) on the hypergrid for the
Euclidean metric in the computationally hard regime. Such hash functions
compress data while preserving \(ℓ₂\) distances between inputs up to some
distortion factor, with the guarantee that even knowing the hash function, no
computationally bounded adversary can find any pair of points that violates the
distortion bound.