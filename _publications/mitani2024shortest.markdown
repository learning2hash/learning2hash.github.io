---
layout: publication
title: Shortest Cover After Edit
authors: Kazuki Mitani, Takuya Mieno, Kazuhisa Seto, Takashi Horiyama
conference: Arxiv
year: 2024
bibkey: mitani2024shortest
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.17428'}]
tags: []
short_authors: Mitani et al.
---
This paper investigates the (quasi-)periodicity of a string when the string
is edited. A string \(C\) is called a cover (as known as a quasi-period) of a
string \(T\) if each character of \(T\) lies within some occurrence of \(C\). By
definition, a cover of \(T\) must be a border of \(T\); that is, it occurs both as
a prefix and as a suffix of \(T\). In this paper, we focus on the changes in the
longest border and the shortest cover of a string when the string is edited
only once. We propose a data structure of size \(O(n)\) that computes the longest
border and the shortest cover of the string in \(O(\ell log n)\) time after an
edit operation (either insertion, deletion, or substitution of some string) is
applied to the input string \(T\) of length \(n\), where \(\ell\) is the length of
the string being inserted or substituted. The data structure can be constructed
in \(O(n)\) time given string \(T\).