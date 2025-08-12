---
layout: publication
title: On The Improvement Of The In-place Merge Algorithm Parallelization
authors: Berenger Bramas, Quentin Bramas
conference: Arxiv
year: 2020
bibkey: bramas2020improvement
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.12648'}]
tags: ["Efficiency"]
short_authors: Berenger Bramas, Quentin Bramas
---
In this paper, we present several improvements in the parallelization of the
in-place merge algorithm, which merges two contiguous sorted arrays into one
with an O(T) space complexity (where T is the number of threads). The approach
divides the two arrays into as many pairs of partitions as there are threads
available; such that each thread can later merge a pair of partitions
independently of the others. We extend the existing method by proposing a new
algorithm to find the median of two partitions. Additionally, we provide a new
strategy to divide the input arrays where we minimize the data movement, but at
the cost of making this stage sequential. Finally, we provide the so-called
linear shifting algorithm that swaps two partitions in-place with contiguous
data access. We emphasize that our approach is straightforward to implement and
that it can also be used for external (out of place) merging. The results
demonstrate that it provides a significant speedup compared to sequential
executions, when the size of the arrays is greater than a thousand elements.