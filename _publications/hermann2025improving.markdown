---
layout: publication
title: 'Morphishash: Improving Space Efficiency Of Shockhash For Minimal Perfect Hashing'
authors: Stefan Hermann
conference: "Arxiv"
year: 2025
citations: 0
bibkey: hermann2025improving
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2503.10161'}
tags: ['Hashing Fundamentals', 'Evaluation Metrics', 'Hashing Methods']
---
A minimal perfect hash function (MPHF) maps a set of n keys to unique
positions \{1, ..., n\}. Representing an MPHF requires at least 1.44 bits per
key. ShockHash is a technique to construct an MPHF and requires just slightly
more space. It gives each key two pseudo random candidate positions. If each
key can be mapped to one of its two candidate positions such that there is
exactly one key mapped to each position, then an MPHF is found. If not,
ShockHash repeats the process with a new set of random candidate positions.
ShockHash has to store how many repetitions were required and for each key to
which of the two candidate positions it is mapped. However, when a given set of
candidate positions can be used as MPHF then there is not only one but multiple
ways of mapping the keys to one of their candidate positions such that the
mapping results in an MPHF. This redundancy makes up for the majority of the
remaining space overhead in ShockHash. In this paper, we present MorphisHash
which is a technique that almost completely eliminates this redundancy. Our
theoretical result is that MorphisHash saves \{\Theta\}(ln(n)) bits compared to
ShockHash. This corresponds to a factor of 20 less space overhead in practice.
The technique to accomplish this might be of a more general interest to
compress data structures.
