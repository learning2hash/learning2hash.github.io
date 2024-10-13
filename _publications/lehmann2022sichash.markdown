---
layout: publication
title: Sichash -- Small Irregular Cuckoo Tables For Perfect Hashing
authors: Lehmann Hans-peter, Sanders Peter, Walzer Stefan
conference: "Arxiv"
year: 2022
bibkey: lehmann2022sichash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2210.01560"}
tags: ['ARXIV', 'Independent']
---
<p>A Perfect Hash Function (PHF) is a hash function that has no
collisions on a given input set. PHFs can be used for space efficient
storage of data in an array, or for determining a compact representative
of each object in the set. In this paper, we present the PHF
construction algorithm SicHash - Small Irregular Cuckoo Tables for
Perfect Hashing. At its core, SicHash uses a known technique: It places
objects in a cuckoo hash table and then stores the final hash function
choice of each object in a retrieval data structure. We combine the idea
with irregular cuckoo hashing, where each object has a different number
of hash functions. Additionally, we use many small tables that we
overload beyond their asymptotic maximum load factor. The most space
efficient competitors often use brute force methods to determine the
PHFs. SicHash provides a more direct construction algorithm that only
rarely needs to recompute parts. Our implementation improves the state
of the art in terms of space usage versus construction time for a wide
range of configurations. At the same time, it provides very fast
queries.</p>
