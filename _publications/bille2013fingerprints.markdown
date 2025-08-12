---
layout: publication
title: Fingerprints In Compressed Strings
authors: "Philip Bille, Patrick Hagge Cording, Inge Li G\xF8rtz, Benjamin Sach, Hjalte\
  \ Wedel Vildh\xF8j, S\xF8ren Vind"
conference: Journal of Computer and System Sciences
year: 2017
bibkey: bille2013fingerprints
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1305.2777'}]
tags: ["Efficiency"]
short_authors: Bille et al.
---
The Karp-Rabin fingerprint of a string is a type of hash value that due to
its strong properties has been used in many string algorithms. In this paper we
show how to construct a data structure for a string \\(S\\) of size \\(N\\) compressed
by a context-free grammar of size \\(n\\) that answers fingerprint queries. That
is, given indices \\(i\\) and \\(j\\), the answer to a query is the fingerprint of the
substring \\(S[i,j]\\). We present the first O(n) space data structures that answer
fingerprint queries without decompressing any characters. For Straight Line
Programs (SLP) we get \\(O(log N)\\) query time, and for Linear SLPs (an SLP
derivative that captures LZ78 compression and its variations) we get \\(O(log
log N)\\) query time. Hence, our data structures has the same time and space
complexity as for random access in SLPs. We utilize the fingerprint data
structures to solve the longest common extension problem in query time \\(O(log
N log \lce)\\) and \\(O(log \lce loglog \lce + loglog N)\\) for SLPs and Linear
SLPs, respectively. Here, \\(\lce\\) denotes the length of the LCE.