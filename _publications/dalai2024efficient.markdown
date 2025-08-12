---
layout: publication
title: An Efficient Algorithm For Group Testing With Runlength Constraints
authors: Marco Dalai, Stefano Della Fiore, Adele A. Rescigno, Ugo Vaccaro
conference: Arxiv
year: 2024
bibkey: dalai2024efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.03491'}]
tags: ["Efficiency"]
short_authors: Dalai et al.
---
In this paper, we provide an efficient algorithm to construct almost optimal
\((k,n,d)\)-superimposed codes with runlength constraints. A
\((k,n,d)\)-superimposed code of length \(t\) is a \(t \times n\) binary matrix such
that any two 1's in each column are separated by a run of at least \(d\) 0's, and
such that for any column \(\mathbf\{c\}\) and any other \(k-1\) columns, there exists
a row where \(\mathbf\{c\}\) has \(1\) and all the remaining \(k-1\) columns have \(0\).
These combinatorial structures were introduced by Agarwal et al. [1], in the
context of Non-Adaptive Group Testing algorithms with runlength constraints.
  By using Moser and Tardos' constructive version of the Lov\'asz Local Lemma,
we provide an efficient randomized Las Vegas algorithm of complexity \(\Theta(t
n^2)\) for the construction of \((k,n,d)\)-superimposed codes of length
\(t=O(dklog n +k^2log n)\). We also show that the length of our codes is
shorter, for \(n\) sufficiently large, than that of the codes whose existence was
proved in [1].