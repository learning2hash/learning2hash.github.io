---
layout: publication
title: Practical Hash-based Anonymity for MAC Addresses
authors: Ali Junade, Dyo Vladimir
conference: "Arxiv"
year: 2020
bibkey: ali2020practical
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.06580"}
tags: ['ARXIV', 'Graph']
---
Given that a MAC address can uniquely identify a person or a vehicle, continuous tracking over a large geographical scale has raised serious privacy concerns amongst governments and the general public. Prior work has demonstrated that simple hash-based approaches to anonymization can be easily inverted due to the small search space of MAC addresses. In particular, it is possible to represent the entire allocated MAC address space in 39 bits and that frequency-based attacks allow for 50% of MAC addresses to be enumerated in 31 bits. We present a practical approach to MAC address anonymization using both computationally expensive hash functions and truncating the resulting hashes to allow for k-anonymity. We provide an expression for computing the percentage of expected collisions, demonstrating that for digests of 24 bits it is possible to store up to 168,617 MAC addresses with the rate of collisions less than 1%. We experimentally demonstrate that a rate of collision of 1% or less can be achieved by storing data sets of 100 MAC addresses in 13 bits, 1,000 MAC addresses in 17 bits and 10,000 MAC addresses in 20 bits.
