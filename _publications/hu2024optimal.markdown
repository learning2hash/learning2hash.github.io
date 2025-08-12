---
layout: publication
title: Optimal Static Dictionary With Worst-case Constant Query Time
authors: Yang Hu, Jingxun Liang, Huacheng Yu, Junkai Zhang, Renfei Zhou
conference: Proceedings of the 57th Annual ACM Symposium on Theory of Computing
year: 2025
bibkey: hu2024optimal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.10655'}]
tags: ["Efficiency"]
short_authors: Hu et al.
---
In this paper, we design a new succinct static dictionary with worst-case
constant query time. A dictionary data structure stores a set of key-value
pairs with distinct keys in \\([U]\\) and values in \\([\sigma]\\), such that given a
query \\(x\in [U]\\), it quickly returns if \\(x\\) is one of the input keys, and if
so, also returns its associated value. The textbook solution to dictionaries is
hash tables. On the other hand, the (information-theoretical) optimal space to
encode such a set of key-value pairs is only \\(\text\{OPT\} :=
log\binom\{U\}\{n\}+nlog \sigma\\).
  We construct a dictionary that uses \\(\text\{OPT\} + n^\{\epsilon\}\\) bits of
space, and answers queries in constant time in worst case. Previously,
constant-time dictionaries are only known with \\(\text\{OPT\} + n/\text\{poly\}log
n\\) space [P\v\{a\}tra\c\{s\}cu 2008], or with \\(\text\{OPT\}+n^\{\epsilon\}\\) space but
expected constant query time [Yu 2020]. We emphasize that most of the extra
\\(n^\{\epsilon\}\\) bits are used to store a lookup table that does not depend on
the input, and random bits for hash functions. The "main" data structure only
occupies \\(\text\{OPT\}+\text\{poly\}log n\\) bits.