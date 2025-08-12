---
layout: publication
title: An Encoding For Order-preserving Matching
authors: Travis Gagie, Giovanni Manzini, Rossano Venturini
conference: Arxiv
year: 2017
bibkey: gagie2016encoding
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.02865'}]
tags: []
short_authors: Travis Gagie, Giovanni Manzini, Rossano Venturini
---
Encoding data structures store enough information to answer the queries they
are meant to support but not enough to recover their underlying datasets. In
this paper we give the first encoding data structure for the challenging
problem of order-preserving pattern matching. This problem was introduced only
a few years ago but has already attracted significant attention because of its
applications in data analysis. Two strings are said to be an order-preserving
match if the \{\em relative order\} of their characters is the same: e.g., \\(4, 1,
3, 2\\) and \\(10, 3, 7, 5\\) are an order-preserving match. We show how, given a
string \\(S [1..n]\\) over an arbitrary alphabet and a constant \\(c \geq 1\\), we can
build an \\(O (n log log n)\\)-bit encoding such that later, given a pattern \\(P
[1..m]\\) with \\(m \leq \lg^c n\\), we can return the number of order-preserving
occurrences of \\(P\\) in \\(S\\) in \\(O (m)\\) time. Within the same time bound we can
also return the starting position of some order-preserving match for \\(P\\) in \\(S\\)
(if such a match exists). We prove that our space bound is within a constant
factor of optimal; our query time is optimal if \\(log \sigma = Ω(log n)\\).
Our space bound contrasts with the \\(Ω (n log n)\\) bits needed in the worst
case to store \\(S\\) itself, an index for order-preserving pattern matching with
no restrictions on the pattern length, or an index for standard pattern
matching even with restrictions on the pattern length. Moreover, we can build
our encoding knowing only how each character compares to \\(O (\lg^c n)\\)
neighbouring characters.