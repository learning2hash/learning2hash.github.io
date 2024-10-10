---
layout: publication
title: Improved Densification Of One Permutation Hashing
authors: Shrivastava Anshumali, Li Ping
conference: "Arxiv"
year: 2014
bibkey: shrivastava2014improved
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1406.4784"}
tags: ['ARXIV', 'Independent', 'LSH']
---
The existing work on densification of one permutation hashing reduces the query processing cost of the ((KL))-parameterized Locality Sensitive Hashing (LSH) algorithm with minwise hashing from (O(dKL)) to merely (O(d + KL)) where (d) is the number of nonzeros of the data vector (K) is the number of hashes in each hash table and (L) is the number of hash tables. While that is a substantial improvement our analysis reveals that the existing densification scheme is sub-optimal. In particular there is no enough randomness in that procedure which affects its accuracy on very sparse datasets. In this paper we provide a new densification procedure which is provably better than the existing scheme. This improvement is more significant for very sparse datasets which are common over the web. The improved technique has the same cost of (O(d + KL)) for query processing thereby making it strictly preferable over the existing procedure. Experimental evaluations on public datasets in the task of hashing based near neighbor search support our theoretical findings.
