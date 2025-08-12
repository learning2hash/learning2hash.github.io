---
layout: publication
title: Efficient Pattern Matching In Elastic-degenerate Strings
authors: Costas Iliopoulos, Ritu Kundu, Solon Pissis
conference: Information and Computation
year: 2020
bibkey: iliopoulos2016efficient
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.08111'}]
tags: ["Efficiency"]
short_authors: Costas Iliopoulos, Ritu Kundu, Solon Pissis
---
In this paper, we extend the notion of gapped strings to elastic-degenerate
strings. An elastic-degenerate string can been seen as an ordered collection of
k > 1 seeds (substrings/subpatterns) interleaved by elastic-degenerate symbols
such that each elastic-degenerate symbol corresponds to a set of two or more
variable length strings. Here, we present an algorithm for solving the pattern
matching problem with (solid) pattern and elastic-degenerate text, running in
O(N+\{\alpha\}\{\gamma\}nm) time; where m is the length of the given pattern; n and
N are the length and total size of the given elastic-degenerate text,
respectively; \{\alpha\} and \{\gamma\} are small constants, respectively
representing the maximum number of strings in any elastic-degenerate symbol of
the text and the largest number of elastic-degenerate symbols spanned by any
occurrence of the pattern in the text. The space used by the algorithm is
linear in the size of the input for a constant number of elastic-degenerate
symbols in the text; \{\alpha\} and \{\gamma\} are so small in real applications
that the algorithm is expected to work very efficiently in practice.