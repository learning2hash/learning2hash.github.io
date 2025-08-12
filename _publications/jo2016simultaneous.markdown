---
layout: publication
title: Simultaneous Encodings For Range And Next/previous Larger/smaller Value Queries
authors: Seungbum Jo, Srinivasa Rao Satti
conference: Theoretical Computer Science
year: 2016
bibkey: jo2016simultaneous
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.07493'}]
tags: ["Efficiency"]
short_authors: Seungbum Jo, Srinivasa Rao Satti
---
Given an array of \(n\) elements from a total order, we propose encodings that
support various range queries (range minimum, range maximum and their
variants), and previous and next smaller/larger value queries. When query time
is not of concern, we obtain a \(4.088n + o(n)\)-bit encoding that supports all
these queries. For the case when we need to support all these queries in
constant time, we give an encoding that takes \(4.585n + o(n)\) bits, where \(n\)
is the length of input array. This improves the \(5.08n+o(n)\)-bit encoding
obtained by encoding the colored \(2d\)-Min and Max heaps proposed by
Fischer~[TCS, 2011]. We first extend the original DFUDS [Algorithmica, 2005]
encoding of the colored 2d-Min (Max) heap that supports the queries in constant
time. Then, we combine the extended DFUDS of \(2d\)-Min heap and \(2d\)-Max heap
using the Min-Max encoding of Gawrychowski and Nicholson [ICALP, 2015] with
some modifications. We also obtain encodings that take lesser space and support
a subset of these queries.