---
layout: publication
title: Learned Indexes For A Google-scale Disk-based Database
authors: "Hussam Abu-Libdeh, Deniz Alt\u0131nb\xFCken, Alex Beutel, Ed H. Chi, Lyric\
  \ Doshi, Tim Kraska, Xiaozhou, Li, Andy Ly, Christopher Olston"
conference: Arxiv
year: 2020
bibkey: abulibdeh2020learned
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.12501'}]
tags: ["Vector Indexing"]
short_authors: Abu-Libdeh et al.
---
There is great excitement about learned index structures, but understandable
skepticism about the practicality of a new method uprooting decades of research
on B-Trees. In this paper, we work to remove some of that uncertainty by
demonstrating how a learned index can be integrated in a distributed,
disk-based database system: Google's Bigtable. We detail several design
decisions we made to integrate learned indexes in Bigtable. Our results show
that integrating learned index significantly improves the end-to-end read
latency and throughput for Bigtable.