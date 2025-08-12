---
layout: publication
title: Faster Algorithms For Text-to-pattern Hamming Distances
authors: Timothy M. Chan, Ce Jin, Virginia Vassilevska Williams, Yinzhan Xu
conference: 2023 IEEE 64th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2023
bibkey: chan2023faster
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.13174'}]
tags: ["Hashing Methods"]
short_authors: Chan et al.
---
We study the classic Text-to-Pattern Hamming Distances problem: given a
pattern \(P\) of length \(m\) and a text \(T\) of length \(n\), both over a
polynomial-size alphabet, compute the Hamming distance between \(P\) and \(T[i\,
.\, . \, i+m-1]\) for every shift \(i\), under the standard Word-RAM model with
\(\Theta(log n)\)-bit words.
  - We provide an \(O(n\sqrt\{m\})\) time Las Vegas randomized algorithm for this
problem, beating the decades-old \(O(n \sqrt\{m log m\})\) running time
[Abrahamson, SICOMP 1987]. We also obtain a deterministic algorithm, with a
slightly higher \(O(n\sqrt\{m\}(log mloglog m)^\{1/4\})\) running time. Our
randomized algorithm extends to the \(k\)-bounded setting, with running time
\(O\big(n+\frac\{nk\}\{\sqrt\{m\}\}\big)\), removing all the extra logarithmic factors
from earlier algorithms [Gawrychowski and Uzna\'\{n\}ski, ICALP 2018; Chan,
Golan, Kociumaka, Kopelowitz and Porat, STOC 2020].
  - For the \((1+\epsilon)\)-approximate version of Text-to-Pattern Hamming
Distances, we give an \(\tilde\{O\}(\epsilon^\{-0.93\}n)\) time Monte Carlo
randomized algorithm, beating the previous \(\tilde\{O\}(\epsilon^\{-1\}n)\) running
time [Kopelowitz and Porat, FOCS 2015; Kopelowitz and Porat, SOSA 2018].
  Our approximation algorithm exploits a connection with \(3\)SUM, and uses a
combination of Fredman's trick, equality matrix product, and random sampling;
in particular, we obtain new results on approximate counting versions of \(3\)SUM
and Exact Triangle, which may be of independent interest. Our exact algorithms
use a novel combination of hashing, bit-packed FFT, and recursion; in
particular, we obtain a faster algorithm for computing the sumset of two
integer sets, in the regime when the universe size is close to quadratic in the
number of elements.
  We also prove a fine-grained equivalence between the exact Text-to-Pattern
Hamming Distances problem and a range-restricted, counting version of \(3\)SUM.