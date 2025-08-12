---
layout: publication
title: Decoding Billions Of Integers Per Second Through Vectorization
authors: Daniel Lemire, Leonid Boytsov
conference: 'Software: Practice and Experience'
year: 2013
bibkey: lemire2012decoding
citations: 212
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1209.2137'}]
tags: ["Efficiency", "Large Scale Search", "Scalability", "Vector Indexing"]
short_authors: Daniel Lemire, Leonid Boytsov
---
In many important applications -- such as search engines and relational
database systems -- data is stored in the form of arrays of integers. Encoding
and, most importantly, decoding of these arrays consumes considerable CPU time.
Therefore, substantial effort has been made to reduce costs associated with
compression and decompression. In particular, researchers have exploited the
superscalar nature of modern processors and SIMD instructions. Nevertheless, we
introduce a novel vectorized scheme called SIMD-BP128 that improves over
previously proposed vectorized approaches. It is nearly twice as fast as the
previously fastest schemes on desktop processors (varint-G8IU and PFOR). At the
same time, SIMD-BP128 saves up to 2 bits per integer. For even better
compression, we propose another new vectorized scheme (SIMD-FastPFOR) that has
a compression ratio within 10% of a state-of-the-art scheme (Simple-8b) while
being two times faster during decoding.