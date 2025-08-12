---
layout: publication
title: Compressing Multisets With Large Alphabets Using Bits-back Coding
authors: Daniel Severo, James Townsend, Ashish Khisti, Alireza Makhzani, Karen Ullrich
conference: IEEE Journal on Selected Areas in Information Theory 2023
year: 2021
bibkey: severo2021compressing
citations: 0
additional_links: [{name: Code, url: 'https://github.com/facebookresearch/multiset-compression'},
  {name: Paper, url: 'https://arxiv.org/abs/2107.09202'}]
tags: ["Compact Codes"]
short_authors: Severo et al.
---
Current methods which compress multisets at an optimal rate have
computational complexity that scales linearly with alphabet size, making them
too slow to be practical in many real-world settings. We show how to convert a
compression algorithm for sequences into one for multisets, in exchange for an
additional complexity term that is quasi-linear in sequence length. This allows
us to compress multisets of exchangeable symbols at an optimal rate, with
computational complexity decoupled from the alphabet size. The key insight is
to avoid encoding the multiset directly, and instead compress a proxy sequence,
using a technique called `bits-back coding'. We demonstrate the method
experimentally on tasks which are intractable with previous optimal-rate
methods: compression of multisets of images and JavaScript Object Notation
(JSON) files. Code for our experiments is available at
https://github.com/facebookresearch/multiset-compression.