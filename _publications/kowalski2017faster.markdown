---
layout: publication
title: Faster Range Minimum Queries
authors: Tomasz Kowalski, Szymon Grabowski
conference: 'Software: Practice and Experience'
year: 2018
bibkey: kowalski2017faster
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.10385'}]
tags: ["Efficiency"]
short_authors: Tomasz Kowalski, Szymon Grabowski
---
Range Minimum Query (RMQ) is an important building brick of many compressed
data structures and string matching algorithms. Although this problem is
essentially solved in theory, with sophisticated data structures allowing for
constant time queries, practical performance and construction time also matter.
Additionally, there are offline scenarios in which the number of queries, \\(q\\),
is rather small and given beforehand, which encourages to use a simpler
approach. In this work, we present a simple data structure, with very fast
construction, which allows to handle queries in constant time on average. This
algorithm, however, requires access to the input data during queries (which is
not the case of sophisticated RMQ solutions). We subsequently refine our
technique, combining it with one of the existing succinct solutions with \\(O(1)\\)
worst-case time queries and no access to the input array. The resulting hybrid
is still a memory frugal data structure, spending usually up to about \\(3n\\)
bits, and providing competitive query times, especially for wide ranges. We
also show how to make our baseline data structure more compact. Experimental
results demonstrate that the proposed BbST (Block-based Sparse Table) variants
are competitive to existing solutions, also in the offline scenario.