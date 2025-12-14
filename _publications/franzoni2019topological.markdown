---
layout: publication
title: Topological And Semantic Graph-based Author Disambiguation On DBLP Data In
  Neo4j
authors: Valentina Franzoni, Michele Lepri, Alfredo Milani
conference: AIKE 2018 239-243
year: 2019
bibkey: franzoni2019topological
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.08977'}]
tags: [Evaluation, Graph-based ANN]
short_authors: Valentina Franzoni, Michele Lepri, Alfredo Milani
---
In this work, we introduce a novel method for entity resolution author
disambiguation in bibliographic networks. Such a method is based on a 2-steps
network traversal using topological similarity measures for rating candidate
nodes. Topological similarity is widely used in the Link Prediction application
domain to assess the likelihood of an unknown link. A similarity function can
be a good approximation for equality, therefore can be used to disambiguate,
basing on the hypothesis that authors with many common co-authors are similar.
Our method has experimented on a graph-based representation of the public DBLP
Computer Science database. The results obtained are extremely encouraging
regarding Precision, Accuracy, and Specificity. Further good aspects are the
locality of the method for disambiguation assessment which avoids the need to
know the global network, and the exploitation of only a few data, e.g. author
name and paper title (i.e., co-authorship data).