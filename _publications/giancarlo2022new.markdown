---
layout: publication
title: A New Class Of String Transformations For Compressed Text Indexing
authors: Raffaele Giancarlo, Giovanni Manzini, Antonio Restivo, Giovanna Rosone, Marinella
  Sciortino
conference: Information and Computation
year: 2023
bibkey: giancarlo2022new
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.05643'}]
tags: []
short_authors: Giancarlo et al.
---
Introduced about thirty years ago in the field of Data Compression, the
Burrows-Wheeler Transform (BWT) is a string transformation that, besides being
a booster of the performance of memoryless compressors, plays a fundamental
role in the design of efficient self-indexing compressed data structures.
Finding other string transformations with the same remarkable properties of BWT
has been a challenge for many researchers for a long time. Among the known BWT
variants, the only one that has been recently shown to be a valid alternative
to BWT is the Alternating BWT (ABWT), another invertible string transformation
introduced about ten years ago in connection with a generalization of Lyndon
words. In this paper, we introduce a whole class of new string transformations,
called local orderings-based transformations, which have all the myriad virtues
of BWT. We show that this new family is a special case of a much larger class
of transformations, based on context adaptive alphabet orderings, that includes
BWT and ABWT. Although all transformations support pattern search, we show
that, in the general case, the transformations within our larger class may take
quadratic time for inversion and pattern search. As a further result, we show
that the local orderings-based transformations can be used for the construction
of the recently introduced r-index, which makes them suitable also for highly
repetitive collections. In this context, we consider the problem of finding,
for a given string, the BWT variant that minimizes the number of runs in the
transformed string, and we provide an algorithm solving this problem in linear
time.