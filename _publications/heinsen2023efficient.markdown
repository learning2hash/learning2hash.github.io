---
layout: publication
title: Efficient Parallelization Of A Ubiquitous Sequential Computation
authors: Franz A. Heinsen
conference: Arxiv
year: 2023
bibkey: heinsen2023efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.06281'}]
tags: ["Efficiency", "Scalability"]
short_authors: Franz A. Heinsen
---
We find a succinct expression for computing the sequence \(x_t = a_t x_\{t-1\} +
b_t\) in parallel with two prefix sums, given \(t = (1, 2, \dots, n)\), \(a_t \in
\mathbb\{R\}^n\), \(b_t \in \mathbb\{R\}^n\), and initial value \(x_0 \in \mathbb\{R\}\).
On \(n\) parallel processors, the computation of \(n\) elements incurs
\(\mathcal\{O\}(log n)\) time and \(\mathcal\{O\}(n)\) space. Sequences of this form
are ubiquitous in science and engineering, making efficient parallelization
useful for a vast number of applications. We implement our expression in
software, test it on parallel hardware, and verify that it executes faster than
sequential computation by a factor of \(\frac\{n\}\{log n\}\).