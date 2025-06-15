---
layout: publication
title: Anchorhash A Scalable Consistent Hash
authors: Mendelson Gal et al.
conference: "Arxiv"
year: 2018
citations: 15
bibkey: mendelson2018anchorhash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1812.09674"}
tags: ['ARXIV']
---
Consistent hashing (CH) is a central building block in many networking
applications, from datacenter load-balancing to distributed storage.
Unfortunately, state-of-the-art CH solutions cannot ensure full consistency
under arbitrary changes and/or cannot scale while maintaining reasonable memory
footprints and update times. We present AnchorHash, a scalable and
fully-consistent hashing algorithm. AnchorHash achieves high key lookup rates,
a low memory footprint, and low update times. We formally establish its strong
theoretical guarantees, and present advanced implementations with a memory
footprint of only a few bytes per resource. Moreover, extensive evaluations
indicate that it outperforms state-of-the-art algorithms, and that it can scale
on a single core to 100 million resources while still achieving a key lookup
rate of more than 15 million keys per second.
