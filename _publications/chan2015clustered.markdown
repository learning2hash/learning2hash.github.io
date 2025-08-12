---
layout: publication
title: Clustered Integer 3SUM Via Additive Combinatorics
authors: Timothy M. Chan, Moshe Lewenstein
conference: Proceedings of the forty-seventh annual ACM symposium on Theory of Computing
year: 2015
bibkey: chan2015clustered
citations: 110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.05204'}]
tags: []
short_authors: Timothy M. Chan, Moshe Lewenstein
---
We present a collection of new results on problems related to 3SUM,
including:
  1. The first truly subquadratic algorithm for
  \(\ \ \ \ \ \) 1a. computing the (min,+) convolution for monotone increasing
sequences with integer values bounded by \(O(n)\),
  \(\ \ \ \ \ \)1b. solving 3SUM for monotone sets in 2D with integer coordinates
bounded by \(O(n)\), and
  \(\ \ \ \ \ \)1c. preprocessing a binary string for histogram indexing (also
called jumbled indexing).
  The running time is:
\(O(n^\{(9+\sqrt\{177\})/12\}\,\textrm\{polylog\}\,n)=O(n^\{1.859\})\) with
randomization, or \(O(n^\{1.864\})\) deterministically. This greatly improves the
previous \(n^2/2^\{Ω(\sqrt\{log n\})\}\) time bound obtained from Williams'
recent result on all-pairs shortest paths [STOC'14], and answers an open
question raised by several researchers studying the histogram indexing problem.
  2. The first algorithm for histogram indexing for any constant alphabet size
that achieves truly subquadratic preprocessing time and truly sublinear query
time.
  3. A truly subquadratic algorithm for integer 3SUM in the case when the given
set can be partitioned into \(n^\{1-\delta\}\) clusters each covered by an interval
of length \(n\), for any constant \(\delta>0\).
  4. An algorithm to preprocess any set of \(n\) integers so that subsequently
3SUM on any given subset can be solved in \(O(n^\{13/7\}\,\textrm\{polylog\}\,n)\)
time.
  All these results are obtained by a surprising new technique, based on the
Balog--Szemer\'edi--Gowers Theorem from additive combinatorics.