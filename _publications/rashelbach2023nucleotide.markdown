---
layout: publication
title: Nucleotide String Indexing Using Range Matching
authors: Alon Rashelbach, Ori Rottensterich, Mark Silberstien
conference: Arxiv
year: 2023
bibkey: rashelbach2023nucleotide
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.03804'}]
tags: []
short_authors: Alon Rashelbach, Ori Rottensterich, Mark Silberstien
---
The two most common data-structures for genome indexing, FM-indices and
hash-tables, exhibit a fundamental trade-off between memory footprint and
performance. We present Ranger, a new indexing technique for nucleotide
sequences that is both memory efficient and fast. We observe that nucleotide
sequences can be represented as integer ranges and leverage a range-matching
algorithm based on neural networks to perform the lookup.
  We prototype Ranger in software and integrate it into the popular Minimap2
tool. Ranger achieves almost identical end-to-end performance as the original
Minimap2, while occupying 1.7\(\times\) and 1.2\(\times\) less memory for short-
and long-reads, respectively. With a limited memory capacity, Ranger achieves
up to 4.3\(\times\) speedup for short reads compared to FM-Index, and up to
4.2\(\times\) and 1.8\(\times\) speedups for short- and long-reads, compared to
hash-tables. Ranger opens up new opportunities in the context of hardware
acceleration by reducing the memory footprint of long-seed indexes used in
state-of-the-art alignment accelerators by up to 23\(\times\) which results with
3\(\times\) faster alignment and negligible accuracy degradation. Moreover, its
worst case memory bandwidth and latency can be bounded in advance without the
need to inflate DRAM capacity.