---
layout: publication
title: Can You Solve Closest String Faster Than Exhaustive Search?
authors: Amir Abboud, Nick Fischer, Elazar Goldenberg, Karthik C. S., Ron Safier
conference: Arxiv
year: 2023
bibkey: abboud2023can
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.16878'}]
tags: ["Efficiency"]
short_authors: Abboud et al.
---
We study the fundamental problem of finding the best string to represent a
given set, in the form of the Closest String problem: Given a set \(X \subseteq
\Sigma^d\) of \(n\) strings, find the string \(x^*\) minimizing the radius of the
smallest Hamming ball around \(x^*\) that encloses all the strings in \(X\). In
this paper, we investigate whether the Closest String problem admits algorithms
that are faster than the trivial exhaustive search algorithm. We obtain the
following results for the two natural versions of the problem:
  \(\bullet\) In the continuous Closest String problem, the goal is to find the
solution string \(x^*\) anywhere in \(\Sigma^d\). For binary strings, the
exhaustive search algorithm runs in time \(O(2^d poly(nd))\) and we prove that it
cannot be improved to time \(O(2^\{(1-\epsilon) d\} poly(nd))\), for any \(\epsilon
> 0\), unless the Strong Exponential Time Hypothesis fails.
  \(\bullet\) In the discrete Closest String problem, \(x^*\) is required to be in
the input set \(X\). While this problem is clearly in polynomial time, its
fine-grained complexity has been pinpointed to be quadratic time \(n^\{2 \pm
o(1)\}\) whenever the dimension is \(\omega(log n) < d < n^\{o(1)\}\). We complement
this known hardness result with new algorithms, proving essentially that
whenever \(d\) falls out of this hard range, the discrete Closest String problem
can be solved faster than exhaustive search. In the small-\(d\) regime, our
algorithm is based on a novel application of the inclusion-exclusion principle.
  Interestingly, all of our results apply (and some are even stronger) to the
natural dual of the Closest String problem, called the Remotest String problem,
where the task is to find a string maximizing the Hamming distance to all the
strings in \(X\).