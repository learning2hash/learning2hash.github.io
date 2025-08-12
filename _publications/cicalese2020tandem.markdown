---
layout: publication
title: The Tandem Duplication Distance Problem Is Hard Over Bounded Alphabets
authors: "Ferdinando Cicalese, Nicol\xF2 Pilati"
conference: Lecture Notes in Computer Science
year: 2021
bibkey: cicalese2020tandem
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.02338'}]
tags: []
short_authors: "Ferdinando Cicalese, Nicol\xF2 Pilati"
---
A tandem duplication denotes the process of inserting a copy of a segment of
DNA adjacent to its original position. More formally, a tandem duplication can
be thought of as an operation that converts a string \\(S = AXB\\) into a string \\(T
= AXXB.\\) As they appear to be involved in genetic disorders, tandem
duplications are widely studied in computational biology. Also, tandem
duplication mechanisms have been recently studied in different contexts, from
formal languages, to information theory, to error-correcting codes for DNA
storage systems.
  The problem of determining the complexity of computing the tandem duplication
distance between two given strings was proposed by [Leupold et al., 2004] and,
very recently, it was shown to be NP-hard for the case of unbounded alphabets
[Lafond et al., STACS2020]. In this paper, we significantly improve this result
and show that the tandem duplication distance problem is NP-hard already for
the case of strings over an alphabet of size \\(\leq 5.\\) We also study some
special classes of strings were it is possible to give linear time solutions to
the existence problem: given strings \\(S\\) and \\(T\\) over the same alphabet, decide
whether there exists a sequence of duplications converting \\(S\\) into \\(T\\). A
polynomial time algorithm that solves the existence problem was only known for
the case of the binary alphabet.