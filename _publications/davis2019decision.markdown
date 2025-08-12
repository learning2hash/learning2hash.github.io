---
layout: publication
title: Decision-directed Data Decomposition
authors: Brent D. Davis, Ethan Jackson, Daniel J. Lizotte
conference: Arxiv
year: 2019
bibkey: davis2019decision
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.08159'}]
tags: []
short_authors: Brent D. Davis, Ethan Jackson, Daniel J. Lizotte
---
We present an algorithm, Decision-Directed Data Decomposition (D4), which
decomposes a dataset into two components. The first contains most of the useful
information for a specified supervised learning task. The second orthogonal
component contains little information about the task but retains associations
and information that were not targeted. The algorithm is simple and scalable.
We illustrate its application in image and text processing domains. Our results
show that 1) post-hoc application of D4 to an image representation space can
remove information about specified concepts without impacting other concepts,
2) D4 is able to improve predictive generalization in certain settings, and 3)
applying D4 to word embedding representations produces state-of-the-art results
in debiasing.