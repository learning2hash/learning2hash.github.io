---
layout: publication
title: Space-efficient Detection Of Unusual Words
authors: Djamal Belazzougui, Fabio Cunial
conference: Lecture Notes in Computer Science
year: 2015
bibkey: belazzougui2015space
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1508.02968'}]
tags: []
short_authors: Djamal Belazzougui, Fabio Cunial
---
Detecting all the strings that occur in a text more frequently or less
frequently than expected according to an IID or a Markov model is a basic
problem in string mining, yet current algorithms are based on data structures
that are either space-inefficient or incur large slowdowns, and current
implementations cannot scale to genomes or metagenomes in practice. In this
paper we engineer an algorithm based on the suffix tree of a string to use just
a small data structure built on the Burrows-Wheeler transform, and a stack of
\(O(\sigma^2log^2 n)\) bits, where \(n\) is the length of the string and \(\sigma\)
is the size of the alphabet. The size of the stack is \(o(n)\) except for very
large values of \(\sigma\). We further improve the algorithm by removing its time
dependency on \(\sigma\), by reporting only a subset of the maximal repeats and
of the minimal rare words of the string, and by detecting and scoring candidate
under-represented strings that \(\textit\{do not occur\}\) in the string. Our
algorithms are practical and work directly on the BWT, thus they can be
immediately applied to a number of existing datasets that are available in this
form, returning this string mining problem to a manageable scale.