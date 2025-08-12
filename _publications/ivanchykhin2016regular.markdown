---
layout: publication
title: 'Regular And Almost Universal Hashing: An Efficient Implementation'
authors: Dmytro Ivanchykhin, Sergey Ignatchenko, Daniel Lemire
conference: 'Software: Practice and Experience'
year: 2016
bibkey: ivanchykhin2016regular
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.09840'}]
tags: ["Hashing Methods"]
short_authors: Dmytro Ivanchykhin, Sergey Ignatchenko, Daniel Lemire
---
Random hashing can provide guarantees regarding the performance of data
structures such as hash tables---even in an adversarial setting. Many existing
families of hash functions are universal: given two data objects, the
probability that they have the same hash value is low given that we pick hash
functions at random. However, universality fails to ensure that all hash
functions are well behaved. We further require regularity: when picking data
objects at random they should have a low probability of having the same hash
value, for any fixed hash function. We present the efficient implementation of
a family of non-cryptographic hash functions (PM+) offering good running times,
good memory usage as well as distinguishing theoretical guarantees: almost
universality and component-wise regularity. On a variety of platforms, our
implementations are comparable to the state of the art in performance. On
recent Intel processors, PM+ achieves a speed of 4.7 bytes per cycle for 32-bit
outputs and 3.3 bytes per cycle for 64-bit outputs. We review vectorization
through SIMD instructions (e.g., AVX2) and optimizations for superscalar
execution.