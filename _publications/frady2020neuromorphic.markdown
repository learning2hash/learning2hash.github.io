---
layout: publication
title: Neuromorphic Nearest-neighbor Search Using Intel's Pohoiki Springs
authors: E. Paxon Frady, Garrick Orchard, David Florey, Nabil Imam, Ruokun Liu, Joyesh
  Mishra, Jonathan Tse, Andreas Wild, Friedrich T. Sommer, Mike Davies
conference: Proceedings of the Neuro-inspired Computational Elements Workshop
year: 2020
bibkey: frady2020neuromorphic
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.12691'}]
tags: [Efficiency, Datasets]
short_authors: Frady et al.
---
Neuromorphic computing applies insights from neuroscience to uncover
innovations in computing technology. In the brain, billions of interconnected
neurons perform rapid computations at extremely low energy levels by leveraging
properties that are foreign to conventional computing systems, such as temporal
spiking codes and finely parallelized processing units integrating both memory
and computation. Here, we showcase the Pohoiki Springs neuromorphic system, a
mesh of 768 interconnected Loihi chips that collectively implement 100 million
spiking neurons in silicon. We demonstrate a scalable approximate k-nearest
neighbor (k-NN) algorithm for searching large databases that exploits
neuromorphic principles. Compared to state-of-the-art conventional CPU-based
implementations, we achieve superior latency, index build time, and energy
efficiency when evaluated on several standard datasets containing over 1
million high-dimensional patterns. Further, the system supports adding new data
points to the indexed database online in O(1) time unlike all but brute force
conventional k-NN implementations.