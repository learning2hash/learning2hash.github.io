---
layout: publication
title: 'Secondary Indexing In One Dimension: Beyond B-trees And Bitmap Indexes'
authors: Rasmus Pagh, S. Srinivasa Rao
conference: Arxiv
year: 2008
bibkey: pagh2008secondary
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0811.2904'}]
tags: ["Efficiency"]
short_authors: Rasmus Pagh, S. Srinivasa Rao
---
Let S be a finite, ordered alphabet, and let x = x_1 x_2 ... x_n be a string
over S. A "secondary index" for x answers alphabet range queries of the form:
Given a range [a_l,a_r] over S, return the set I_\{[a_l;a_r]\} = \{i |x_i \in
[a_l; a_r]\}. Secondary indexes are heavily used in relational databases and
scientific data analysis. It is well-known that the obvious solution, storing a
dictionary for the position set associated with each character, does not always
give optimal query time. In this paper we give the first theoretically optimal
data structure for the secondary indexing problem. In the I/O model, the amount
of data read when answering a query is within a constant factor of the minimum
space needed to represent I_\{[a_l;a_r]\}, assuming that the size of internal
memory is (|S| log n)^\{delta\} blocks, for some constant delta > 0. The space
usage of the data structure is O(n log |S|) bits in the worst case, and we
further show how to bound the size of the data structure in terms of the 0-th
order entropy of x. We show how to support updates achieving various time-space
trade-offs.
  We also consider an approximate version of the basic secondary indexing
problem where a query reports a superset of I_\{[a_l;a_r]\} containing each
element not in I_\{[a_l;a_r]\} with probability at most epsilon, where epsilon >
0 is the false positive probability. For this problem the amount of data that
needs to be read by the query algorithm is reduced to O(|I_\{[a_l;a_r]\}|
log(1/epsilon)) bits.