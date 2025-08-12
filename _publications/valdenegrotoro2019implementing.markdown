---
layout: publication
title: Implementing Noise With Hash Functions For Graphics Processing Units
authors: Matias Valdenegro-Toro, Hector Pincheira
conference: Arxiv
year: 2019
bibkey: valdenegrotoro2019implementing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.12270'}]
tags: ["Hashing Methods"]
short_authors: Matias Valdenegro-Toro, Hector Pincheira
---
We propose a modification to Perlin noise which use computable hash functions
instead of textures as lookup tables. We implemented the FNV1, Jenkins and
Murmur hashes on Shader Model 4.0 Graphics Processing Units for noise
generation. Modified versions of the FNV1 and Jenkins hashes provide very close
performance compared to a texture based Perlin noise implementation. Our noise
modification enables noise function evaluation without any texture fetches,
trading computational power for memory bandwidth.