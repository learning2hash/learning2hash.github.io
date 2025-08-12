---
layout: publication
title: 'Tree Edit Distance Learning Via Adaptive Symbol Embeddings: Supplementary
  Materials And Results'
authors: "Benjamin Paa\xDFen"
conference: Arxiv
year: 2018
bibkey: "paa\xDFen2018tree"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.07123'}]
tags: ["Distance Metric Learning"]
short_authors: "Benjamin Paa\xDFen"
---
Metric learning has the aim to improve classification accuracy by learning a
distance measure which brings data points from the same class closer together
and pushes data points from different classes further apart. Recent research
has demonstrated that metric learning approaches can also be applied to trees,
such as molecular structures, abstract syntax trees of computer programs, or
syntax trees of natural language, by learning the cost function of an edit
distance, i.e. the costs of replacing, deleting, or inserting nodes in a tree.
However, learning such costs directly may yield an edit distance which violates
metric axioms, is challenging to interpret, and may not generalize well. In
this contribution, we propose a novel metric learning approach for trees which
learns an edit distance indirectly by embedding the tree nodes as vectors, such
that the Euclidean distance between those vectors supports class
discrimination. We learn such embeddings by reducing the distance to
prototypical trees from the same class and increasing the distance to
prototypical trees from different classes. In our experiments, we show that our
proposed metric learning approach improves upon the state-of-the-art in metric
learning for trees on six benchmark data sets, ranging from computer science
over biomedical data to a natural-language processing data set containing over
300,000 nodes.