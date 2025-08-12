---
layout: publication
title: An Algorithm To Recover Shredded Random Matrices
authors: Caelan Atamanchuk, Luc Devroye, Massimo Vicenzo
conference: SIAM Journal on Discrete Mathematics
year: 2024
bibkey: atamanchuk2023algorithm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.16715'}]
tags: []
short_authors: Caelan Atamanchuk, Luc Devroye, Massimo Vicenzo
---
Given some binary matrix \\(M\\), suppose we are presented with the collection of
its rows and columns in independent arbitrary orderings. From this information,
are we able to recover the unique original orderings and matrix? We present an
algorithm that identifies whether there is a unique ordering associated with a
set of rows and columns, and outputs either the unique correct orderings for
the rows and columns or the full collection of all valid orderings and valid
matrices. We show that there is a constant \\(c > 0\\) such that the algorithm
terminates in \\(O(n^2)\\) time with high probability and in expectation for random
\\(n \times n\\) binary matrices with i.i.d.\ Bernoulli \\((p)\\) entries
\\((m_\{ij\})_\{ij=1\}^n\\) such that \\(\frac\{clog^2(n)\}\{n(loglog(n))^2\} \leq p \leq
\frac\{1\}\{2\}\\).