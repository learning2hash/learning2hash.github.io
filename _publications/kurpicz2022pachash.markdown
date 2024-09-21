---
layout: publication
title: PaCHash Packed and Compressed Hash Tables
authors: Kurpicz Florian, Lehmann Hans-peter, Sanders Peter
conference: "Arxiv"
year: 2022
bibkey: kurpicz2022pachash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2205.04745"}
tags: ['ARXIV', 'General']
---
We introduce PaCHash a hash table that stores its objects contiguously in an array without intervening space even if the objects have variable size. In particular each object can be compressed using standard compression techniques. A small search data structure allows locating the objects in constant expected time. PaCHash is most naturally described as a static external hash table where it needs a constant number of bits of internal memory per block of external memory. Here in some sense PaCHash beats a lower bound on the space consumption of k-perfect hashing. An implementation for fast SSDs needs about 5 bits of internal memory per block of external memory requires only one disk access (of variable length) per search operation and has small internal search overhead compared to the disk access cost. Our experiments show that it has lower space consumption than all previous approaches even when considering objects of identical size.
