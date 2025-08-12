---
layout: publication
title: The Colored Longest Common Prefix Array Computed Via Sequential Scans
authors: F. Garofalo, G. Rosone, M. Sciortino, D. Verzotto
conference: Lecture Notes in Computer Science
year: 2018
bibkey: garofalo2018colored
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07596'}]
tags: []
short_authors: Garofalo et al.
---
Due to the increased availability of large datasets of biological sequences,
the tools for sequence comparison are now relying on efficient alignment-free
approaches to a greater extent. Most of the alignment-free approaches require
the computation of statistics of the sequences in the dataset. Such
computations become impractical in internal memory when very large collections
of long sequences are considered. In this paper, we present a new conceptual
data structure, the colored longest common prefix array (cLCP), that allows to
efficiently tackle several problems with an alignment-free approach. In fact,
we show that such a data structure can be computed via sequential scans in
semi-external memory. By using cLCP, we propose an efficient lightweight
strategy to solve the multi-string Average Common Substring (ACS) problem, that
consists in the pairwise comparison of a single string against a collection of
\(m\) strings simultaneously, in order to obtain \(m\) ACS induced distances.
Experimental results confirm the effectiveness of our approach.