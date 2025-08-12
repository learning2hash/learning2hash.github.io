---
layout: publication
title: Parallel External Sorting Of ASCII Records Using Learned Models
authors: Ani Kristo, Tim Kraska
conference: Arxiv
year: 2023
bibkey: kristo2023parallel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.05671'}]
tags: ["Efficiency", "Scalability"]
short_authors: Ani Kristo, Tim Kraska
---
External sorting is at the core of many operations in large-scale database
systems, such as ordering and aggregation queries for large result sets,
building indexes, sort-merge joins, duplicate removal, sharding, and record
clustering. Unlike in-memory sorting, these algorithms need to work together
with the OS and the filesystem to efficiently utilize system resources and
minimize disk I/O.
  In this paper we describe ELSAR: a parallel external sorting algorithm that
uses an innovative paradigm based on a learned data distribution model. The
algorithm leverages the model to arrange the input records into mutually
exclusive, monotonic, and equi-depth partitions that, once sorted, can simply
be concatenated to form the output. This method completely eliminates the need
for multi-way file merging, which is typically used in external sorting.
  We present thorough benchmarks for uniform and skewed datasets in various
storage media, where we measure the sorting rates, size scalability, and energy
efficiency of ELSAR and other sorting algorithms. We observed that ELSAR has up
to 1.65x higher sorting rates than the next-best external sort (Nsort) on SSD
drives and 5.31x higher than the GNU coreutils' sort utility on Intel Optane
non-volatile memory. In addition, ELSAR supersedes the current winner of the
SortBenchmark for the most energy-efficient external string sorting algorithm
by an impressive margin of 41%.
  These results reinforce the premise that novel learning-enhanced algorithms
can provide remarkable performance benefits over traditional ones.