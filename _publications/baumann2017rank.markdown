---
layout: publication
title: Rank-select Indices Without Tears
authors: Tim Baumann, Torben Hagerup
conference: Lecture Notes in Computer Science
year: 2019
bibkey: baumann2017rank
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.02377'}]
tags: []
short_authors: Tim Baumann, Torben Hagerup
---
A rank-select index for a sequence \\(B=(b_1,\ldots,b_n)\\) of \\(n\\) bits is a data
structure that, if provided with an operation to access \\(\Theta(log n)\\)
arbitrary consecutive bits of \\(B\\) in constant time (thus \\(B\\) is stored outside
of the data structure), can compute \\(\mathit\{rank\}_B(j)=\sum_\{i=1\}^j b_i\\) for
given \\(j\in\\{0,\ldots,n\\}\\) and
\\(\mathit\{select\}_B(k)=\min\\{j:\mathit\{rank\}_B(j)\ge k\\}\\) for given
\\(k\in\\{1,\ldots,\sum_\{i=1\}^n b_i\\}\\). We describe a new rank-select index that,
like previous rank-select indices, occupies \\(O(nloglog n/log n)\\) bits and
executes \\(\mathit\{rank\}\\) and \\(\mathit\{select\}\\) queries in constant time. Its
derivation is intended to be particularly easy to follow and largely free of
tedious low-level detail, its operations are given by straight-line code, and
we show that it can be constructed in \\(O(n/log n)\\) time.