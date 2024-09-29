---
layout: publication
title: C45;minhash Rigorously Reducing K Permutations To Two
authors: Li Xiaoyun, Li Ping
conference: "Arxiv"
year: 2021
bibkey: li2021rigorously
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2109.03337"}
tags: ['ARXIV', 'Independent']
---
Minwise hashing (MinHash) is an important and practical algorithm for generating random hashes to approximate the Jaccard (resemblance) similarity in massive binary (0/1) data. The basic theory of MinHash requires applying hundreds or even thousands of independent random permutations to each data vector in the dataset in order to obtain reliable results for (e.g.) building large45;scale learning models or approximate near neighbor search in massive data. In this paper we propose 123;bf Circulant MinHash (C45;MinHash)125; and provide the surprising theoretical results that we just need textbf123;two125; independent random permutations. For C45;MinHash we first conduct an initial permutation on the data vector then we use a second permutation to generate hash values. Basically the second permutation is re45;used K times via circulant shifting to produce K hashes. Unlike classical MinHash these K hashes are obviously correlated but we are able to provide rigorous proofs that we still obtain an unbiased estimate of the Jaccard similarity and the theoretical variance is uniformly smaller than that of the classical MinHash with K independent permutations. The theoretical proofs of C45;MinHash require some non45;trivial efforts. Numerical experiments are conducted to justify the theory and demonstrate the effectiveness of C45;MinHash.
