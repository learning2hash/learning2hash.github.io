---
layout: publication
title: Geometric Covering Using Random Fields
authors: Goncalves Felipe, Keren Daniel, Shahar Amit, Yehuda Gal
conference: "Arxiv"
year: 2023
bibkey: goncalves2023geometric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2311.14082"}
tags: ['ARXIV', 'Independent', 'LSH']
---
A set of vectors \{&#37; raw &#37;\}\\(S \subseteq \mathbb\{R\}^d\\)\{&#37; endraw &#37;\} is \{&#37; raw &#37;\}\\((k\_1,\varepsilon)\\)\{&#37; endraw &#37;\}-clusterable if there are \{&#37; raw &#37;\}\\(k\_1\\)\{&#37; endraw &#37;\} balls of radius \{&#37; raw &#37;\}\\(\varepsilon\\)\{&#37; endraw &#37;\} that cover \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\}. A set of vectors \{&#37; raw &#37;\}\\(S \subseteq \mathbb\{R\}^d\\)\{&#37; endraw &#37;\} is \{&#37; raw &#37;\}\\((k\_2,\delta)\\)\{&#37; endraw &#37;\}-far from being clusterable if there are at least \{&#37; raw &#37;\}\\(k\_2\\)\{&#37; endraw &#37;\} vectors in \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\}, with all pairwise distances at least \{&#37; raw &#37;\}\\(\delta\\)\{&#37; endraw &#37;\}. We propose a probabilistic algorithm to distinguish between these two cases. Our algorithm reaches a decision by only looking at the extreme values of a scalar valued hash function, defined by a random field, on \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\}; hence, it is especially suitable in distributed and online settings. An important feature of our method is that the algorithm is oblivious to the number of vectors: in the online setting, for example, the algorithm stores only a constant number of scalars, which is independent of the stream length. We introduce random field hash functions, which are a key ingredient in our paradigm. Random field hash functions generalize locality-sensitive hashing (LSH). In addition to the LSH requirement that nearby vectors are hashed to similar values, our hash function also guarantees that the hash values are (nearly) independent random variables for distant vectors. We formulate necessary conditions for the kernels which define the random fields applied to our problem, as well as a measure of kernel optimality, for which we provide a bound. Then, we propose a method to construct kernels which approximate the optimal one.
