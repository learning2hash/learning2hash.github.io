---
layout: publication
title: A Sparse Johnson-lindenstrauss Transform Using Fast Hashing
authors: Houen Jakob Bæk Tejs, Thorup Mikkel
conference: "Arxiv"
year: 2023
bibkey: houen2023sparse
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2305.03110"}
tags: ['ARXIV', 'FOCS', 'Independent']
---
The \emph&amp;\#123;Sparse Johnson-Lindenstrauss Transform&amp;\#125; of Kane and Nelson (SODA 2012) provides a linear dimensionality-reducing map $A \in \mathbb&amp;\#123;R&amp;\#125;^&amp;\#123;m \times u&amp;\#125;\( in \)\ell\_2\( that preserves distances up to distortion of \)1 + \varepsilon$ with probability \(1 - \delta\), where \(m = O(\varepsilon^\&amp;\#123;-2\&amp;\#125; \log 1/\delta)\) and each column of \(A\) has \(O(\varepsilon m)\) non-zero entries. The previous analyses of the Sparse Johnson-Lindenstrauss Transform all assumed access to a \(\Omega(\log 1/\delta)\)-wise independent hash function. The main contribution of this paper is a more general analysis of the Sparse Johnson-Lindenstrauss Transform with less assumptions on the hash function. We also show that the \emph&amp;\#123;Mixed Tabulation hash function&amp;\#125; of Dahlgaard, Knudsen, Rotenberg, and Thorup (FOCS 2015) satisfies the conditions of our analysis, thus giving us the first analysis of a Sparse Johnson-Lindenstrauss Transform that works with a practical hash function.
