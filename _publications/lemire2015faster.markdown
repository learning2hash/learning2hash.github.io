---
layout: publication
title: Faster 6445;bit Universal Hashing Using Carry45;less Multiplications
authors: Lemire Daniel, Kaser Owen
conference: "Journal of Cryptographic Engineering Volume"
year: 2015
bibkey: lemire2015faster
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1503.03465"}
tags: ['Independent']
---
Intel and AMD support the Carry45;less Multiplication (CLMUL) instruction set in their x64 processors. We use CLMUL to implement an almost universal 6445;bit hash family (CLHASH). We compare this new family with what might be the fastest almost universal family on x64 processors (VHASH). We find that CLHASH is at least 6037; faster. We also compare CLHASH with a popular hash function designed for speed (Googles CityHash). We find that CLHASH is 4037; faster than CityHash on inputs larger than 64 bytes and just as fast otherwise.
