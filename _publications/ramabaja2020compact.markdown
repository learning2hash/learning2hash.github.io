---
layout: publication
title: "Compact Merkle Multiproofs"
authors: Ramabaja Lum, Avdullahu Arber
conference: Arxiv
year: 2020
bibkey: ramabaja2020compact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2002.07648"}
tags: ['ARXIV', 'TIP']
---
The compact Merkle multiproof is a new and significantly more memory-efficient way to generate and verify sparse Merkle multiproofs. A standard sparse Merkle multiproof requires to store an index for every non-leaf hash in the multiproof. The compact Merkle multiproof on the other hand requires only $k$ leaf indices, where $k$ is the number of elements used for creating a multiproof. This significantly reduces the size of multirpoofs, especially for larger Merke trees.