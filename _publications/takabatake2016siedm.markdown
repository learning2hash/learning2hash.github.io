---
layout: publication
title: 'Siedm: An Efficient String Index And Search Algorithm For Edit Distance With
  Moves'
authors: Yoshimasa Takabatake, Kenta Nakashima, Tetsuji Kuboyama, Yasuo Tabei, Hiroshi
  Sakamoto
conference: Algorithms
year: 2016
bibkey: takabatake2016siedm
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.06688'}]
tags: ["Efficiency"]
short_authors: Takabatake et al.
---
Although several self-indexes for highly repetitive text collections exist,
developing an index and search algorithm with editing operations remains a
challenge. Edit distance with moves (EDM) is a string-to-string distance
measure that includes substring moves in addition to ordinal editing operations
to turn one string into another. Although the problem of computing EDM is
intractable, it has a wide range of potential applications, especially in
approximate string retrieval. Despite the importance of computing EDM, there
has been no efficient method for indexing and searching large text collections
based on the EDM measure. We propose the first algorithm, named string index
for edit distance with moves (siEDM), for indexing and searching strings with
EDM. The siEDM algorithm builds an index structure by leveraging the idea
behind the edit sensitive parsing (ESP), an efficient algorithm enabling
approximately computing EDM with guarantees of upper and lower bounds for the
exact EDM. siEDM efficiently prunes the space for searching query strings by
the proposed method, which enables fast query searches with the same guarantee
as ESP. We experimentally tested the ability of siEDM to index and search
strings on benchmark datasets, and we showed siEDM's efficiency.