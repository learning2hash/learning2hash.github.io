---
layout: publication
title: On Finding Similar Items In A Stream Of Transactions
authors: Andrea Campagna, Rasmus Pagh
conference: 2010 IEEE International Conference on Data Mining Workshops
year: 2010
bibkey: campagna2010finding
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1010.2371'}]
tags: ["Recommender Systems", "Scalability", "Similarity Search"]
short_authors: Andrea Campagna, Rasmus Pagh
---
While there has been a lot of work on finding frequent itemsets in
transaction data streams, none of these solve the problem of finding similar
pairs according to standard similarity measures. This paper is a first attempt
at dealing with this, arguably more important, problem. We start out with a
negative result that also explains the lack of theoretical upper bounds on the
space usage of data mining algorithms for finding frequent itemsets: Any
algorithm that (even only approximately and with a chance of error) finds the
most frequent k-itemset must use space Omega(min\{mb,n^k,(mb/phi)^k\}) bits,
where mb is the number of items in the stream so far, n is the number of
distinct items and phi is a support threshold. To achieve any non-trivial space
upper bound we must thus abandon a worst-case assumption on the data stream. We
work under the model that the transactions come in random order, and show that
surprisingly, not only is small-space similarity mining possible for the most
common similarity measures, but the mining accuracy improves with the length of
the stream for any fixed support threshold.