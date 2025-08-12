---
layout: publication
title: Efficient Geometric-based Computation Of The String Subsequence Kernel
authors: Slimane Bellaouar, Hadda Cherroun, Djelloul Ziadi
conference: Data Mining and Knowledge Discovery
year: 2017
bibkey: bellaouar2015efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.07776'}]
tags: ["Efficiency"]
short_authors: Slimane Bellaouar, Hadda Cherroun, Djelloul Ziadi
---
Kernel methods are powerful tools in machine learning. They have to be
computationally efficient. In this paper, we present a novel Geometric-based
approach to compute efficiently the string subsequence kernel (SSK). Our main
idea is that the SSK computation reduces to range query problem. We started by
the construction of a match list \\(L(s,t)=\\{(i,j):s_\{i\}=t_\{j\}\\}\\) where \\(s\\) and
\\(t\\) are the strings to be compared; such match list contains only the required
data that contribute to the result. To compute efficiently the SSK, we extended
the layered range tree data structure to a layered range sum tree, a
range-aggregation data structure. The whole process takes \\( O(p|L|log|L|)\\)
time and \\(O(|L|log|L|)\\) space, where \\(|L|\\) is the size of the match list and
\\(p\\) is the length of the SSK. We present empiric evaluations of our approach
against the dynamic and the sparse programming approaches both on synthetically
generated data and on newswire article data. Such experiments show the
efficiency of our approach for large alphabet size except for very short
strings. Moreover, compared to the sparse dynamic approach, the proposed
approach outperforms absolutely for long strings.