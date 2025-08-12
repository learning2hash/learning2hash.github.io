---
layout: publication
title: Itemsets For Real-valued Datasets
authors: Nikolaj Tatti
conference: 2013 IEEE 13th International Conference on Data Mining
year: 2013
bibkey: tatti2013itemsets
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.00804'}]
tags: ["Datasets"]
short_authors: Nikolaj Tatti
---
Pattern mining is one of the most well-studied subfields in exploratory data
analysis. While there is a significant amount of literature on how to discover
and rank itemsets efficiently from binary data, there is surprisingly little
research done in mining patterns from real-valued data. In this paper we
propose a family of quality scores for real-valued itemsets. We approach the
problem by considering casting the dataset into a binary data and computing the
support from this data. This naive approach requires us to select thresholds.
To remedy this, instead of selecting one set of thresholds, we treat thresholds
as random variables and compute the average support. We show that we can
compute this support efficiently, and we also introduce two normalisations,
namely comparing the support against the independence assumption and, more
generally, against the partition assumption. Our experimental evaluation
demonstrates that we can discover statistically significant patterns
efficiently.