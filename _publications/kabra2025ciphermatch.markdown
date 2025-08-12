---
layout: publication
title: 'CIPHERMATCH: Accelerating Homomorphic Encryption-based String Matching Via
  Memory-efficient Data Packing And In-flash Processing'
authors: Mayank Kabra, Rakesh Nadig, Harshita Gupta, Rahul Bera, Manos Frouzakis,
  Vamanan Arulchelvan, Yu Liang, Haiyu Mao, Mohammad Sadrosadati, Onur Mutlu
conference: Proceedings of the 30th ACM International Conference on Architectural
  Support for Programming Languages and Operating Systems, Volume 2
year: 2025
bibkey: kabra2025ciphermatch
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.08968'}]
tags: []
short_authors: Kabra et al.
---
Homomorphic encryption (HE) allows secure computation on encrypted data
without revealing the original data, providing significant benefits for
privacy-sensitive applications. Many cloud computing applications (e.g., DNA
read mapping, biometric matching, web search) use exact string matching as a
key operation. However, prior string matching algorithms that use homomorphic
encryption are limited by high computational latency caused by the use of
complex operations and data movement bottlenecks due to the large encrypted
data size. In this work, we provide an efficient algorithm-hardware codesign to
accelerate HE-based secure exact string matching. We propose CIPHERMATCH, which
(i) reduces the increase in memory footprint after encryption using an
optimized software-based data packing scheme, (ii) eliminates the use of costly
homomorphic operations (e.g., multiplication and rotation), and (iii) reduces
data movement by designing a new in-flash processing (IFP) architecture. We
demonstrate the benefits of CIPHERMATCH using two case studies: (1) Exact DNA
string matching and (2) encrypted database search. Our pure software-based
CIPHERMATCH implementation that uses our memory-efficient data packing scheme
improves performance and reduces energy consumption by 42.9X and 17.6X,
respectively, compared to the state-of-the-art software baseline. Integrating
CIPHERMATCH with IFP improves performance and reduces energy consumption by
136.9X and 256.4X, respectively, compared to the software-based CIPHERMATCH
implementation.