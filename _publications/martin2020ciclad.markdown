---
layout: publication
title: 'CICLAD: A Fast And Memory-efficient Closed Itemset Miner For Streams'
authors: Tomas Martin, Guy Francoeur, Petko Valtchev
conference: Proceedings of the 26th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2020
bibkey: martin2020ciclad
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.01946'}]
tags: ["Efficiency", "KDD"]
short_authors: Tomas Martin, Guy Francoeur, Petko Valtchev
---
Mining association rules from data streams is a challenging task due to the
(typically) limited resources available vs. the large size of the result.
Frequent closed itemsets (FCI) enable an efficient first step, yet current FCI
stream miners are not optimal on resource consumption, e.g. they store a large
number of extra itemsets at an additional cost. In a search for a better
storage-efficiency trade-off, we designed Ciclad,an intersection-based
sliding-window FCI miner. Leveraging in-depth insights into FCI evolution, it
combines minimal storage with quick access. Experimental results indicate
Ciclad's memory imprint is much lower and its performances globally better than
competitor methods.