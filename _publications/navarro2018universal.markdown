---
layout: publication
title: Universal Compressed Text Indexing
authors: Gonzalo Navarro, Nicola Prezza
conference: Theoretical Computer Science
year: 2018
bibkey: navarro2018universal
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.09520'}]
tags: []
short_authors: Gonzalo Navarro, Nicola Prezza
---
The rise of repetitive datasets has lately generated a lot of interest in
compressed self-indexes based on dictionary compression, a rich and
heterogeneous family that exploits text repetitions in different ways. For each
such compression scheme, several different indexing solutions have been
proposed in the last two decades. To date, the fastest indexes for repetitive
texts are based on the run-length compressed Burrows-Wheeler transform and on
the Compact Directed Acyclic Word Graph. The most space-efficient indexes, on
the other hand, are based on the Lempel-Ziv parsing and on grammar compression.
Indexes for more universal schemes such as collage systems and macro schemes
have not yet been proposed. Very recently, Kempa and Prezza [STOC 2018] showed
that all dictionary compressors can be interpreted as approximation algorithms
for the smallest string attractor, that is, a set of text positions capturing
all distinct substrings. Starting from this observation, in this paper we
develop the first universal compressed self-index, that is, the first indexing
data structure based on string attractors, which can therefore be built on top
of any dictionary-compressed text representation. Let \(\gamma\) be the size of a
string attractor for a text of length \(n\). Our index takes
\(O(\gammalog(n/\gamma))\) words of space and supports locating the \(occ\)
occurrences of any pattern of length \(m\) in \(O(mlog n + occlog^\{\epsilon\}n)\)
time, for any constant \(\epsilon>0\). This is, in particular, the first index
for general macro schemes and collage systems. Our result shows that the
relation between indexing and compression is much deeper than what was
previously thought: the simple property standing at the core of all dictionary
compressors is sufficient to support fast indexed queries.