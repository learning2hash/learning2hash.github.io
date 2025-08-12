---
layout: publication
title: Using Positional Sequence Patterns To Estimate The Selectivity Of SQL LIKE
  Queries
authors: Mehmet Aytimur, Ali Cakmak
conference: Expert Systems with Applications
year: 2020
bibkey: aytimur2020using
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01164'}]
tags: []
short_authors: Mehmet Aytimur, Ali Cakmak
---
With the dramatic increase in the amount of the text-based data which
commonly contains misspellings and other errors, querying such data with
flexible search patterns becomes more and more commonplace. Relational
databases support the LIKE operator to allow searching with a particular
wildcard predicate (e.g., LIKE 'Sub%', which matches all strings starting with
'Sub'). Due to the large size of text data, executing such queries in the most
optimal way is quite critical for database performance. While building the most
efficient execution plan for a LIKE query, the query optimizer requires the
selectivity estimate for the flexible pattern-based query predicate. Recently,
SPH algorithm is proposed which employs a sequence pattern-based histogram
structure to estimate the selectivity of LIKE queries. A drawback of the SPH
approach is that it often overestimates the selectivity of queries. In order to
alleviate the overestimation problem, in this paper, we propose a novel
sequence pattern type, called positional sequence patterns. The proposed
patterns differentiate between sequence item pairs that appear next to each
other in all pattern occurrences from those that may have other items between
them. Besides, we employ redundant pattern elimination based on pattern
information content during histogram construction. Finally, we propose a
partitioning-based matching scheme during the selectivity estimation. The
experimental results on a real dataset from DBLP show that the proposed
approach outperforms the state of the art by around 20% improvement in error
rates.