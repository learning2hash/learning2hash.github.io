---
layout: publication
title: Inducing The Lyndon Array
authors: Felipe A. Louza, Sabrina Mantaci, Giovanni Manzini, Marinella Sciortino,
  Guilherme P. Telles
conference: Lecture Notes in Computer Science
year: 2019
bibkey: louza2019inducing
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.12987'}]
tags: []
short_authors: Louza et al.
---
In this paper we propose a variant of the induced suffix sorting algorithm by
Nong (TOIS, 2013) that computes simultaneously the Lyndon array and the suffix
array of a text in \(O(n)\) time using \(\sigma + O(1)\) words of working space,
where \(n\) is the length of the text and \(\sigma\) is the alphabet size. Our
result improves the previous best space requirement for linear time computation
of the Lyndon array. In fact, all the known linear algorithms for Lyndon array
computation use suffix sorting as a preprocessing step and use \(O(n)\) words of
working space in addition to the Lyndon array and suffix array. Experimental
results with real and synthetic datasets show that our algorithm is not only
space-efficient but also fast in practice.