---
layout: publication
title: Space-efficient String Indexing For Wildcard Pattern Matching
authors: Moshe Lewenstein, Yakov Nekrich, Jeffrey Scott Vitter
conference: Arxiv
year: 2014
bibkey: lewenstein2014space
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1401.0625'}]
tags: ["Efficiency"]
short_authors: Moshe Lewenstein, Yakov Nekrich, Jeffrey Scott Vitter
---
In this paper we describe compressed indexes that support pattern matching
queries for strings with wildcards. For a constant size alphabet our data
structure uses \(O(nlog^\{\epsilon\}n)\) bits for any \(\epsilon>0\) and
reports all \(\mathrm\{occ\}\) occurrences of a wildcard string in \(O(m+\sigma^g
\cdot\mu(n) + \mathrm\{occ\})\) time, where \(\mu(n)=o(logloglog n)\), \(\sigma\)
is the alphabet size, \(m\) is the number of alphabet symbols and \(g\) is the
number of wildcard symbols in the query string. We also present an \(O(n)\)-bit
index with \(O((m+\sigma^g+\mathrm\{occ\})log^\{\epsilon\}n)\) query time and an
\(O(n(loglog n)^2)\)-bit index with \(O((m+\sigma^g+\mathrm\{occ\})loglog n)\)
query time. These are the first non-trivial data structures for this problem
that need \(o(nlog n)\) bits of space.