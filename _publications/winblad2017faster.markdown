---
layout: publication
title: Faster Concurrent Range Queries With Contention Adapting Search Trees Using
  Immutable Data
authors: Kjell Winblad
conference: Arxiv
year: 2017
bibkey: winblad2017faster
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.00722'}]
tags: ["Efficiency", "Scalability"]
short_authors: Kjell Winblad
---
The need for scalable concurrent ordered set data structures with
linearizable range query support is increasing due to the rise of multicore
computers, data processing platforms and in-memory databases. This paper
presents a new concurrent ordered set with linearizable range query support.
The new data structure is based on the contention adapting search tree and an
immutable data structure. Experimental results show that the new data structure
is as much as three times faster compared to related data structures. The data
structure scales well due to its ability to adapt the sizes of its immutable
parts to the contention level and the sizes of the range queries.