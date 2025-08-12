---
layout: publication
title: 'Pivotcompress: Compression By Sorting'
authors: Oscar Stiffelman
conference: Arxiv
year: 2014
bibkey: stiffelman2014pivotcompress
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1411.5127'}]
tags: []
short_authors: Oscar Stiffelman
---
Sorted data is usually easier to compress than unsorted permutations of the
same data. This motivates a simple compression scheme: specify the sorted
permutation of the data along with a representation of the sorted data
compressed recursively. The sorted permutation can be specified by recording
the decisions made by quicksort. If the size of the data is known, then the
quicksort decisions describe the data at a rate that is nearly as efficient as
the minimal prefix-free code for the distribution, which is bounded by the
entropy of the distribution. This is possible even though the distribution is
unknown ahead of time. Used in this way, quicksort acts as a universal code in
that it is asymptotically optimal for any stationary source. The Shannon
entropy is a lower bound when describing stochastic, independent symbols.
However, it is possible to encode non-uniform, finite strings below the entropy
of the sample distribution by also encoding symbol counts because the values in
the sequence are no longer independent once the counts are known. The key
insight is that sparse quicksort comparison vectors can also be compressed to
achieve an even lower rate when data is highly non-uniform while incurring only
a modest penalty when data is random.