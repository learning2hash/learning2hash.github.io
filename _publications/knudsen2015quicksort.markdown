---
layout: publication
title: Quicksort Largest Bucket and Min-Wise Hashing with Limited Independence
authors: Knudsen Mathias Bæk Tejs, Stöckel Morten
conference: "Arxiv"
year: 2015
bibkey: knudsen2015quicksort
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1502.05729"}
tags: ['ARXIV']
---
Randomized algorithms and data structures are often analyzed under the assumption of access to a perfect source of randomness. The most fundamental metric used to measure how random a hash function or a random number generator is is its independence a sequence of random variables is said to be k-independent if every variable is uniform and every size k subset is independent. In this paper we consider three classic algorithms under limited independence. We provide new bounds for randomized quicksort min-wise hashing and largest bucket size under limited independence. Our results can be summarized as follows. -Randomized quicksort. When pivot elements are computed using a 5-independent hash function Karloff and Raghavan J.ACM93 showed O ( n log n) expected worst-case running time for a special version of quicksort. We improve upon this showing that the same running time is achieved with only 4-independence. -Min-wise hashing. For a set A consider the probability of a particular element being mapped to the smallest hash value. It is known that 5-independence implies the optimal probability O (1 /n). Broder et al. STOC98 showed that 2-independence implies it is O(1 / ). We show a matching lower bound as well as new tight bounds for 3- and 4-independent hash functions. -Largest bucket. We consider the case where n balls are distributed to n buckets using a k-independent hash function and analyze the largest bucket size. Alon et. al STOC97 showed that there exists a 2-independent hash function implying a bucket of size Omega ( n^1/2). We generalize the bound providing a k-independent family of functions that imply size Omega ( n^1/k).
