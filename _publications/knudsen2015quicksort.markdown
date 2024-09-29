---
layout: publication
title: Quicksort Largest Bucket And Min45;wise Hashing With Limited Independence
authors: Knudsen Mathias Bæk Tejs, Stöckel Morten
conference: "Arxiv"
year: 2015
bibkey: knudsen2015quicksort
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1502.05729"}
tags: ['ARXIV', 'Independent']
---
Randomized algorithms and data structures are often analyzed under the assumption of access to a perfect source of randomness. The most fundamental metric used to measure how random a hash function or a random number generator is is its independence a sequence of random variables is said to be k45;independent if every variable is uniform and every size k subset is independent. In this paper we consider three classic algorithms under limited independence. We provide new bounds for randomized quicksort min45;wise hashing and largest bucket size under limited independence. Our results can be summarized as follows. 45;Randomized quicksort. When pivot elements are computed using a 545;independent hash function Karloff and Raghavan J.ACM93 showed O ( n log n) expected worst45;case running time for a special version of quicksort. We improve upon this showing that the same running time is achieved with only 445;independence. 45;Min45;wise hashing. For a set A consider the probability of a particular element being mapped to the smallest hash value. It is known that 545;independence implies the optimal probability O (1 /n). Broder et al. STOC98 showed that 245;independence implies it is O(1 / sqrt123;A125;). We show a matching lower bound as well as new tight bounds for 345; and 445;independent hash functions. 45;Largest bucket. We consider the case where n balls are distributed to n buckets using a k45;independent hash function and analyze the largest bucket size. Alon et. al STOC97 showed that there exists a 245;independent hash function implying a bucket of size Omega ( n^123;1/2125;). We generalize the bound providing a k45;independent family of functions that imply size Omega ( n^123;1/k125;).
