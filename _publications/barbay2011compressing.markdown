---
layout: publication
title: On Compressing Permutations And Adaptive Sorting
authors: "J\xE9r\xE9my Barbay, Gonzalo Navarro"
conference: Theoretical Computer Science
year: 2013
bibkey: barbay2011compressing
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1108.4408'}]
tags: []
short_authors: "J\xE9r\xE9my Barbay, Gonzalo Navarro"
---
Previous compact representations of permutations have focused on adding a
small index on top of the plain data \\(<\pi(1), \pi(2),...\pi(n)>\\), in order to
efficiently support the application of the inverse or the iterated permutation.
  In this paper we initiate the study of techniques that exploit the
compressibility of the data itself, while retaining efficient computation of
\\(\pi(i)\\) and its inverse.
  In particular, we focus on exploiting \{\em runs\}, which are subsets
(contiguous or not) of the domain where the permutation is monotonic.
  Several variants of those types of runs arise in real applications such as
inverted indexes and suffix arrays.
  Furthermore, our improved results on compressed data structures for
permutations also yield better adaptive sorting algorithms.