---
layout: publication
title: Full-text And Keyword Indexes For String Searching
authors: "Aleksander Cis\u0142ak"
conference: Arxiv
year: 2015
bibkey: "cis\u0142ak2015full"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1508.06610'}]
tags: []
short_authors: "Aleksander Cis\u0142ak"
---
In this work, we present a literature review for full-text and keyword
indexes as well as our contributions (which are mostly practice-oriented).
  The first contribution is the FM-bloated index, which is a modification of
the well-known FM-index (a compressed, full-text index) that trades space for
speed. In our approach, the count table and the occurrence lists store
information about selected \(q\)-grams in addition to the individual characters.
Two variants are described, namely one using \(O(n log^2 n)\) bits of space with
\(O(m + log m log log n)\) average query time, and one with linear space and
\(O(m log log n)\) average query time, where \(n\) is the input text length and
\(m\) is the pattern length. We experimentally show that a significant speedup
can be achieved by operating on \(q\)-grams (albeit at the cost of very high
space requirements, hence the name "bloated").
  In the category of keyword indexes we present the so-called split index,
which can efficiently solve the \(k\)-mismatches problem, especially for 1 error.
Our implementation in the C++ language is focused mostly on data compaction,
which is beneficial for the search speed (by being cache friendly). We compare
our solution with other algorithms and we show that it is faster when the
Hamming distance is used. Query times in the order of 1 microsecond were
reported for one mismatch for a few-megabyte natural language dictionary on a
medium-end PC.
  A minor contribution includes string sketches which aim to speed up
approximate string comparison at the cost of additional space (\(O(1)\) per
string). They can be used in the context of keyword indexes in order to deduce
that two strings differ by at least \(k\) mismatches with the use of fast bitwise
operations rather than an explicit verification.