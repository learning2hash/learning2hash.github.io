---
layout: publication
title: Fast Locality-sensitive Hashing Frameworks For Approximate Near Neighbor Search
authors: Tobias Christiani
conference: Lecture Notes in Computer Science
year: 2017
bibkey: christiani2017fast
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.07586'}]
tags: [Evaluation, Efficiency, Tools & Libraries, Hashing Methods, Locality Sensitive
    Hashing]
short_authors: Tobias Christiani
---
The Indyk-Motwani Locality-Sensitive Hashing (LSH) framework (STOC 1998) is a
general technique for constructing a data structure to answer approximate near
neighbor queries by using a distribution \(\mathcal\{H\}\) over locality-sensitive
hash functions that partition space. For a collection of \(n\) points, after
preprocessing, the query time is dominated by \(O(n^\{\rho\} log n)\) evaluations
of hash functions from \(\mathcal\{H\}\) and \(O(n^\{\rho\})\) hash table lookups and
distance computations where \(\rho \in (0,1)\) is determined by the
locality-sensitivity properties of \(\mathcal\{H\}\). It follows from a recent
result by Dahlgaard et al. (FOCS 2017) that the number of locality-sensitive
hash functions can be reduced to \(O(log^2 n)\), leaving the query time to be
dominated by \(O(n^\{\rho\})\) distance computations and \(O(n^\{\rho\} log n)\)
additional word-RAM operations. We state this result as a general framework and
provide a simpler analysis showing that the number of lookups and distance
computations closely match the Indyk-Motwani framework, making it a viable
replacement in practice. Using ideas from another locality-sensitive hashing
framework by Andoni and Indyk (SODA 2006) we are able to reduce the number of
additional word-RAM operations to \(O(n^\rho)\).