---
layout: publication
title: Strong Link Between BWT And XBW Via Aho-corasick Automaton And Applications
  To Run-length Encoding
authors: Bastien Cazaux, Eric Rivals
conference: 30th Annual Symposium on Combinatorial Pattern Matching (CPM 2019) Leibniz
  International Proceedings in Informatics (LIPIcs) vol 128 p. 241--2420 2019
year: 2018
bibkey: cazaux2018strong
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.10070'}]
tags: []
short_authors: Bastien Cazaux, Eric Rivals
---
The boom of genomic sequencing makes compression of set of sequences
inescapable. This underlies the need for multi-string indexing data structures
that helps compressing the data. The most prominent example of such data
structures is the Burrows-Wheeler Transform (BWT), a reversible permutation of
a text that improves its compressibility. A similar data structure, the
eXtended Burrows-Wheeler Transform (XBW), is able to index a tree labelled with
alphabet symbols. A link between a multi-string BWT and the Aho-Corasick
automaton has already been found and led to a way to build a XBW from a
multi-string BWT. We exhibit a stronger link between a multi-string BWT and a
XBW by using the order of the concatenation in the multi-string. This bijective
link has several applications: first, it allows to build one data structure
from the other; second, it enables one to compute an ordering of the input
strings that optimises a Run-Length measure (i.e., the compressibility) of the
BWT or of the XBW.