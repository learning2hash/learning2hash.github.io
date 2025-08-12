---
layout: publication
title: Top-k Color Queries For Document Retrieval
authors: Marek Karpinski, Yakov Nekrich
conference: Arxiv
year: 2011
bibkey: karpinski2010top
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1007.1361'}]
tags: ["Text Retrieval"]
short_authors: Marek Karpinski, Yakov Nekrich
---
In this paper we describe a new efficient (in fact optimal) data structure
for the \{\em top-\\(K\\) color problem\}. Each element of an array \\(A\\) is assigned a
color \\(c\\) with priority \\(p(c)\\). For a query range \\([a,b]\\) and a value \\(K\\), we
have to report \\(K\\) colors with the highest priorities among all colors that
occur in \\(A[a..b]\\), sorted in reverse order by their priorities. We show that
such queries can be answered in \\(O(K)\\) time using an \\(O(Nlog \sigma)\\) bits
data structure, where \\(N\\) is the number of elements in the array and \\(\sigma\\)
is the number of colors. Thus our data structure is asymptotically optimal with
respect to the worst-case query time and space. As an immediate application of
our results, we obtain optimal time solutions for several document retrieval
problems. The method of the paper could be also of independent interest.