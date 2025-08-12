---
layout: publication
title: 'Shaving Logs Via Large Sieve Inequality: Faster Algorithms For Sparse Convolution
  And More'
authors: Ce Jin, Yinzhan Xu
conference: Proceedings of the 56th Annual ACM Symposium on Theory of Computing
year: 2024
bibkey: jin2024shaving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.20326'}]
tags: ["Efficiency"]
short_authors: Ce Jin, Yinzhan Xu
---
In sparse convolution-type problems, a common technique is to hash the input
integers modulo a random prime \(p\in [Q/2,Q]\) for some parameter \(Q\), which
reduces the range of the input integers while preserving their additive
structure. However, this hash family suffers from two drawbacks, which led to
bottlenecks in many state-of-the-art algorithms: (1) The collision probability
of two elements from \([N]\) is \(O(\frac\{log N\}\{Q\})\) rather than
\(O(\frac\{1\}\{Q\})\); (2) It is difficult to derandomize the choice of \(p\); known
derandomization techniques lead to super-logarithmic overhead [Chan, Lewenstein
STOC'15].
  In this paper, we partially overcome these drawbacks in certain scenarios,
via novel applications of the large sieve inequality from analytic number
theory. Consequently, we obtain the following improved algorithms for various
problems (in the standard word RAM model):
  Sparse Nonnegative Convolution: We obtain an \(O(tlog t)\)-time Las Vegas
algorithm that computes the convolution \(A\star B\) of two nonnegative integer
vectors \(A,B\), where \(t\) is the output sparsity \(\|A\star B\|_0\). Moreover, our
algorithm terminates in \(O(tlog t)\) time with \(1-1/\mathrm\{poly\}(t)\)
probability.
  Text-to-Pattern Hamming Distances: Given a length-\(m\) pattern \(P\) and a
length-\(n\) text \(T\), we obtain a deterministic \(O(n\sqrt\{mlog log m\})\)-time
algorithm that exactly computes the Hamming distance between \(P\) and every
length-\(m\) substring of \(T\).
  Sparse General Convolution: We also give a Monte Carlo \(O(tlog t)\) time
algorithm for sparse convolution with possibly negative input in the restricted
case where the length \(N\) of the input vectors satisfies \(N\le t^\{1.99\}\).