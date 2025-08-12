---
layout: publication
title: Substring Range Reporting
authors: Philip Bille, Inge Li Goertz
conference: Lecture Notes in Computer Science
year: 2011
bibkey: bille2011substring
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1108.3683'}]
tags: ["Efficiency"]
short_authors: Philip Bille, Inge Li Goertz
---
We revisit various string indexing problems with range reporting features,
namely, position-restricted substring searching, indexing substrings with gaps,
and indexing substrings with intervals. We obtain the following main results.
\{itemize\} We give efficient reductions for each of the above problems to a new
problem, which we call *substring range reporting*. Hence, we unify the
previous work by showing that we may restrict our attention to a single problem
rather than studying each of the above problems individually. We show how to
solve substring range reporting with optimal query time and little space.
Combined with our reductions this leads to significantly improved time-space
trade-offs for the above problems. In particular, for each problem we obtain
the first solutions with optimal time query and \(O(nlog^\{O(1)\} n)\) space,
where \(n\) is the length of the indexed string. We show that our techniques for
substring range reporting generalize to *substring range counting* and
*substring range emptiness* variants. We also obtain non-trivial
time-space trade-offs for these problems. \{itemize\} Our bounds for substring
range reporting are based on a novel combination of suffix trees and range
reporting data structures. The reductions are simple and general and may apply
to other combinations of string indexing with range reporting.