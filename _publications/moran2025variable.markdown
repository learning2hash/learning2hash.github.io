---
layout: publication
title: Variable Bit Quantisation For LSH
authors: S. Moran, Lavrenko, Osborne
conference: No Venue
year: 2025
bibkey: moran2025variable
citations: 21
additional_links: [{name: Paper, url: 'http://homepages.inf.ed.ac.uk/miles/papers/acl13.pdf'}]
tags: ["Locality-Sensitive-Hashing", "Quantization"]
short_authors: S. Moran, Lavrenko, Osborne
---
We introduce a scheme for optimally allocating
a variable number of bits per
LSH hyperplane. Previous approaches assign
a constant number of bits per hyperplane.
This neglects the fact that a subset
of hyperplanes may be more informative
than others. Our method, dubbed Variable
Bit Quantisation (VBQ), provides a datadriven
non-uniform bit allocation across
hyperplanes. Despite only using a fraction
of the available hyperplanes, VBQ outperforms
uniform quantisation by up to 168%
for retrieval across standard text and image
datasets.