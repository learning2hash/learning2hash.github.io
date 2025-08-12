---
layout: publication
title: Compressed Indexing With Signature Grammars
authors: Anders Roy Christiansen, Mikko Berggren Ettienne
conference: Lecture Notes in Computer Science
year: 2018
bibkey: christiansen2017compressed
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.08217'}]
tags: ["Compact Codes", "Efficiency"]
short_authors: Anders Roy Christiansen, Mikko Berggren Ettienne
---
The compressed indexing problem is to preprocess a string \\(S\\) of length \\(n\\)
into a compressed representation that supports pattern matching queries. That
is, given a string \\(P\\) of length \\(m\\) report all occurrences of \\(P\\) in \\(S\\).
  We present a data structure that supports pattern matching queries in \\(O(m +
occ (\lg\lg n + \lg^\epsilon z))\\) time using \\(O(z \lg(n / z))\\) space where \\(z\\)
is the size of the LZ77 parse of \\(S\\) and \\(\epsilon > 0\\) is an arbitrarily small
constant, when the alphabet is small or \\(z = O(n^\{1 - \delta\})\\) for any
constant \\(\delta > 0\\). We also present two data structures for the general
case; one where the space is increased by \\(O(z\lg\lg z)\\), and one where the
query time changes from worst-case to expected. These results improve the
previously best known solutions. Notably, this is the first data structure that
decides if \\(P\\) occurs in \\(S\\) in \\(O(m)\\) time using \\(O(z\lg(n/z))\\) space.
  Our results are mainly obtained by a novel combination of a randomized
grammar construction algorithm with well known techniques relating pattern
matching to 2D-range reporting.