---
layout: publication
title: 'RLZAP: Relative Lempel-ziv With Adaptive Pointers'
authors: "Anthony J. Cox, Andrea Farruggia, Travis Gagie, Simon J. Puglisi, Jouni\
  \ Sir\xE9n"
conference: Lecture Notes in Computer Science
year: 2016
bibkey: cox2016rlzap
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.04421'}]
tags: []
short_authors: Cox et al.
---
Relative Lempel-Ziv (RLZ) is a popular algorithm for compressing databases of
genomes from individuals of the same species when fast random access is
desired. With Kuruppu et al.'s (SPIRE 2010) original implementation, a
reference genome is selected and then the other genomes are greedily parsed
into phrases exactly matching substrings of the reference. Deorowicz and
Grabowski (Bioinformatics, 2011) pointed out that letting each phrase end with
a mismatch character usually gives better compression because many of the
differences between individuals' genomes are single-nucleotide substitutions.
Ferrada et al. (SPIRE 2014) then pointed out that also using relative pointers
and run-length compressing them usually gives even better compression. In this
paper we generalize Ferrada et al.'s idea to handle well also short insertions,
deletions and multi-character substitutions. We show experimentally that our
generalization achieves better compression than Ferrada et al.'s implementation
with comparable random-access times.