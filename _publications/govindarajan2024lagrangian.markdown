---
layout: publication
title: Lagrangian Hashing For Compressed Neural Field Representations
authors: Govindarajan Shrisudhan Ahan, Sambugaro Zeno Ahan, Akhmedkhan Ahan, Shabanov, Takikawa Towaki, Rebain Daniel, Sun Weiwei, Conci Nicola, Yi Kwang Moo, Tagliasacchi Andrea
conference: "Arxiv"
year: 2024
bibkey: govindarajan2024lagrangian
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2409.05334"}
tags: ['ARXIV']
---
We present Lagrangian Hashing a representation for neural fields combining the characteristics of fast training NeRF methods that rely on Eulerian grids (i.e.~InstantNGP) with those that employ points equipped with features as a way to represent information (e.g. 3D Gaussian Splatting or PointNeRF). We achieve this by incorporating a point-based representation into the high-resolution layers of the hierarchical hash tables of an InstantNGP representation. As our points are equipped with a field of influence our representation can be interpreted as a mixture of Gaussians stored within the hash table. We propose a loss that encourages the movement of our Gaussians towards regions that require more representation budget to be sufficiently well represented. Our main finding is that our representation allows the reconstruction of signals using a more compact representation without compromising quality.
