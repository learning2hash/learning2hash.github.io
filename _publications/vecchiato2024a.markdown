---
layout: publication
title: A Learning-to-rank Formulation Of Clustering-based Approximate Nearest Neighbor
  Search
authors: Thomas Vecchiato, Claudio Lucchese, Franco Maria Nardini, Sebastian Bruch
conference: Proceedings of the 47th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2024
bibkey: vecchiato2024a
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.11731'}]
tags: [SIGIR, Datasets]
short_authors: Vecchiato et al.
---
A critical piece of the modern information retrieval puzzle is approximate
nearest neighbor search. Its objective is to return a set of \(k\) data points
that are closest to a query point, with its accuracy measured by the proportion
of exact nearest neighbors captured in the returned set. One popular approach
to this question is clustering: The indexing algorithm partitions data points
into non-overlapping subsets and represents each partition by a point such as
its centroid. The query processing algorithm first identifies the nearest
clusters -- a process known as routing -- then performs a nearest neighbor
search over those clusters only. In this work, we make a simple observation:
The routing function solves a ranking problem. Its quality can therefore be
assessed with a ranking metric, making the function amenable to
learning-to-rank. Interestingly, ground-truth is often freely available: Given
a query distribution in a top-\(k\) configuration, the ground-truth is the set of
clusters that contain the exact top-\(k\) vectors. We develop this insight and
apply it to Maximum Inner Product Search (MIPS). As we demonstrate empirically
on various datasets, learning a simple linear function consistently improves
the accuracy of clustering-based MIPS.