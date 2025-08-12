---
layout: publication
title: Multiple Set Matching And Pre-filtering With Bloom Multifilters
authors: Francesco Concas, Pengfei Xu, Mohammad A. Hoque, Jiaheng Lu, Sasu Tarkoma
conference: Arxiv
year: 2019
bibkey: concas2019multiple
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.01825'}]
tags: []
short_authors: Concas et al.
---
Bloom filter is a space-efficient probabilistic data structure for checking
elements' membership in a set. Given multiple sets, however, a standard Bloom
filter is not sufficient when looking for the items to which an element or a
set of input elements belong to. In this article, we solve multiple set
matching problem by proposing two efficient Bloom Multifilters called Bloom
Matrix and Bloom Vector. Both of them are space efficient and answer queries
with a set of identifiers for multiple set matching problems. We show that the
space efficiency can be optimized further according to the distribution of
labels among multiple sets: Uniform and Zipf. While both of them are space
efficient, Bloom Vector can efficiently exploit Zipf distribution of data for
further space reduction. Our results also highlight that basic ADD and LOOKUP
operations on Bloom Matrix are faster than on Bloom Vector. However, Bloom
Matrix does not meet the theoretical false positive rate of less than \(10^\{-2\}\)
for LOOKUP operations if the represented data or the labels are not uniformly
distributed among the multiple sets. Consequently, we introduce \textit\{Bloom
Test\} which uses Bloom Matrix as the pre-filter structure to determine which
structure is suitable for improved performance with an arbitrary input dataset.