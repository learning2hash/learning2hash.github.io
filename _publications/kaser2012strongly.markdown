---
layout: publication
title: Strongly Universal String Hashing Is Fast
authors: Kaser Owen, Lemire Daniel
conference: "Computer Journal"
year: 2012
bibkey: kaser2012strongly
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1202.4961"}
tags: ['Independent']
---
We present fast strongly universal string hashing families: they can process data at a rate of 0.2 CPU cycle per byte. Maybe surprisingly, we find that these families---though they require a large buffer of random numbers---are often faster than popular hash functions with weaker theoretical guarantees. Moreover, conventional wisdom is that hash functions with fewer multiplications are faster. Yet we find that they may fail to be faster due to operation pipelining. We present experimental results on several processors including low-powered processors. Our tests include hash functions designed for processors with the Carry-Less Multiplication (CLMUL) instruction set. We also prove, using accessible proofs, the strong universality of our families.
