---
layout: publication
title: Sampling And Reconstruction Using Bloom Filters
authors: Neha Sengupta, Amitabha Bagchi, Srikanta Bedathur, Maya Ramanath
conference: 2017 IEEE 33rd International Conference on Data Engineering (ICDE)
year: 2017
bibkey: sengupta2017sampling
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.03308'}]
tags: []
short_authors: Sengupta et al.
---
In this paper, we address the problem of sampling from a set and
reconstructing a set stored as a Bloom filter. To the best of our knowledge our
work is the first to address this question. We introduce a novel hierarchical
data structure called BloomSampleTree that helps us design efficient algorithms
to extract an almost uniform sample from the set stored in a Bloom filter and
also allows us to reconstruct the set efficiently. In the case where the hash
functions used in the Bloom filter implementation are partially invertible, in
the sense that it is easy to calculate the set of elements that map to a
particular hash value, we propose a second, more space-efficient method called
HashInvert for the reconstruction. We study the properties of these two methods
both analytically as well as experimentally. We provide bounds on run times for
both methods and sample quality for the BloomSampleTree based algorithm, and
show through an extensive experimental evaluation that our methods are
efficient and effective.