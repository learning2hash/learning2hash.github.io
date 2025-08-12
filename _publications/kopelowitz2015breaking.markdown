---
layout: publication
title: 'Breaking The Variance: Approximating The Hamming Distance In $\tilde O(1/\epsilon)$
  Time Per Alignment'
authors: Tsvi Kopelowitz, Ely Porat
conference: Arxiv
year: 2015
bibkey: kopelowitz2015breaking
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.04515'}]
tags: ["Distance Metric Learning", "Efficiency", "Hashing Methods", "Locality Sensitive Hashing", "Scalability"]
short_authors: Tsvi Kopelowitz, Ely Porat
---
The algorithmic tasks of computing the Hamming distance between a given
pattern of length \(m\) and each location in a text of length \(n\) is one of the
most fundamental algorithmic tasks in string algorithms. Unfortunately, there
is evidence that for a text \(T\) of size \(n\) and a pattern \(P\) of size \(m\), one
cannot compute the exact Hamming distance for all locations in \(T\) in time
which is less than \(\tilde O(n\sqrt m)\). However, Karloff~\cite\{karloff\} showed
that if one is willing to suffer a \(1\pm\epsilon\) approximation, then it is
possible to solve the problem with high probability, in \(\tilde O(\frac n
\{\epsilon^2\})\) time.
  Due to related lower bounds for computing the Hamming distance of two strings
in the one-way communication complexity model, it is strongly believed that
obtaining an algorithm for solving the approximation version cannot be done
much faster as a function of \(\frac 1 \epsilon\). We show here that this belief
is false by introducing a new \(\tilde O(\frac\{n\}\{\epsilon\})\) time algorithm
that succeeds with high probability.
  The main idea behind our algorithm, which is common in sparse recovery
problems, is to reduce the variance of a specific randomized experiment by
(approximately) separating heavy hitters from non-heavy hitters. However, while
known sparse recovery techniques work very well on vectors, they do not seem to
apply here, where we are dealing with mismatches between pairs of characters.
We introduce two main algorithmic ingredients. The first is a new sparse
recovery method that applies for pair inputs (such as in our setting). The
second is a new construction of hash/projection functions, which allows to
count the number of projections that induce mismatches between two characters
exponentially faster than brute force. We expect that these algorithmic
techniques will be of independent interest.