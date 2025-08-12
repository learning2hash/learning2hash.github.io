---
layout: publication
title: Fast Compressed Self-indexes With Deterministic Linear-time Construction
authors: J. Ian Munro, Gonzalo Navarro, Yakov Nekrich
conference: Algorithmica
year: 2019
bibkey: munro2017fast
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.01743'}]
tags: ["Efficiency", "Vector Indexing"]
short_authors: J. Ian Munro, Gonzalo Navarro, Yakov Nekrich
---
We introduce a compressed suffix array representation that, on a text \\(T\\) of
length \\(n\\) over an alphabet of size \\(\sigma\\), can be built in \\(O(n)\\)
deterministic time, within \\(O(nlog\sigma)\\) bits of working space, and counts
the number of occurrences of any pattern \\(P\\) in \\(T\\) in time \\(O(|P| + loglog_w
\sigma)\\) on a RAM machine of \\(w=Ω(log n)\\)-bit words. This new index
outperforms all the other compressed indexes that can be built in linear
deterministic time, and some others. The only faster indexes can be built in
linear time only in expectation, or require \\(\Theta(nlog n)\\) bits. We also
show that, by using \\(O(nlog\sigma)\\) bits, we can build in linear time an index
that counts in time \\(O(|P|/log_\sigma n + log n(loglog n)^2)\\), which is
RAM-optimal for \\(w=\Theta(log n)\\) and sufficiently long patterns.