---
layout: publication
title: 'Temporal-aware Spiking Transformer Hashing Based On 3D-DWT'
authors: Zihao Mei et al.
conference: "Arxiv"
year: 2025
citations: 0
bibkey: mei2025temporal
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2501.06786'}
tags: ['Hashing Methods', 'Supervision Type', 'Supervision Types', 'Tools and Libraries', 'Hashing Fundamentals', 'Graph and Transformer Models']
---
With the rapid growth of dynamic vision sensor (DVS) data, constructing a
low-energy, efficient data retrieval system has become an urgent task. Hash
learning is one of the most important retrieval technologies which can keep the
distance between hash codes consistent with the distance between DVS data. As
spiking neural networks (SNNs) can encode information through spikes, they
demonstrate great potential in promoting energy efficiency. Based on the binary
characteristics of SNNs, we first propose a novel supervised hashing method
named Spikinghash with a hierarchical lightweight structure. Spiking WaveMixer
(SWM) is deployed in shallow layers, utilizing a multilevel 3D discrete wavelet
transform (3D-DWT) to decouple spatiotemporal features into various
low-frequency and high frequency components, and then employing efficient
spectral feature fusion. SWM can effectively capture the temporal dependencies
and local spatial features. Spiking Self-Attention (SSA) is deployed in deeper
layers to further extract global spatiotemporal information. We also design a
hash layer utilizing binary characteristic of SNNs, which integrates
information over multiple time steps to generate final hash codes. Furthermore,
we propose a new dynamic soft similarity loss for SNNs, which utilizes membrane
potentials to construct a learnable similarity matrix as soft labels to fully
capture the similarity differences between classes and compensate information
loss in SNNs, thereby improving retrieval performance. Experiments on multiple
datasets demonstrate that Spikinghash can achieve state-of-the-art results with
low energy consumption and fewer parameters.
