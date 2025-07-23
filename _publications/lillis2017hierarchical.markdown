---
layout: publication
title: Hierarchical Bloom Filter Trees For Approximate Matching
authors: Lillis David, Breitinger Frank, Scanlon Mark
conference: The Journal of Digital Forensics, Security and Law
year: 2018
bibkey: lillis2017hierarchical
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.04544'}]
tags: ["Efficiency", "Hashing Methods", "Scalability", "Similarity Search"]
short_authors: Lillis David, Breitinger Frank, Scanlon Mark
---
Bytewise approximate matching algorithms have in recent years shown
significant promise in de- tecting files that are similar at the byte level.
This is very useful for digital forensic investigators, who are regularly faced
with the problem of searching through a seized device for pertinent data. A
common scenario is where an investigator is in possession of a collection of
"known-illegal" files (e.g. a collection of child abuse material) and wishes to
find whether copies of these are stored on the seized device. Approximate
matching addresses shortcomings in traditional hashing, which can only find
identical files, by also being able to deal with cases of merged files,
embedded files, partial files, or if a file has been changed in any way.
  Most approximate matching algorithms work by comparing pairs of files, which
is not a scalable approach when faced with large corpora. This paper
demonstrates the effectiveness of using a "Hierarchical Bloom Filter Tree"
(HBFT) data structure to reduce the running time of
collection-against-collection matching, with a specific focus on the MRSH-v2
algorithm. Three experiments are discussed, which explore the effects of
different configurations of HBFTs. The proposed approach dramatically reduces
the number of pairwise comparisons required, and demonstrates substantial speed
gains, while maintaining effectiveness.