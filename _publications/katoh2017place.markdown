---
layout: publication
title: In-place Initializable Arrays
authors: Takashi Katoh, Keisuke Goto
conference: Theoretical Computer Science
year: 2022
bibkey: katoh2017place
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.08900'}]
tags: []
short_authors: Takashi Katoh, Keisuke Goto
---
An initializable array is an array that supports the read and write
operations for any element and the initialization of the entire array. This
paper proposes a simple in-place algorithm to implement an initializable array
of length \\(N\\) containing \\(\ell \in O(w)\\) bits entries in \\(N \ell +1\\) bits on
the word RAM model with \\(w\\) bits word size, i.e., the proposed array requires
only 1 extra bit on top of a normal array of length \\(N\\) containing \\(\ell\\) bits
entries. Our algorithm supports the all three operations in constant worst-case
time, that is, it runs in-place using at most constant number of words \\(O(w)\\)
bits during each operation. The time and space complexities are optimal since
it was already proven that there is no implementation of an initializable array
with no extra bit supporting all the operations in constant worst-case time
[Hagerup and Kammer, ISAAC 2017]. Our algorithm significantly improves upon the
best algorithm presented in the earlier studies [Navarro, CSUR 2014] which uses
\\(N + o(N)\\) extra bits to support all the operations in constant worst-case
time.