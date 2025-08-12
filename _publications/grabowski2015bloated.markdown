---
layout: publication
title: A Bloated Fm-index Reducing The Number Of Cache Misses During The Search
authors: "Szymon Grabowski, Aleksander Cis\u0142ak"
conference: Arxiv
year: 2015
bibkey: grabowski2015bloated
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.01996'}]
tags: ["Efficiency", "Hashing Methods", "Memory Efficiency"]
short_authors: "Szymon Grabowski, Aleksander Cis\u0142ak"
---
The FM-index is a well-known compressed full-text index, based on the
Burrows-Wheeler transform (BWT). During a pattern search, the BWT sequence is
accessed at "random" locations, which is cache-unfriendly. In this paper, we
are interested in speeding up the FM-index by working on \(q\)-grams rather than
individual characters, at the cost of using more space. The first presented
variant is related to an inverted index on \(q\)-grams, yet the occurrence lists
in our solution are in the sorted suffix order rather than text order in a
traditional inverted index. This variant obtains \(O(m/|CL| + log n log m)\)
cache misses in the worst case, where \(n\) and \(m\) are the text and pattern
lengths, respectively, and \(|CL|\) is the CPU cache line size, in symbols
(typically 64 in modern hardware). This index is often several times faster
than the fastest known FM-indexes (especially for long patterns), yet the space
requirements are enormous, \(O(nlog^2 n)\) bits in theory and about \(80n\)-\(95n\)
bytes in practice. For this reason, we dub our approach FM-bloated. The second
presented variant requires \(O(nlog n)\) bits of space.