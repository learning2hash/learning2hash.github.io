---
layout: publication
title: Codes With Unequal Locality
authors: Swanand Kadhe, Alex Sprintson
conference: 2016 IEEE International Symposium on Information Theory (ISIT)
year: 2016
bibkey: kadhe2016codes
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.06153'}]
tags: ["Compact Codes", "Locality Sensitive Hashing"]
short_authors: Swanand Kadhe, Alex Sprintson
---
For a code \(\code\), its \(i\)-th symbol is said to have locality \(r\) if its
value can be recovered by accessing some other \(r\) symbols of \(\code\). Locally
repairable codes (LRCs) are the family of codes such that every symbol has
locality \(r\).
  In this paper, we focus on (linear) codes whose individual symbols can be
partitioned into disjoint subsets such that the symbols in one subset have
different locality than the symbols in other. We call such codes as "codes with
unequal locality". For codes with "unequal information locality", we compute a
tight upper bound on the minimum distance as a function of number of
information symbols of each locality. We demonstrate that the construction of
Pyramid codes can be adapted to design codes with unequal information locality
that achieve the minimum distance bound. This result generalizes the classical
result of Gopalan et al. for codes with unequal locality. Next, we consider
codes with "unequal all symbol locality", and establish an upper bound on the
minimum distance as a function of number of symbols of each locality. We show
that the construction based on rank-metric codes by Silberstein et al. can be
adapted to obtain codes with unequal all symbol locality that achieve the
minimum distance bound. Finally, we introduce the concept of "locality
requirement" on a code, which can be viewed as a recoverability requirement on
symbols. Information locality requirement on a code essentially specifies the
minimum number of information symbols of different localities that must be
present in the code. We present a greedy algorithm that assigns localities to
information symbols so as to maximize the minimum distance among all codes that
satisfy a given locality requirement.