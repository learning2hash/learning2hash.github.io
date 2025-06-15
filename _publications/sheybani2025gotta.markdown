---
layout: publication
title: 'Gotta Hash ''em All! Speeding Up Hash Functions For Zero-knowledge Proof Applications'
authors: Nojan Sheybani et al.
conference: "Arxiv"
year: 2025
citations: 0
bibkey: sheybani2025gotta
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2501.18780'}
tags: ['Independent', 'Unimodal', 'Shallow', 'Training Strategy', 'Hashing', 'Applications']
---
Collision-resistant cryptographic hash functions (CRHs) are crucial for
security in modern systems but are optimized for standard CPUs. While heavily
used in zero-knowledge proof (ZKP) applications, traditional CRHs are
inefficient in the ZK domain. ZK-friendly hashes have been developed but
struggle on consumer hardware due to a lack of specialized ZK-specific
hardware. To address this, we present HashEmAll, a novel collection of
FPGA-based realizations of three ZK-friendly hash functions: Griffin,
Rescue-Prime, and Reinforced Concrete. Each hash offers different optimization
focuses, allowing users to choose based on the constraints of their
applications. Through our ZK-optimized arithmetic functions on reconfigurable
hardware, HashEmAll outperforms CPU implementations by up to \\(23\times\\) with
lower power consumption and compatibility with accessible FPGAs.
