---
layout: publication
title: Fast Locality-sensitive Hashing Frameworks For Approximate Near Neighbor Search
authors: Christiani Tobias
conference: "Arxiv"
year: 2017
bibkey: christiani2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1708.07586"}
tags: ['ARXIV', 'FOCS', 'Independent', 'LSH']
---
<p>The Indyk-Motwani Locality-Sensitive Hashing (LSH) framework (STOC
1998) is a general technique for constructing a data structure to answer
approximate near neighbor queries by using a distribution <span
class="math inline">\(\mathcal{H}\)</span> over locality-sensitive hash
functions that partition space. For a collection of <span
class="math inline">\(n\)</span> points, after preprocessing, the query
time is dominated by <span class="math inline">\(O(n^{\rho} \log
n)\)</span> evaluations of hash functions from <span
class="math inline">\(\mathcal{H}\)</span> and <span
class="math inline">\(O(n^{\rho})\)</span> hash table lookups and
distance computations where <span class="math inline">\(\rho \in
(0,1)\)</span> is determined by the locality-sensitivity properties of
<span class="math inline">\(\mathcal{H}\)</span>. It follows from a
recent result by Dahlgaard et al. (FOCS 2017) that the number of
locality-sensitive hash functions can be reduced to <span
class="math inline">\(O(\log^2 n)\)</span>, leaving the query time to be
dominated by <span class="math inline">\(O(n^{\rho})\)</span> distance
computations and <span class="math inline">\(O(n^{\rho} \log n)\)</span>
additional word-RAM operations. We state this result as a general
framework and provide a simpler analysis showing that the number of
lookups and distance computations closely match the Indyk-Motwani
framework, making it a viable replacement in practice. Using ideas from
another locality-sensitive hashing framework by Andoni and Indyk (SODA
2006) we are able to reduce the number of additional word-RAM operations
to <span class="math inline">\(O(n^\rho)\)</span>.</p>
