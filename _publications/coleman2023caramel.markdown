---
layout: publication
title: 'CARAMEL: A Succinct Read-only Lookup Table Via Compressed Static Functions'
authors: Benjamin Coleman, David Torres Ramos, Vihan Lakshman, Chen Luo, Anshumali
  Shrivastava
conference: Arxiv
year: 2023
bibkey: coleman2023caramel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.16545'}]
tags: ["Compact Codes"]
short_authors: Coleman et al.
---
Lookup tables are a fundamental structure in many data processing and systems
applications. Examples include tokenized text in NLP, quantized embedding
collections in recommendation systems, integer sketches for streaming data, and
hash-based string representations in genomics. With the increasing size of
web-scale data, such applications often require compression techniques that
support fast random \(O(1)\) lookup of individual parameters directly on the
compressed data (i.e. without blockwise decompression in RAM). While the
community has proposd a number of succinct data structures that support queries
over compressed representations, these approaches do not fully leverage the
low-entropy structure prevalent in real-world workloads to reduce space.
Inspired by recent advances in static function construction techniques, we
propose a space-efficient representation of immutable key-value data, called
CARAMEL, specifically designed for the case where the values are multi-sets. By
carefully combining multiple compressed static functions, CARAMEL occupies
space proportional to the data entropy with low memory overheads and minimal
lookup costs. We demonstrate 1.25-16x compression on practical lookup tasks
drawn from real-world systems, improving upon established techniques, including
a production-grade read-only database widely used for development within
Amazon.com.