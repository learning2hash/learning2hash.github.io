---
layout: publication
title: Sub-string/pattern Matching In Sub-linear Time Using A Sparse Fourier Transform
  Approach
authors: Nagaraj T. Janakiraman, Avinash Vem, Krishna R. Narayanan, Jean-Francois
  Chamberland
conference: Arxiv
year: 2017
bibkey: janakiraman2017sub
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.07852'}]
tags: ["Efficiency", "Scalability", "Similarity Search"]
short_authors: Janakiraman et al.
---
We consider the problem of querying a string (or, a database) of length \(N\)
bits to determine all the locations where a substring (query) of length \(M\)
appears either exactly or is within a Hamming distance of \(K\) from the query.
We assume that sketches of the original signal can be computed off line and
stored. Using the sparse Fourier transform computation based approach
introduced by Pawar and Ramchandran, we show that all such matches can be
determined with high probability in sub-linear time. Specifically, if the query
length \(M = O(N^\mu)\) and the number of matches \(L=O(N^\lambda)\), we show that
for \(\lambda < 1-\mu\) all the matching positions can be determined with a
probability that approaches 1 as \(N \rightarrow \infty\) for \(K \leq
\frac\{1\}\{6\}M\). More importantly our scheme has a worst-case computational
complexity that is only \(O\left(\max\\{N^\{1-\mu\}log^2 N, N^\{\mu+\lambda\}log N
\\}\right)\), which means we can recover all the matching positions in \{\it
sub-linear\} time for \(\lambda<1-\mu\). This is a substantial improvement over
the best known computational complexity of \(O\left(N^\{1-0.359 \mu\} \right)\) for
recovering one matching position by Andoni \{\em et al.\} \cite\{andoni2013shift\}.
Further, the number of Fourier transform coefficients that need to be computed,
stored and accessed, i.e., the sketching complexity of this algorithm is only
\(O\left(N^\{1-\mu\}log N\right)\). Several extensions of the main theme are also
discussed.