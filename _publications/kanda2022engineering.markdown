---
layout: publication
title: Engineering Faster Double-array Aho-corasick Automata
authors: Shunsuke Kanda, Koichi Akabe, Yusuke Oda
conference: 'Software: Practice and Experience'
year: 2023
bibkey: kanda2022engineering
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.13870'}]
tags: []
short_authors: Shunsuke Kanda, Koichi Akabe, Yusuke Oda
---
Multiple pattern matching in strings is a fundamental problem in text
processing applications such as regular expressions or tokenization. This paper
studies efficient implementations of double-array Aho-Corasick automata
(DAACs), data structures for quickly performing the multiple pattern matching.
The practical performance of DAACs is improved by carefully designing the data
structure, and many implementation techniques have been proposed thus far. A
problem in DAACs is that their ideas are not aggregated. Since comprehensive
descriptions and experimental analyses are unavailable, engineers face
difficulties in implementing an efficient DAAC.
  In this paper, we review implementation techniques for DAACs and provide a
comprehensive description of them. We also propose several new techniques for
further improvement. We conduct exhaustive experiments through real-world
datasets and reveal the best combination of techniques to achieve a higher
performance in DAACs. The best combination is different from those used in the
most popular libraries of DAACs, which demonstrates that their performance can
be further enhanced. On the basis of our experimental analysis, we developed a
new Rust library for fast multiple pattern matching using DAACs, named
Daachorse, as open-source software at https://github.com/daac-tools/daachorse.
Experiments demonstrate that Daachorse outperforms other AC-automaton
implementations, indicating its suitability as a fast alternative for multiple
pattern matching in many applications.