---
layout: publication
title: Memory Efficient De Bruijn Graph Construction
authors: Yang Li, Pegah Kamousi, Fangqiu Han, Shengqi Yang, Xifeng Yan, Subhash Suri
conference: Arxiv
year: 2012
bibkey: li2012memory
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1207.3532'}]
tags: ["Memory Efficiency"]
short_authors: Li et al.
---
Massively parallel DNA sequencing technologies are revolutionizing genomics
research. Billions of short reads generated at low costs can be assembled for
reconstructing the whole genomes. Unfortunately, the large memory footprint of
the existing de novo assembly algorithms makes it challenging to get the
assembly done for higher eukaryotes like mammals. In this work, we investigate
the memory issue of constructing de Bruijn graph, a core task in leading
assembly algorithms, which often consumes several hundreds of gigabytes memory
for large genomes. We propose a disk-based partition method, called Minimum
Substring Partitioning (MSP), to complete the task using less than 10 gigabytes
memory, without runtime slowdown. MSP breaks the short reads into multiple
small disjoint partitions so that each partition can be loaded into memory,
processed individually and later merged with others to form a de Bruijn graph.
By leveraging the overlaps among the k-mers (substring of length k), MSP
achieves astonishing compression ratio: The total size of partitions is reduced
from \(\Theta(kn)\) to \(\Theta(n)\), where \(n\) is the size of the short read
database, and \(k\) is the length of a \(k\)-mer. Experimental results show that
our method can build de Bruijn graphs using a commodity computer for any
large-volume sequence dataset.