---
layout: publication
title: Em-k Indexing For Approximate Query Matching In Large-scale ER
authors: Samudra Herath, Matthew Roughan, Gary Glonek
conference: Arxiv
year: 2021
bibkey: herath2021em
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04070'}]
tags: ["Datasets", "Scalability", "Similarity Search", "Tree Based ANN"]
short_authors: Samudra Herath, Matthew Roughan, Gary Glonek
---
Accurate and efficient entity resolution (ER) is a significant challenge in
many data mining and analysis projects requiring integrating and processing
massive data collections. It is becoming increasingly important in real-world
applications to develop ER solutions that produce prompt responses for entity
queries on large-scale databases. Some of these applications demand entity
query matching against large-scale reference databases within a short time. We
define this as the query matching problem in ER in this work. Indexing or
blocking techniques reduce the search space and execution time in the ER
process. However, approximate indexing techniques that scale to very
large-scale datasets remain open to research. In this paper, we investigate the
query matching problem in ER to propose an indexing method suitable for
approximate and efficient query matching.
  We first use spatial mappings to embed records in a multidimensional
Euclidean space that preserves the domain-specific similarity. Among the
various mapping techniques, we choose multidimensional scaling. Then using a
Kd-tree and the nearest neighbour search, the method returns a block of records
that includes potential matches for a query. Our method can process queries
against a large-scale dataset using only a fraction of the data \(L\) (given the
dataset size is \(N\)), with a \(O(L^2)\) complexity where \(L \ll N\). The
experiments conducted on several datasets showed the effectiveness of the
proposed method.