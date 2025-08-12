---
layout: publication
title: The Parameterized Suffix Tray
authors: Noriki Fujisato, Yuto Nakashima, Shunsuke Inenaga, Hideo Bannai, Masayuki
  Takeda
conference: Arxiv
year: 2020
bibkey: fujisato2020parameterized
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.10092'}]
tags: []
short_authors: Fujisato et al.
---
Let \(\Sigma\) and \(\Pi\) be disjoint alphabets, respectively called the static
alphabet and the parameterized alphabet. Two strings \(x\) and \(y\) over \(\Sigma
\cup \Pi\) of equal length are said to parameterized match (p-match) if there
exists a renaming bijection \(f\) on \(\Sigma\) and \(\Pi\) which is identity on
\(\Sigma\) and maps the characters of \(x\) to those of \(y\) so that the two strings
become identical. The indexing version of the problem of finding p-matching
occurrences of a given pattern in the text is a well-studied topic in string
matching. In this paper, we present a state-of-the-art indexing structure for
p-matching called the parameterized suffix tray of an input text \(T\), denoted
by \(\mathsf\{PSTray\}(T)\). We show that \(\mathsf\{PSTray\}(T)\) occupies \(O(n)\)
space and supports pattern matching queries in \(O(m + log (\sigma+\pi) +
\mathit\{occ\})\) time, where \(n\) is the length of \(T\), \(m\) is the length of a
query pattern \(P\), \(\pi\) is the number of distinct symbols of \(|\Pi|\) in \(T\),
\(\sigma\) is the number of distinct symbols of \(|\Sigma|\) in \(T\) and
\(\mathit\{occ\}\) is the number of p-matching occurrences of \(P\) in \(T\). We also
present how to build \(\mathsf\{PSTray\}(T)\) in \(O(n)\) time from the parameterized
suffix tree of \(T\).