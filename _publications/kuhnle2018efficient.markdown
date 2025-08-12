---
layout: publication
title: Efficient Construction Of A Complete Index For Pan-genomics Read Alignment
authors: Alan Kuhnle, Taher Mun, Christina Boucher, Travis Gagie, Ben Langmead, Giovanni
  Manzini
conference: Journal of Computational Biology
year: 2020
bibkey: kuhnle2018efficient
citations: 57
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.06933'}]
tags: ["Efficiency"]
short_authors: Kuhnle et al.
---
While short read aligners, which predominantly use the FM-index, are able to
easily index one or a few human genomes, they do not scale well to indexing
databases containing thousands of genomes. To understand why, it helps to
examine the main components of the FM-index in more detail, which is a rank
data structure over the Burrows-Wheeler Transform (BWT) of the string that will
allow us to find the interval in the string's suffix array (SA) containing
pointers to starting positions of occurrences of a given pattern; second, a
sample of the SA that --- when used with the rank data structure --- allows us
access the SA. The rank data structure can be kept small even for large genomic
databases, by run-length compressing the BWT, but until recently there was no
means known to keep the SA sample small without greatly slowing down access to
the SA. Now that Gagie et al. (SODA 2018) have defined an SA sample that takes
about the same space as the run-length compressed BWT --- we have the design
for efficient FM-indexes of genomic databases but are faced with the problem of
building them. In 2018 we showed how to build the BWT of large genomic
databases efficiently (WABI 2018) but the problem of building Gagie et al.'s SA
sample efficiently was left open. We compare our approach to state-of-the-art
methods for constructing the SA sample, and demonstrate that it is the fastest
and most space-efficient method on highly repetitive genomic databases. Lastly,
we apply our method for indexing partial and whole human genomes, and show that
it improves over Bowtie with respect to both memory and time.