---
layout: publication
title: Consistent Subset Sampling
authors: Kutzkov Konstantin, Pagh Rasmus
conference: "Arxiv"
year: 2014
bibkey: kutzkov2014consistent
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1404.4693"}
tags: ['ARXIV', 'Graph', 'Independent']
---
Consistent sampling is a technique for specifying in small space a subset (S) of a potentially large universe (U) such that the elements in (S) satisfy a suitably chosen sampling condition. Given a subset (subseteq U) it should be possible to quickly compute (cap S) i.e. the elements in () satisfying the sampling condition. Consistent sampling has important applications in similarity estimation and estimation of the number of distinct items in a data stream. In this paper we generalize consistent sampling to the setting where we are interested in sampling size-(k) subsets occurring in some set in a collection of sets of bounded size (b) where (k) is a small integer. This can be done by applying standard consistent sampling to the (k)-subsets of each set but that approach requires time (Theta(b^k)). Using a carefully designed hash function for a given sampling probability (p in (01) we show how to improve the time complexity to (Theta(b^lceil k/2rceillog log b + pb^k)) in expectation while maintaining strong concentration bounds for the sample. The space usage of our method is (Theta(b^lceil k/4rceil)). We demonstrate the utility of our technique by applying it to several well-studied data mining problems. We show how to efficiently estimate the number of frequent (k)-itemsets in a stream of transactions and the number of bipartite cliques in a graph given as incidence stream. Further building upon a recent work by Campagna et al. we show that our approach can be applied to frequent itemset mining in a parallel or distributed setting. We also present applications in graph stream mining.
