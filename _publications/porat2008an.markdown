---
layout: publication
title: An Optimal Bloom Filter Replacement Based on Matrix Solving
authors: Porat Ely
conference: Arxiv
year: 2008
bibkey: porat2008an
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/0804.1845"}
tags: ['Arxiv']
---
We suggest a method for holding a dictionary data structure, which maps keys to values, in the spirit of Bloom Filters. The space requirements of the dictionary we suggest are much smaller than those of a hashtable. We allow storing n keys, each mapped to value which is a string of k bits. Our suggested method requires nk + o(n) bits space to store the dictionary, and O(n) time to produce the data structure, and allows answering a membership query in O(1) memory probes. The dictionary size does not depend on the size of the keys. However, reducing the space requirements of the data structure comes at a certain cost. Our dictionary has a small probability of a one sided error. When attempting to obtain the value for a key that is stored in the dictionary we always get the correct answer. However, when testing for membership of an element that is not stored in the dictionary, we may get an incorrect answer, and when requesting the value of such an element we may get a certain random value. Our method is based on solving equations in GF(2^k) and using several hash functions. Another significant advantage of our suggested method is that we do not require using sophisticated hash functions. We only require pairwise independent hash functions. We also suggest a data structure that requires only nk bits space, has O(n2) preprocessing time, and has a O(log n) query time. However, this data structures requires a uniform hash functions. In order replace a Bloom Filter of n elements with an error proability of 2^{-k}, we require nk + o(n) memory bits, O(1) query time, O(n) preprocessing time, and only pairwise independent hash function. Even the most advanced previously known Bloom Filter would require nk+O(n) space, and a uniform hash functions, so our method is significantly less space consuming especially when k is small.
