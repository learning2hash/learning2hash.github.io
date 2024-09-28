---
layout: publication
title: Geometric Covering using Random Fields
authors: Goncalves Felipe, Keren Daniel, Shahar Amit, Yehuda Gal
conference: "Arxiv"
year: 2023
bibkey: goncalves2023geometric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2311.14082"}
tags: ['ARXIV', 'Independent', 'LSH']
---
A set of vectors S subseteq ^d is (k_1varepsilon)-clusterable if there are k_1 balls of radius varepsilon that cover S. A set of vectors S subseteq ^d is (k_2delta)-far from being clusterable if there are at least k_2 vectors in S with all pairwise distances at least delta. We propose a probabilistic algorithm to distinguish between these two cases. Our algorithm reaches a decision by only looking at the extreme values of a scalar valued hash function defined by a random field on S; hence it is especially suitable in distributed and online settings. An important feature of our method is that the algorithm is oblivious to the number of vectors in the online setting for example the algorithm stores only a constant number of scalars which is independent of the stream length. We introduce random field hash functions which are a key ingredient in our paradigm. Random field hash functions generalize locality-sensitive hashing (LSH). In addition to the LSH requirement that nearby vectors are hashed to similar values our hash function also guarantees that the hash values are (nearly) independent random variables for distant vectors. We formulate necessary conditions for the kernels which define the random fields applied to our problem as well as a measure of kernel optimality for which we provide a bound. Then we propose a method to construct kernels which approximate the optimal one.
