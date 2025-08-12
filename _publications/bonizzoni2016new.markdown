---
layout: publication
title: A New Lightweight Algorithm To Compute The BWT And The LCP Array Of A Set Of
  Strings
authors: Paola Bonizzoni, Gianluca Della Vedova, Serena Nicosia, Marco Previtali,
  Raffaella Rizzi
conference: Arxiv
year: 2016
bibkey: bonizzoni2016new
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.08342'}]
tags: []
short_authors: Bonizzoni et al.
---
Indexing of very large collections of strings such as those produced by the
widespread sequencing technologies, heavily relies on multi-string
generalizations of the Burrows-Wheeler Transform (BWT), and for this problem
various in-memory algorithms have been proposed. The rapid growing of data that
are processed routinely, such as in bioinformatics, requires a large amount of
main memory, and this fact has motivated the development of algorithms, to
compute the BWT, that work almost entirely in external memory. On the other
hand, the related problem of computing the Longest Common Prefix (LCP) array is
often instrumental in several algorithms on collection of strings, such as
those that compute the suffix-prefix overlap among strings, which is an
essential step for many genome assembly algorithms. The best current
lightweight approach to compute BWT and LCP array on a set of \(m\) strings, each
one \(k\) characters long, has I/O complexity that is \(O(mk^2 log |\Sigma|)\)
(where \(|\Sigma|\) is the size of the alphabet), thus it is not optimal. In this
paper we propose a novel approach to build BWT and LCP array (simultaneously)
with \(O(kmL(log k +log \sigma))\) I/O complexity, where \(L\) is the length of
longest substring that appears at least twice in the input strings.