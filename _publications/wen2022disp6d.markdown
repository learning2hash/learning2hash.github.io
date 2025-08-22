---
layout: publication
title: 'DISP6D: Disentangled Implicit Shape And Pose Learning For Scalable 6D Pose
  Estimation'
authors: Yilin Wen, Xiangyu Li, Hao Pan, Lei Yang, Zheng Wang, Taku Komura, Wenping
  Wang
conference: Lecture Notes in Computer Science
year: 2022
bibkey: wen2022disp6d
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.12549'}]
tags: ["Evaluation", "Scalability", "Tools & Libraries"]
short_authors: Wen et al.
---
Scalable 6D pose estimation for rigid objects from RGB images aims at
handling multiple objects and generalizing to novel objects. Building on a
well-known auto-encoding framework to cope with object symmetry and the lack of
labeled training data, we achieve scalability by disentangling the latent
representation of auto-encoder into shape and pose sub-spaces. The latent shape
space models the similarity of different objects through contrastive metric
learning, and the latent pose code is compared with canonical rotations for
rotation retrieval. Because different object symmetries induce inconsistent
latent pose spaces, we re-entangle the shape representation with canonical
rotations to generate shape-dependent pose codebooks for rotation retrieval. We
show state-of-the-art performance on two benchmarks containing textureless CAD
objects without category and daily objects with categories respectively, and
further demonstrate improved scalability by extending to a more challenging
setting of daily objects across categories.