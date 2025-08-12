---
layout: publication
title: 'Linear-size CDAWG: New Repetition-aware Indexing And Grammar Compression'
authors: Takuya Takagi, Keisuke Goto, Yuta Fujishige, Shunsuke Inenaga, Hiroki Arimura
conference: Lecture Notes in Computer Science
year: 2017
bibkey: takagi2017linear
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.09779'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Takagi et al.
---
In this paper, we propose a novel approach to combine *compact directed
acyclic word graphs* (CDAWGs) and grammar-based compression. This leads us to
an efficient self-index, called Linear-size CDAWGs (L-CDAWGs), which can be
represented with \(O(\tilde e_T log n)\) bits of space allowing for \(O(log
n)\)-time random and \(O(1)\)-time sequential accesses to edge labels, and \(O(m
log \sigma + occ)\)-time pattern matching. Here, \(\tilde e_T\) is the number of
all extensions of maximal repeats in \(T\), \(n\) and \(m\) are respectively the
lengths of the text \(T\) and a given pattern, \(\sigma\) is the alphabet size, and
\(occ\) is the number of occurrences of the pattern in \(T\). The repetitiveness
measure \(\tilde e_T\) is known to be much smaller than the text length \(n\) for
highly repetitive text. For constant alphabets, our L-CDAWGs achieve \(O(m +
occ)\) pattern matching time with \(O(e_T^r log n)\) bits of space, which
improves the pattern matching time of Belazzougui et al.'s run-length
BWT-CDAWGs by a factor of \(log log n\), with the same space complexity. Here,
\(e_T^r\) is the number of right extensions of maximal repeats in \(T\). As a
byproduct, our result gives a way of constructing an SLP of size \(O(\tilde
e_T)\) for a given text \(T\) in \(O(n + \tilde e_T log \sigma)\) time.