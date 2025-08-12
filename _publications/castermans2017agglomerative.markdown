---
layout: publication
title: Agglomerative Clustering Of Growing Squares
authors: Thom Castermans, Bettina Speckmann, Frank Staals, Kevin Verbeek
conference: Lecture Notes in Computer Science
year: 2018
bibkey: castermans2017agglomerative
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.10195'}]
tags: []
short_authors: Castermans et al.
---
We study an agglomerative clustering problem motivated by interactive glyphs
in geo-visualization. Consider a set of disjoint square glyphs on an
interactive map. When the user zooms out, the glyphs grow in size relative to
the map, possibly with different speeds. When two glyphs intersect, we wish to
replace them by a new glyph that captures the information of the intersecting
glyphs.
  We present a fully dynamic kinetic data structure that maintains a set of \\(n\\)
disjoint growing squares. Our data structure uses \\(O(n (log n loglog n)^2)\\)
space, supports queries in worst case \\(O(log^3 n)\\) time, and updates in
\\(O(log^7 n)\\) amortized time. This leads to an \\(O(n\alpha(n)log^7 n)\\) time
algorithm to solve the agglomerative clustering problem. This is a significant
improvement over the current best \\(O(n^2)\\) time algorithms.