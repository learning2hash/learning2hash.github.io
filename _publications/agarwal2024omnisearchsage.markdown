---
layout: publication
title: 'Omnisearchsage: Multi-task Multi-entity Embeddings For Pinterest Search'
authors: Prabhat Agarwal, Minhazul Islam Sk, Nikil Pancha, Kurchi Subhra Hazra, Jiajing
  Xu, Chuck Rosenberg
conference: Companion Proceedings of the ACM Web Conference 2024
year: 2024
bibkey: agarwal2024omnisearchsage
citations: 5
additional_links: [{name: Code, url: 'https://github.com/pinterest/atg-research/tree/main/omnisearchsage'},
  {name: Paper, url: 'https://arxiv.org/abs/2404.16260'}]
tags: [Efficiency]
short_authors: Agarwal et al.
---
In this paper, we present OmniSearchSage, a versatile and scalable system for
understanding search queries, pins, and products for Pinterest search. We
jointly learn a unified query embedding coupled with pin and product
embeddings, leading to an improvement of \(>8%\) relevance, \(>7%\) engagement,
and \(>5%\) ads CTR in Pinterest's production search system. The main
contributors to these gains are improved content understanding, better
multi-task learning, and real-time serving. We enrich our entity
representations using diverse text derived from image captions from a
generative LLM, historical engagement, and user-curated boards. Our multitask
learning setup produces a single search query embedding in the same space as
pin and product embeddings and compatible with pre-existing pin and product
embeddings. We show the value of each feature through ablation studies, and
show the effectiveness of a unified model compared to standalone counterparts.
Finally, we share how these embeddings have been deployed across the Pinterest
search stack, from retrieval to ranking, scaling to serve \(300k\) requests per
second at low latency. Our implementation of this work is available at
https://github.com/pinterest/atg-research/tree/main/omnisearchsage.