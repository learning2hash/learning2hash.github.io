---
layout: publication
title: A Simple Streaming Bit-parallel Algorithm For Swap Pattern Matching
authors: "V\xE1clav Bla\u017Eej, Ond\u0159ej Such\xFD, Tom\xE1\u0161 Valla"
conference: Arxiv
year: 2016
bibkey: "bla\u017Eej2016simple"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.04763'}]
tags: []
short_authors: "V\xE1clav Bla\u017Eej, Ond\u0159ej Such\xFD, Tom\xE1\u0161 Valla"
---
The pattern matching problem with swaps is to find all occurrences of a
pattern in a text while allowing the pattern to swap adjacent symbols. The goal
is to design fast matching algorithm that takes advantage of the bit
parallelism of bitwise machine instructions and has only streaming access to
the input. We introduce a new approach to solve this problem based on the graph
theoretic model and compare its performance to previously known algorithms. We
also show that an approach using deterministic finite automata cannot achieve
similarly efficient algorithms. Furthermore, we describe a fatal flaw in some
of the previously published algorithms based on the same model. Finally, we
provide experimental evaluation of our algorithm on real-world data.