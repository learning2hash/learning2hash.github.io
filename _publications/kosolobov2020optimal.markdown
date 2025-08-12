---
layout: publication
title: Optimal Skeleton Huffman Trees Revisited
authors: Dmitry Kosolobov, Oleg Merkurev
conference: Lecture Notes in Computer Science
year: 2020
bibkey: kosolobov2020optimal
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.05239'}]
tags: []
short_authors: Dmitry Kosolobov, Oleg Merkurev
---
A skeleton Huffman tree is a Huffman tree in which all disjoint maximal
perfect subtrees are shrunk into leaves. Skeleton Huffman trees, besides saving
storage space, are also used for faster decoding and for speeding up
Huffman-shaped wavelet trees. In 2017 Klein et al. introduced an optimal
skeleton tree: for given symbol frequencies, it has the least number of nodes
among all optimal prefix-free code trees (not necessarily Huffman's) with
shrunk perfect subtrees. Klein et al. described a simple algorithm that, for
fixed codeword lengths, finds a skeleton tree with the least number of nodes;
with this algorithm one can process each set of optimal codeword lengths to
find an optimal skeleton tree. However, there are exponentially many such sets
in the worst case. We describe an \(O(n^2log n)\)-time algorithm that, given \(n\)
symbol frequencies, constructs an optimal skeleton tree and its corresponding
optimal code.