---
layout: publication
title: Encoding 2-D Range Maximum Queries
authors: Mordecai J. Golin, John Iacono, Danny Krizanc, Rajeev Raman, S. Srinivasa
  Rao, Sunil Shende
conference: Arxiv
year: 2011
bibkey: golin2011encoding
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1109.2885'}]
tags: []
short_authors: Golin et al.
---
We consider the *two-dimensional range maximum query (2D-RMQ)* problem:
given an array \(A\) of ordered values, to pre-process it so that we can find the
position of the smallest element in the sub-matrix defined by a
(user-specified) range of rows and range of columns. We focus on determining
the *effective* entropy of 2D-RMQ, i.e., how many bits are needed to
encode \(A\) so that 2D-RMQ queries can be answered *without* access to \(A\).
We give tight upper and lower bounds on the expected effective entropy for the
case when \(A\) contains independent identically-distributed random values, and
new upper and lower bounds for arbitrary \(A\), for the case when \(A\) contains
few rows. The latter results improve upon previous upper and lower bounds by
Brodal et al. (ESA 2010). In some cases we also give data structures whose
space usage is close to the effective entropy and answer 2D-RMQ queries
rapidly.