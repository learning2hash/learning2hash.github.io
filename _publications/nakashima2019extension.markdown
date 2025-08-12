---
layout: publication
title: An Extension Of Linear-size Suffix Tries For Parameterized Strings
authors: Katsuhito Nakashima, Diptarama Hendrian, Ryo Yoshinaka, Ayumi Shinohara
conference: Arxiv
year: 2019
bibkey: nakashima2019extension
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.00216'}]
tags: []
short_authors: Nakashima et al.
---
In this paper, we propose a new indexing structure for parameterized strings
which we call PLSTs, by generalizing linear-size suffix tries for ordinary
strings. Two parameterized strings are said to match if there is a bijection on
the symbol set that makes the two coincide. PLSTs are applicable to the
parameterized pattern matching problem, which is to decide whether the input
parameterized text has a substring that matches the input parameterized
pattern. The size of PLSTs is linear in the text size, with which our algorithm
solves the parameterized pattern matching problem in linear time in the pattern
size. PLSTs can be seen as a compacted version of parameterized suffix tries
and a combination of linear-size suffix tries and parameterized suffix trees.
We experimentally show that PLSTs are more space efficient than parameterized
suffix trees for highly repetitive strings.