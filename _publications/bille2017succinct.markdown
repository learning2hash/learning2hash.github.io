---
layout: publication
title: Succinct Partial Sums And Fenwick Trees
authors: Philip Bille, Anders Roy Christiansen, Nicola Prezza, Frederik Rye Skjoldjensen
conference: Lecture Notes in Computer Science
year: 2017
bibkey: bille2017succinct
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.10987'}]
tags: ["Tree Based ANN"]
short_authors: Bille et al.
---
We consider the well-studied partial sums problem in succint space where one
is to maintain an array of n k-bit integers subject to updates such that
partial sums queries can be efficiently answered. We present two succint
versions of the Fenwick Tree - which is known for its simplicity and
practicality. Our results hold in the encoding model where one is allowed to
reuse the space from the input data. Our main result is the first that only
requires nk + o(n) bits of space while still supporting sum/update in O(log_b
n) / O(b log_b n) time where 2 <= b <= log^O(1) n. The second result shows how
optimal time for sum/update can be achieved while only slightly increasing the
space usage to nk + o(nk) bits. Beyond Fenwick Trees, the results are primarily
based on bit-packing and sampling - making them very practical - and they also
allow for simple optimal parallelization.