---
layout: publication
title: Hierarchical Overlap Graph
authors: Bastien Cazaux, Eric Rivals
conference: Information Processing Letters
year: 2019
bibkey: cazaux2018hierarchical
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.04632'}]
tags: []
short_authors: Bastien Cazaux, Eric Rivals
---
Given a set of finite words, the Overlap Graph (OG) is a complete weighted
digraph where each word is a node and where the weight of an arc equals the
length of the longest overlap of one word onto the other (Overlap is an
asymmetric notion). The OG serves to assemble DNA fragments or to compute
shortest superstrings which are a compressed representation of the input. The
OG requires a space is quadratic in the number of words, which limits its
scalability. The Hierarchical Overlap Graph (HOG) is an alternative graph that
also encodes all maximal overlaps, but uses a space that is linear in the sum
of the lengths of the input words. We propose the first algorithm to build the
HOG in linear space for words of equal length.