---
layout: publication
title: "Faster 64-bit universal hashing using carry-less multiplications"
authors: Lemire Daniel, Kaser Owen
conference: Journal of Cryptographic Engineering, Volume
year: 2015
bibkey: lemire2015faster
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1503.03465"}
tags: ['TIP', 'Volume']
---
Intel and AMD support the Carry-less Multiplication (CLMUL) instruction set in their x64 processors. We use CLMUL to implement an almost universal 64-bit hash family (CLHASH). We compare this new family with what might be the fastest almost universal family on x64 processors (VHASH). We find that CLHASH is at least 60% faster. We also compare CLHASH with a popular hash function designed for speed (Google's CityHash). We find that CLHASH is 40% faster than CityHash on inputs larger than 64 bytes and just as fast otherwise.