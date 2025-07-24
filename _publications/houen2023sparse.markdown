---
layout: publication
title: A Sparse Johnson-lindenstrauss Transform Using Fast Hashing
authors: "Jakob B\xE6k Tejs Houen, Mikkel Thorup"
conference: Arxiv
year: 2023
bibkey: houen2023sparse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03110'}]
tags: ["Evaluation", "Hashing Methods"]
short_authors: "Jakob B\xE6k Tejs Houen, Mikkel Thorup"
---
The *Sparse Johnson-Lindenstrauss Transform* of Kane and Nelson (SODA
2012) provides a linear dimensionality-reducing map \\(A \in \mathbb\{R\}^\{m \times
u\}\\) in \\(ℓ₂\\) that preserves distances up to distortion of \\(1 + \epsilon\\)
with probability \\(1 - \delta\\), where \\(m = O(\epsilon^\{-2\} log 1/\delta)\\)
and each column of \\(A\\) has \\(O(\epsilon m)\\) non-zero entries. The previous
analyses of the Sparse Johnson-Lindenstrauss Transform all assumed access to a
\\(Ω(log 1/\delta)\\)-wise independent hash function. The main contribution
of this paper is a more general analysis of the Sparse Johnson-Lindenstrauss
Transform with less assumptions on the hash function. We also show that the
*Mixed Tabulation hash function* of Dahlgaard, Knudsen, Rotenberg, and
Thorup (FOCS 2015) satisfies the conditions of our analysis, thus giving us the
first analysis of a Sparse Johnson-Lindenstrauss Transform that works with a
practical hash function.