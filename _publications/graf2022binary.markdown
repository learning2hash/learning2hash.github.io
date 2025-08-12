---
layout: publication
title: 'Binary Fuse Filters: Fast And Smaller Than Xor Filters'
authors: Thomas Mueller Graf, Daniel Lemire
conference: ACM Journal of Experimental Algorithmics
year: 2022
bibkey: graf2022binary
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.01174'}]
tags: []
short_authors: Thomas Mueller Graf, Daniel Lemire
---
Bloom and cuckoo filters provide fast approximate set membership while using
little memory. Engineers use them to avoid expensive disk and network accesses.
The recently introduced xor filters can be faster and smaller than Bloom and
cuckoo filters. The xor filters are within 23% of the theoretical lower bound
in storage as opposed to 44% for Bloom filters. Inspired by Dietzfelbinger and
Walzer, we build probabilistic filters -- called binary fuse filters -- that
are within 13% of the storage lower bound -- without sacrificing query speed.
As an additional benefit, the construction of the new binary fuse filters can
be more than twice as fast as the construction of xor filters. By slightly
sacrificing query speed, we further reduce storage to within 8% of the lower
bound. We compare the performance against a wide range of competitive
alternatives such as Bloom filters, blocked Bloom filters, vector quotient
filters, cuckoo filters, and the recent ribbon filters. Our experiments suggest
that binary fuse filters are superior to xor filters.