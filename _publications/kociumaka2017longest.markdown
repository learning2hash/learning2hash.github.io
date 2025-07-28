---
layout: publication
title: Longest Common Substring With Approximately \(k\) Mismatches
authors: Tomasz Kociumaka, Jakub Radoszewski, Tatiana Starikovskaya
conference: Algorithmica
year: 2019
bibkey: kociumaka2017longest
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.08573'}]
tags: []
short_authors: Tomasz Kociumaka, Jakub Radoszewski, Tatiana Starikovskaya
---
In the longest common substring problem, we are given two strings of length
\\(n\\) and must find a substring of maximal length that occurs in both strings. It
is well known that the problem can be solved in linear time, but the solution
is not robust and can vary greatly when the input strings are changed even by
one character. To circumvent this, Leimeister and Morgenstern introduced the
problem of the longest common substring with \\(k\\) mismatches. Lately, this
problem has received a lot of attention in the literature. In this paper, we
first show a conditional lower bound based on the SETH hypothesis implying that
there is little hope to improve existing solutions. We then introduce a new but
closely related problem of the longest common substring with approximately \\(k\\)
mismatches and use locality-sensitive hashing to show that it admits a solution
with strongly subquadratic running time. We also apply these results to obtain
a strongly subquadratic-time 2-approximation algorithm for the longest common
substring with \\(k\\) mismatches problem and show conditional hardness of
improving its approximation ratio.