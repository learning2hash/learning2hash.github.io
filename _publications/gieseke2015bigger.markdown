---
layout: publication
title: Bigger Buffer K-d Trees On Multi-many-core Systems
authors: Fabian Gieseke, Cosmin Eugen Oancea, Ashish Mahabal, Christian Igel, Tom
  Heskes
conference: Arxiv
year: 2015
bibkey: gieseke2015bigger
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.02831'}]
tags: [Tools & Libraries, Tree-based ANN]
short_authors: Gieseke et al.
---
A buffer k-d tree is a k-d tree variant for massively-parallel nearest
neighbor search. While providing valuable speed-ups on modern many-core devices
in case both a large number of reference and query points are given, buffer k-d
trees are limited by the amount of points that can fit on a single device. In
this work, we show how to modify the original data structure and the associated
workflow to make the overall approach capable of dealing with massive data
sets. We further provide a simple yet efficient way of using multiple devices
given in a single workstation. The applicability of the modified framework is
demonstrated in the context of astronomy, a field that is faced with huge
amounts of data.