---
layout: publication
title: A Bijective String Sorting Transform
authors: Joseph Yossi Gil, David Allen Scott
conference: Arxiv
year: 2012
bibkey: gil2012bijective
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1201.3077'}]
tags: []
short_authors: Joseph Yossi Gil, David Allen Scott
---
Given a string of characters, the Burrows-Wheeler Transform rearranges the
characters in it so as to produce another string of the same length which is
more amenable to compression techniques such as move to front, run-length
encoding, and entropy encoders. We present a variant of the transform which
gives rise to similar or better compression value, but, unlike the original,
the transform we present is bijective, in that the inverse transformation
exists for all strings. Our experiments indicate that using our variant of the
transform gives rise to better compression ratio than the original
Burrows-Wheeler transform. We also show that both the transform and its inverse
can be computed in linear time and consuming linear storage.