---
layout: publication
title: A Fast Algorithm For Constructing Balanced Binary Search Trees
authors: Pavel S. Ruzankin
conference: SN Computer Science 3 article 67 (2022)
year: 2019
bibkey: ruzankin2019fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.02499'}]
tags: ["Efficiency", "Tree Based ANN"]
short_authors: Pavel S. Ruzankin
---
We suggest a new non-recursive algorithm for constructing a binary search
tree given an array of numbers. The algorithm has \(O(N)\) time and \(O(1)\) memory
complexity if the given array of \(N\) numbers is sorted. The resulting tree is
of minimal height and can be transformed to a complete binary search tree
(retaining minimal height) with \(O(log N)\) time and \(O(1)\) memory.
  The algorithm allows simple and effective parallelization.