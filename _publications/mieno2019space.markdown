---
layout: publication
title: Space-efficient Algorithms For Computing Minimal/shortest Unique Substrings
authors: "Takuya Mieno, Dominik K\xF6ppl, Yuto Nakashima, Shunsuke Inenaga, Hideo\
  \ Bannai, Masayuki Takeda"
conference: Theoretical Computer Science
year: 2020
bibkey: mieno2019space
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.12854'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Mieno et al.
---
Given a string \\(T\\) of length \\(n\\), a substring \\(u = T[i..j]\\) of \\(T\\) is called
a shortest unique substring (SUS) for an interval \\([s,t]\\) if (a) \\(u\\) occurs
exactly once in \\(T\\), (b) \\(u\\) contains the interval \\([s,t]\\) (i.e. \\(i \leq s \leq
t \leq j\\)), and (c) every substring \\(v\\) of \\(T\\) with \\(|v| < |u|\\) containing
\\([s,t]\\) occurs at least twice in \\(T\\). Given a query interval \\([s, t] \subset
[1, n]\\), the interval SUS problem is to output all the SUSs for the interval
\\([s,t]\\). In this article, we propose a \\(4n + o(n)\\) bits data structure
answering an interval SUS query in output-sensitive \\(O(\mathit\{occ\})\\) time,
where \\(\mathit\{occ\}\\) is the number of returned SUSs. Additionally, we focus on
the point SUS problem, which is the interval SUS problem for \\(s = t\\). Here, we
propose a \\(\lceil (log_2\{3\} + 1)n \rceil + o(n)\\) bits data structure answering
a point SUS query in the same output-sensitive time. We also propose
space-efficient algorithms for computing the minimal unique substrings of \\(T\\).