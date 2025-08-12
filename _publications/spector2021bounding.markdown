---
layout: publication
title: 'Bounding The Last Mile: Efficient Learned String Indexing'
authors: Benjamin Spector, Andreas Kipf, Kapil Vaidya, Chi Wang, Umar Farooq Minhas,
  Tim Kraska
conference: Arxiv
year: 2021
bibkey: spector2021bounding
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.14905'}]
tags: ["Vector Indexing"]
short_authors: Spector et al.
---
We introduce the RadixStringSpline (RSS) learned index structure for
efficiently indexing strings. RSS is a tree of radix splines each indexing a
fixed number of bytes. RSS approaches or exceeds the performance of traditional
string indexes while using 7-70\(\times\) less memory. RSS achieves this by using
the minimal string prefix to sufficiently distinguish the data unlike most
learned approaches which index the entire string. Additionally, the
bounded-error nature of RSS accelerates the last mile search and also enables a
memory-efficient hash-table lookup accelerator. We benchmark RSS on several
real-world string datasets against ART and HOT. Our experiments suggest this
line of research may be promising for future memory-intensive database
applications.