---
layout: publication
title: Content-based Music Similarity With Triplet Networks
authors: Joseph Cleveland, Derek Cheng, Michael Zhou, Thorsten Joachims, Douglas Turnbull
conference: Arxiv
year: 2020
bibkey: cleveland2020content
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.04938'}]
tags: ["Uncategorized"]
short_authors: Cleveland et al.
---
We explore the feasibility of using triplet neural networks to embed songs
based on content-based music similarity. Our network is trained using triplets
of songs such that two songs by the same artist are embedded closer to one
another than to a third song by a different artist. We compare two models that
are trained using different ways of picking this third song: at random vs.
based on shared genre labels. Our experiments are conducted using songs from
the Free Music Archive and use standard audio features. The initial results
show that shallow Siamese networks can be used to embed music for a simple
artist retrieval task.