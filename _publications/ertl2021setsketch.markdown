---
layout: publication
title: 'Setsketch: Filling The Gap Between Minhash And Hyperloglog'
authors: Ertl Otmar
conference: Proceedings of the VLDB Endowment
year: 2021
bibkey: ertl2021setsketch
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.00314'}]
tags: ["Locality Sensitive Hashing"]
---
MinHash and HyperLogLog are sketching algorithms that have become
indispensable for set summaries in big data applications. While HyperLogLog
allows counting different elements with very little space, MinHash is suitable
for the fast comparison of sets as it allows estimating the Jaccard similarity
and other joint quantities. This work presents a new data structure called
SetSketch that is able to continuously fill the gap between both use cases. Its
commutative and idempotent insert operation and its mergeable state make it
suitable for distributed environments. Fast, robust, and easy-to-implement
estimators for cardinality and joint quantities, as well as the ability to use
SetSketch for similarity search, enable versatile applications. The presented
joint estimator can also be applied to other data structures such as MinHash,
HyperLogLog, or HyperMinHash, where it even performs better than the
corresponding state-of-the-art estimators in many cases.