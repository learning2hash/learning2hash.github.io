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
<p>Consistent sampling is a technique for specifying, in small space, a
subset <span class="math inline">\(S\)</span> of a potentially large
universe <span class="math inline">\(U\)</span> such that the elements
in <span class="math inline">\(S\)</span> satisfy a suitably chosen
sampling condition. Given a subset <span
class="math inline">\(\mathcal{I}\subseteq U\)</span> it should be
possible to quickly compute <span class="math inline">\(\mathcal{I}\cap
S\)</span>, i.e., the elements in <span
class="math inline">\(\mathcal{I}\)</span> satisfying the sampling
condition. Consistent sampling has important applications in similarity
estimation, and estimation of the number of distinct items in a data
stream. In this paper we generalize consistent sampling to the setting
where we are interested in sampling size-<span
class="math inline">\(k\)</span> subsets occurring in some set in a
collection of sets of bounded size <span
class="math inline">\(b\)</span>, where <span
class="math inline">\(k\)</span> is a small integer. This can be done by
applying standard consistent sampling to the <span
class="math inline">\(k\)</span>-subsets of each set, but that approach
requires time <span class="math inline">\(\Theta(b^k)\)</span>. Using a
carefully designed hash function, for a given sampling probability <span
class="math inline">\(p \in (0,1]\)</span>, we show how to improve the
time complexity to <span class="math inline">\(\Theta(b^{\lceil
k/2\rceil}\log \log b + pb^k)\)</span> in expectation, while maintaining
strong concentration bounds for the sample. The space usage of our
method is <span class="math inline">\(\Theta(b^{\lceil
k/4\rceil})\)</span>. We demonstrate the utility of our technique by
applying it to several well-studied data mining problems. We show how to
efficiently estimate the number of frequent <span
class="math inline">\(k\)</span>-itemsets in a stream of transactions
and the number of bipartite cliques in a graph given as incidence
stream. Further, building upon a recent work by Campagna et al., we show
that our approach can be applied to frequent itemset mining in a
parallel or distributed setting. We also present applications in graph
stream mining.</p>
