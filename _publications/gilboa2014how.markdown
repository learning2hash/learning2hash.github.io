---
layout: publication
title: How Many Queries Are Needed To Distinguish A Truncated Random Permutation From
  A Random Function?
authors: Shoni Gilboa, Shay Gueron, Ben Morris
conference: Journal of Cryptology
year: 2017
bibkey: gilboa2014how
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.5204'}]
tags: ["Privacy & Security"]
short_authors: Shoni Gilboa, Shay Gueron, Ben Morris
---
An oracle chooses a function \\(f\\) from the set of \\(n\\) bits strings to itself,
which is either a randomly chosen permutation or a randomly chosen function.
When queried by an \\(n\\)-bit string \\(w\\), the oracle computes \\(f(w)\\), truncates
the \\(m\\) last bits, and returns only the first \\(n-m\\) bits of \\(f(w)\\). How many
queries does a querying adversary need to submit in order to distinguish the
truncated permutation from the (truncated) function?
  In 1998, Hall et al. showed an algorithm for determining (with high
probability) whether or not \\(f\\) is a permutation, using \\(O(2^\{\frac\{m+n\}\{2\}\})\\)
queries. They also showed that if \\(m < n/7\\), a smaller number of queries will
not suffice. For \\(m > n/7\\), their method gives a weaker bound. In this note, we
first show how a modification of the approximation method used by Hall et al.
can solve the problem completely. It extends the result to practically any \\(m\\),
showing that \\(Ω(2^\{\frac\{m+n\}\{2\}\})\\) queries are needed to get a
non-negligible distinguishing advantage. However, more surprisingly, a better
bound for the distinguishing advantage can be obtained from a result of Stam
published, in a different context, already in 1978. We also show that, at least
in some cases, Stam's bound is tight.