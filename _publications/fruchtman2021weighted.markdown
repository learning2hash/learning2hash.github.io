---
layout: publication
title: Weighted Burrows-wheeler Compression
authors: Aharon Fruchtman, Yoav Gross, Shmuel T. Klein, Dana Shapira
conference: SN Computer Science
year: 2023
bibkey: fruchtman2021weighted
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.10327'}]
tags: ["Efficiency"]
short_authors: Fruchtman et al.
---
A weight based dynamic compression method has recently been proposed, which
is especially suitable for the encoding of files with locally skewed
distributions. Its main idea is to assign larger weights to closer to be
encoded symbols by means of an increasing weight function, rather than
considering each position in the text evenly. A well known transformation that
tends to convert input files into files with a more skewed distribution is the
Burrows-Wheeler Transform. This paper employs the weighted approach on
Burrows-Wheeler transformed files and provides empirical evidence of the
efficiency of this combination.