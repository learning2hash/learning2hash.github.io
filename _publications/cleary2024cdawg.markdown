---
layout: publication
title: The CDAWG Index And Pattern Matching On Grammar-compressed Strings
authors: Alan M. Cleary, Joseph Winjum, Jordan Dood, Shunsuke Inenaga
conference: Arxiv
year: 2024
bibkey: cleary2024cdawg
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.08826'}]
tags: []
short_authors: Cleary et al.
---
The compact directed acyclic word graph (CDAWG) is the minimal compact
automaton that recognizes all the suffixes of a string. Classically the CDAWG
has been implemented as an index of the string it recognizes, requiring \(o(n)\)
space for a copy of the string \(T\) being indexed, where \(n=|T|\). In this work,
we propose using the CDAWG as an index for grammar-compressed strings. While
this enables all analyses supported by the CDAWG on any grammar-compressed
string, in this work we specifically consider pattern matching. Using the CDAWG
index, pattern matching can be performed on any grammar-compressed string in
\(\mathcal\{O\}(\text\{ra\}(m)+\text\{occ\})\) time while requiring only
\(\mathcal\{O\}(\text\{er\}(T))\) additional space, where \(m\) is the length of the
pattern, \(\text\{ra\}(m)\) is the grammar random access time, \(\text\{occ\}\) is the
number of occurrences of the pattern in \(T\), and \(\text\{er\}(T)\) is the number
of right-extensions of the maximal repeats in \(T\). Our experiments show that
even when using a na\"ive random access algorithm, the CDAWG index achieves
state of the art run-time performance for pattern matching on
grammar-compressed strings. Additionally, we find that all of the grammars
computed for our experiments are smaller than the number of right-extensions in
the string they produce and, thus, their CDAWGs are within the best known
\(\mathcal\{O\}(\text\{er\}(T))\) space asymptotic bound.