---
layout: publication
title: Acceleration Of Fm-index Queries Through Prefix-free Parsing
authors: "Aaron Hong, Marco Oliva, Dominik K\xF6ppl, Hideo Bannai, Christina Boucher,\
  \ Travis Gagie"
conference: Arxiv
year: 2023
bibkey: hong2023acceleration
citations: 0
additional_links: [{name: Code, url: 'https://github.com/marco-oliva/afm'}, {name: Paper,
    url: 'https://arxiv.org/abs/2305.05893'}]
tags: ["Efficiency"]
short_authors: Hong et al.
---
FM-indexes are a crucial data structure in DNA alignment, for example, but
searching with them usually takes at least one random access per character in
the query pattern. Ferragina and Fischer observed in 2007 that word-based
indexes often use fewer random accesses than character-based indexes, and thus
support faster searches. Since DNA lacks natural word-boundaries, however, it
is necessary to parse it somehow before applying word-based FM-indexing. Last
year, Deng et al.\ proposed parsing genomic data by induced suffix sorting, and
showed the resulting word-based FM-indexes support faster counting queries than
standard FM-indexes when patterns are a few thousand characters or longer. In
this paper we show that using prefix-free parsing -- which takes parameters
that let us tune the average length of the phrases -- instead of induced suffix
sorting, gives a significant speedup for patterns of only a few hundred
characters. We implement our method and demonstrate it is between 3 and 18
times faster than competing methods on queries to GRCh38. And was consistently
faster on queries made to 25,000, 50,000 and 100,000 SARS-CoV-2 genomes. Hence,
it is very clear that our method accelerates the performance of count over all
state-of-the-art methods with a minor increase in the memory. Our source code
is available at https://github.com/marco-oliva/afm .