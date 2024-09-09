---
layout: publication
title: Implementing Noise with Hash functions for Graphics Processing Units
authors: Valdenegro-Toro Matias, Pincheira Hector
conference: "Arxiv"
year: 2019
bibkey: valdenegrotoro2019implementing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1903.12270"}
tags: ['ARXIV', 'Graph']
---
We propose a modification to Perlin noise which use computable hash functions instead of textures as lookup tables. We implemented the FNV1 Jenkins and Murmur hashes on Shader Model 4.0 Graphics Processing Units for noise generation. Modified versions of the FNV1 and Jenkins hashes provide very close performance compared to a texture based Perlin noise implementation. Our noise modification enables noise function evaluation without any texture fetches trading computational power for memory bandwidth.
