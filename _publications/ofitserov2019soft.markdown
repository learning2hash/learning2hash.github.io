---
layout: publication
title: Soft Edit Distance For Differentiable Comparison Of Symbolic Sequences
authors: Evgenii Ofitserov, Vasily Tsvetkov, Vadim Nazarov
conference: Arxiv
year: 2019
bibkey: ofitserov2019soft
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.12562'}]
tags: []
short_authors: Evgenii Ofitserov, Vasily Tsvetkov, Vadim Nazarov
---
Edit distance, also known as Levenshtein distance, is an essential way to
compare two strings that proved to be particularly useful in the analysis of
genetic sequences and natural language processing. However, edit distance is a
discrete function that is known to be hard to optimize. This fact hampers the
use of this metric in Machine Learning. Even as simple algorithm as K-means
fails to cluster a set of sequences using edit distance if they are of variable
length and abundance. In this paper we propose a novel metric - soft edit
distance (SED), which is a smooth approximation of edit distance. It is
differentiable and therefore it is possible to optimize it with gradient
methods. Similar to original edit distance, SED as well as its derivatives can
be calculated with recurrent formulas at polynomial time. We prove usefulness
of the proposed metric on synthetic datasets and clustering of biological
sequences.