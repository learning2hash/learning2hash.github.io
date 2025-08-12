---
layout: publication
title: Optimal In-place Suffix Sorting
authors: Zhize Li, Jian Li, Hongwei Huo
conference: Lecture Notes in Computer Science
year: 2018
bibkey: li2016optimal
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.08305'}]
tags: []
short_authors: Zhize Li, Jian Li, Hongwei Huo
---
The suffix array is a fundamental data structure for many applications that
involve string searching and data compression. Designing time/space-efficient
suffix array construction algorithms has attracted significant attention and
considerable advances have been made for the past 20 years. We obtain the
*first* in-place suffix array construction algorithms that are optimal
both in time and space for (read-only) integer alphabets. Concretely, we make
the following contributions:
  1. For integer alphabets, we obtain the first suffix sorting algorithm which
takes linear time and uses only \\(O(1)\\) workspace (the workspace is the total
space needed beyond the input string and the output suffix array). The input
string may be modified during the execution of the algorithm, but should be
restored upon termination of the algorithm.
  2. We strengthen the first result by providing the first in-place linear time
algorithm for read-only integer alphabets with \\(|\Sigma|=O(n)\\) (i.e., the input
string cannot be modified). This algorithm settles the open problem posed by
Franceschini and Muthukrishnan in ICALP 2007. The open problem asked to design
in-place algorithms in \\(o(nlog n)\\) time and ultimately, in \\(O(n)\\) time for
(read-only) integer alphabets with \\(|\Sigma| \leq n\\). Our result is in fact
slightly stronger since we allow \\(|\Sigma|=O(n)\\).
  3. Besides, for the read-only general alphabets (i.e., only comparisons are
allowed), we present an optimal in-place \\(O(nlog n)\\) time suffix sorting
algorithm, recovering the result obtained by Franceschini and Muthukrishnan
which was an open problem posed by Manzini and Ferragina in ESA 2002.