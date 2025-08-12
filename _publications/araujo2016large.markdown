---
layout: publication
title: Large-scale Query-by-image Video Retrieval Using Bloom Filters
authors: Andre Araujo, Jason Chaves, Haricharan Lakshman, Roland Angst, Bernd Girod
conference: Arxiv
year: 2016
bibkey: araujo2016large
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.07939'}]
tags: ["Scalability", "Video Retrieval"]
short_authors: Araujo et al.
---
We consider the problem of using image queries to retrieve videos from a
database. Our focus is on large-scale applications, where it is infeasible to
index each database video frame independently. Our main contribution is a
framework based on Bloom filters, which can be used to index long video
segments, enabling efficient image-to-video comparisons. Using this framework,
we investigate several retrieval architectures, by considering different types
of aggregation and different functions to encode visual information -- these
play a crucial role in achieving high performance. Extensive experiments show
that the proposed technique improves mean average precision by 24% on a public
dataset, while being 4X faster, compared to the previous state-of-the-art.