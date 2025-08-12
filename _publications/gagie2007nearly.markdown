---
layout: publication
title: A Nearly Tight Memory-redundancy Trade-off For One-pass Compression
authors: Travis Gagie
conference: Arxiv
year: 2007
bibkey: gagie2007nearly
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0708.1877'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Travis Gagie
---
Let \(s\) be a string of length \(n\) over an alphabet of constant size \(\sigma\)
and let \(c\) and \(\epsilon\) be constants with (1 \geq c \geq 0) and (\epsilon >
0). Using (O (n)) time, (O (n^c)) bits of memory and one pass we can always
encode \(s\) in (n H_k (s) + O (\sigma^k n^\{1 - c + \epsilon\})) bits for all
integers (k \geq 0) simultaneously. On the other hand, even with unlimited
time, using (O (n^c)) bits of memory and one pass we cannot always encode \(s\)
in (O (n H_k (s) + \sigma^k n^\{1 - c - \epsilon\})) bits for, e.g., (k = \lceil
(c + \epsilon / 2) log_\sigma n \rceil).