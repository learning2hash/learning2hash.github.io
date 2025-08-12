---
layout: publication
title: The Tandem Duplication Distance Is Np-hard
authors: Manuel Lafond, Binhai Zhu, Peng Zou
conference: Arxiv
year: 2020
bibkey: lafond2019tandem
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.05266'}]
tags: ["Distance Metric Learning"]
short_authors: Manuel Lafond, Binhai Zhu, Peng Zou
---
In computational biology, tandem duplication is an important biological
phenomenon which can occur either at the genome or at the DNA level. A tandem
duplication takes a copy of a genome segment and inserts it right after the
segment - this can be represented as the string operation \\(AXB \Rightarrow
AXXB\\). For example, Tandem exon duplications have been found in many species
such as human, fly or worm, and have been largely studied in computational
biology. The Tandem Duplication (TD) distance problem we investigate in this
paper is defined as follows: given two strings \\(S\\) and \\(T\\) over the same
alphabet, compute the smallest sequence of tandem duplications required to
convert \\(S\\) to \\(T\\). The natural question of whether the TD distance can be
computed in polynomial time was posed in 2004 by Leupold et al. and had
remained open, despite the fact that tandem duplications have received much
attention ever since. In this paper, we prove that this problem is NP-hard. We
further show that this hardness holds even if all characters of \\(S\\) are
distinct. This is known as the exemplar TD distance, which is of special
relevance in bioinformatics. One of the tools we develop for the reduction is a
new problem called the Cost-Effective Subgraph, for which we obtain
W[1]-hardness results that might be of independent interest. We finally show
that computing the exemplar TD distance between \\(S\\) and \\(T\\) is fixed-parameter
tractable. Our results open the door to many other questions, and we conclude
with several open problems.