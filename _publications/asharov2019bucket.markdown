---
layout: publication
title: 'Bucket Oblivious Sort: An Extremely Simple Oblivious Sort'
authors: Gilad Asharov, T-H. Hubert Chan, Kartik Nayak, Rafael Pass, Ling Ren, Elaine
  Shi
conference: Symposium on Simplicity in Algorithms
year: 2019
bibkey: asharov2019bucket
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.01765'}]
tags: []
short_authors: Asharov et al.
---
We propose a conceptually simple oblivious sort and oblivious random
permutation algorithms called bucket oblivious sort and bucket oblivious random
permutation. Bucket oblivious sort uses \(6nlog n\) time (measured by the number
of memory accesses) and \(2Z\) client storage with an error probability
exponentially small in \(Z\). The above runtime is only \(3\times\) slower than a
non-oblivious merge sort baseline; for \(2^\{30\}\) elements, it is \(5\times\)
faster than bitonic sort, the de facto oblivious sorting algorithm in practical
implementations.