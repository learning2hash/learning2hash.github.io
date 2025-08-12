---
layout: publication
title: Hashing With Linear Probing And Referential Integrity
authors: Peter Sanders
conference: Arxiv
year: 2018
bibkey: sanders2018hashing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.04602'}]
tags: ["Hashing Methods"]
short_authors: Peter Sanders
---
We describe a variant of linear probing hash tables that never moves elements
and thus supports referential integrity, i.e., pointers to elements remain
valid while this element is in the hash table. This is achieved by the folklore
method of marking some table entries as formerly occupied (tombstones). The
innovation is that the number of tombstones is minimized. Experiments indicate
that this allows an unbounded number of operations with bounded overhead
compared to linear probing without tombstones (and without referential
integrity).