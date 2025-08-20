---
layout: publication
title: Efficient Construction Of Neighborhood Graphs By The Multiple Sorting Method
authors: Takeaki Uno, Masashi Sugiyama, Koji Tsuda
conference: Arxiv
year: 2009
bibkey: uno2009efficient
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0904.3151'}]
tags: [Evaluation, Efficiency, Locality Sensitive Hashing, Graph-based ANN]
short_authors: Takeaki Uno, Masashi Sugiyama, Koji Tsuda
---
Neighborhood graphs are gaining popularity as a concise data representation
in machine learning. However, naive graph construction by pairwise distance
calculation takes \(O(n^2)\) runtime for \(n\) data points and this is
prohibitively slow for millions of data points. For strings of equal length,
the multiple sorting method (Uno, 2008) can construct an \(\epsilon\)-neighbor
graph in \(O(n+m)\) time, where \(m\) is the number of \(\epsilon\)-neighbor pairs in
the data. To introduce this remarkably efficient algorithm to continuous
domains such as images, signals and texts, we employ a random projection method
to convert vectors to strings. Theoretical results are presented to elucidate
the trade-off between approximation quality and computation time. Empirical
results show the efficiency of our method in comparison to fast nearest
neighbor alternatives.