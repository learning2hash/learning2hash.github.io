---
layout: publication
title: Relative Suffix Trees
authors: "Andrea Farruggia, Travis Gagie, Gonzalo Navarro, Simon J. Puglisi, Jouni\
  \ Sir\xE9n"
conference: The Computer Journal
year: 2017
bibkey: farruggia2015relative
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1508.02550'}]
tags: []
short_authors: Farruggia et al.
---
Suffix trees are one of the most versatile data structures in stringology,
with many applications in bioinformatics. Their main drawback is their size,
which can be tens of times larger than the input sequence. Much effort has been
put into reducing the space usage, leading ultimately to compressed suffix
trees. These compressed data structures can efficiently simulate the suffix
tree, while using space proportional to a compressed representation of the
sequence. In this work, we take a new approach to compressed suffix trees for
repetitive sequence collections, such as collections of individual genomes. We
compress the suffix trees of individual sequences relative to the suffix tree
of a reference sequence. These relative data structures provide competitive
time/space trade-offs, being almost as small as the smallest compressed suffix
trees for repetitive collections, and competitive in time with the largest and
fastest compressed suffix trees.