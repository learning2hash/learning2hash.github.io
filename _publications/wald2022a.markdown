---
layout: publication
title: A Stack-free Traversal Algorithm For Left-balanced K-d Trees
authors: Ingo Wald
conference: Arxiv
year: 2022
bibkey: wald2022a
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.12859'}]
tags: [Tree-based ANN]
short_authors: Ingo Wald
---
We present an algorithm that allows for find-closest-point and kNN-style
traversals of left-balanced k-d trees, without the need for either recursion or
software-managed stacks; instead using only current and last previously
traversed node to compute which node to traverse next.