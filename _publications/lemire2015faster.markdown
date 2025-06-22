---
layout: publication
title: Faster 64-bit Universal Hashing Using Carry-less Multiplications
authors: Daniel Lemire, Owen Kaser
conference: Journal of Cryptographic Engineering Volume 6 Issue 3 pp 171-185 2016
year: 2015
citations: 15
bibkey: lemire2015faster
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1503.03465'}]
tags: [Hashing Methods]
---
Intel and AMD support the Carry-less Multiplication (CLMUL) instruction set
in their x64 processors. We use CLMUL to implement an almost universal 64-bit
hash family (CLHASH). We compare this new family with what might be the fastest
almost universal family on x64 processors (VHASH). We find that CLHASH is at
least 60% faster. We also compare CLHASH with a popular hash function designed
for speed (Google's CityHash). We find that CLHASH is 40% faster than CityHash
on inputs larger than 64 bytes and just as fast otherwise.