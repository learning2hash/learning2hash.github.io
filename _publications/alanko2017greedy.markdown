---
layout: publication
title: Greedy Shortest Common Superstring Approximation In Compact Space
authors: Jarno Alanko, Tuukka Norri
conference: Lecture Notes in Computer Science
year: 2017
bibkey: alanko2017greedy
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07727'}]
tags: []
short_authors: Jarno Alanko, Tuukka Norri
---
Given a set of strings, the shortest common superstring problem is to find
the shortest possible string that contains all the input strings. The problem
is NP-hard, but a lot of work has gone into designing approximation algorithms
for solving the problem. We present the first time and space efficient
implementation of the classic greedy heuristic which merges strings in
decreasing order of overlap length. Our implementation works in \(O(n log
\sigma)\) time and bits of space, where \(n\) is the total length of the input
strings in characters, and \(\sigma\) is the size of the alphabet. After index
construction, a practical implementation of our algorithm uses roughly \(5 n
log \sigma\) bits of space and reasonable time for a real dataset that consists
of DNA fragments.