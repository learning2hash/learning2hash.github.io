---
layout: publication
title: 'Nearbucket-lsh: Efficient Similarity Search In P2P Networks'
authors: Naama Kraus, David Carmel, Idit Keidar, Meni Orenbach
conference: Arxiv
year: 2015
citations: 5
bibkey: kraus2015nearbucket
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.07148'}]
tags: [Hashing Methods]
---
We present NearBucket-LSH, an effective algorithm for similarity search in
large-scale distributed online social networks organized as peer-to-peer
overlays. As communication is a dominant consideration in distributed systems,
we focus on minimizing the network cost while guaranteeing good search quality.
Our algorithm is based on Locality Sensitive Hashing (LSH), which limits the
search to collections of objects, called buckets, that have a high probability
to be similar to the query. More specifically, NearBucket-LSH employs an LSH
extension that searches in near buckets, and improves search quality but also
significantly increases the network cost. We decrease the network cost by
considering the internals of both LSH and the P2P overlay, and harnessing their
properties to our needs. We show that our NearBucket-LSH increases search
quality for a given network cost compared to previous art. In many cases, the
search quality increases by more than 50%.