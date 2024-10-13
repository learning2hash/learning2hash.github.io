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
<p>The of Kane and Nelson (SODA 2012) provides a linear
dimensionality-reducing map <span class="math inline">\(A \in
\mathbb{R}^{m \times
u}\)</span> in <span class="math inline">\(\ell_2\)</span> that
preserves distances up to distortion of <span class="math inline">\(1 +
\varepsilon\)</span> with probability <span class="math inline">\(1 -
\delta\)</span>, where <span class="math inline">\(m =
O(\varepsilon^{-2} \log 1/\delta)\)</span> and each column of <span
class="math inline">\(A\)</span> has <span
class="math inline">\(O(\varepsilon m)\)</span> non-zero entries. The
previous analyses of the Sparse Johnson-Lindenstrauss Transform all
assumed access to a <span class="math inline">\(\Omega(\log
1/\delta)\)</span>-wise independent hash function. The main contribution
of this paper is a more general analysis of the Sparse
Johnson-Lindenstrauss Transform with less assumptions on the hash
function. We also show that the of Dahlgaard, Knudsen, Rotenberg, and
Thorup (FOCS 2015) satisfies the conditions of our analysis, thus giving
us the first analysis of a Sparse Johnson-Lindenstrauss Transform that
works with a practical hash function.</p>
