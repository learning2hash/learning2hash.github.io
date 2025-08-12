---
layout: publication
title: Deterministic Sparse Suffix Sorting In The Restore Model
authors: "Johannes Fischer, Tomohiro I, Dominik K\xF6ppl"
conference: ACM Transactions on Algorithms
year: 2020
bibkey: fischer2015deterministic
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.07417'}]
tags: []
short_authors: "Johannes Fischer, Tomohiro I, Dominik K\xF6ppl"
---
Given a text \\(T\\) of length \\(n\\), we propose a deterministic online algorithm
computing the sparse suffix array and the sparse longest common prefix array of
\\(T\\) in \\(O(c \sqrt\{\lg n\} + m \lg m \lg n \lg^* n)\\) time with \\(O(m)\\) words of
space under the premise that the space of \\(T\\) is rewritable, where \\(m \le n\\) is
the number of suffixes to be sorted (provided online and arbitrarily), and \\(c\\)
is the number of characters with \\(m \le c \le n\\) that must be compared for
distinguishing the designated suffixes.