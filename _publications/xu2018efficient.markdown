---
layout: publication
title: Efficient Taxonomic Similarity Joins With Adaptive Overlap Constraint
authors: Pengfei Xu, Jiaheng Lu
conference: Proceedings of the 27th ACM International Conference on Information and
  Knowledge Management
year: 2018
bibkey: xu2018efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.12123'}]
tags: ["CIKM", "Efficiency"]
short_authors: Pengfei Xu, Jiaheng Lu
---
A similarity join aims to find all similar pairs between two collections of
records. Established approaches usually deal with synthetic differences like
typos and abbreviations, but neglect the semantic relations between words. Such
relations, however, are helpful for obtaining high-quality joining results. In
this paper, we leverage the taxonomy knowledge (i.e., a set of IS-A
hierarchical relations) to define a similarity measure which finds
semantic-similar records from two datasets. Based on this measure, we develop a
similarity join algorithm with prefix filtering framework to prune away
irrelevant pairs effectively. Our technical contribution here is an algorithm
that judiciously selects critical parameters in a prefix filter to maximise its
filtering power, supported by an estimation technique and Monte Carlo
simulation process. Empirical experiments show that our proposed methods
exhibit high efficiency and scalability, outperforming the state-of-art by a
large margin.