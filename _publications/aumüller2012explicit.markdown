---
layout: publication
title: 'Explicit And Efficient Hash Families Suffice For Cuckoo Hashing With A Stash'
authors: Martin Aumüller, Martin Dietzfelbinger, Philipp Woelfel
conference: "Arxiv"
year: 2012
citations: 5
bibkey: aumüller2012explicit
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1204.4431'}
tags: ['Independent', 'Unimodal', 'Evaluation', 'Shallow', 'Hashing']
---
It is shown that for cuckoo hashing with a stash as proposed by Kirsch,
Mitzenmacher, and Wieder (2008) families of very simple hash functions can be
used, maintaining the favorable performance guarantees: with stash size \\(s\\) the
probability of a rehash is \\(O(1/n^\{s+1\})\\), and the evaluation time is \\(O(s)\\).
Instead of the full randomness needed for the analysis of Kirsch et al. and of
Kutzelnigg (2010) (resp. \\(\Theta(log n)\\)-wise independence for standard cuckoo
hashing) the new approach even works with 2-wise independent hash families as
building blocks. Both construction and analysis build upon the work of
Dietzfelbinger and Woelfel (2003). The analysis, which can also be applied to
the fully random case, utilizes a graph counting argument and is much simpler
than previous proofs. As a byproduct, an algorithm for simulating uniform
hashing is obtained. While it requires about twice as much space as the most
space efficient solutions, it is attractive because of its simple and direct
structure.
