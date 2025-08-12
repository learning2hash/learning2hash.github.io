---
layout: publication
title: Sublinear-time Algorithms For Computing & Embedding Gap Edit Distance
authors: Tomasz Kociumaka, Barna Saha
conference: 2020 IEEE 61st Annual Symposium on Foundations of Computer Science (FOCS)
year: 2020
bibkey: kociumaka2020sublinear
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.12762'}]
tags: ["Efficiency"]
short_authors: Tomasz Kociumaka, Barna Saha
---
In this paper, we design new sublinear-time algorithms for solving the gap
edit distance problem and for embedding edit distance to Hamming distance. For
the gap edit distance problem, we give an \(\tilde\{O\}(\frac\{n\}\{k\}+k^2)\)-time
greedy algorithm that distinguishes between length-\(n\) input strings with edit
distance at most \(k\) and those with edit distance exceeding \((3k+5)k\). This is
an improvement and a simplification upon the result of Goldenberg, Krauthgamer,
and Saha [FOCS 2019], where the \(k\) vs \(\Theta(k^2)\) gap edit distance problem
is solved in \(\tilde\{O\}(\frac\{n\}\{k\}+k^3)\) time. We further generalize our
result to solve the \(k\) vs \(k'\) gap edit distance problem in time
\(\tilde\{O\}(\frac\{nk\}\{k'\}+k^2+ \frac\{k^2\}\{k'\}\sqrt\{nk\})\), strictly improving
upon the previously known bound \(\tilde\{O\}(\frac\{nk\}\{k'\}+k^3)\). Finally, we
show that if the input strings do not have long highly periodic substrings,
then already the \(k\) vs \((1+\epsilon)k\) gap edit distance problem can be solved
in sublinear time. Specifically, if the strings contain no substring of length
\(\ell\) with period at most \(2k\), then the running time we achieve is
\(\tilde\{O\}(\frac\{n\}\{\epsilon^2 k\}+k^2\ell)\).
  We further give the first sublinear-time probabilistic embedding of edit
distance to Hamming distance. For any parameter \(p\), our
\(\tilde\{O\}(\frac\{n\}\{p\})\)-time procedure yields an embedding with distortion
\(O(kp)\), where \(k\) is the edit distance of the original strings. Specifically,
the Hamming distance of the resultant strings is between \(\frac\{k-p+1\}\{p+1\}\)
and \(O(k^2)\) with good probability. This generalizes the linear-time embedding
of Chakraborty, Goldenberg, and Kouck\'y [STOC 2016], where the resultant
Hamming distance is between \(\frac k2\) and \(O(k^2)\). Our algorithm is based on
a random walk over samples, which we believe will find other applications in
sublinear-time algorithms.