---
layout: publication
title: 'Hashing And Metric Learning For Charged Particle Tracking'
authors: Sabrina Amrouche, Moritz Kiehn, Tobias Golling, Andreas Salzburger
conference: "Arxiv"
year: 2021
citations: 5
bibkey: amrouche2021hashing
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2101.06428'}
tags: ['Cross-Modal', 'Deep', 'Efficiency', 'Retrieval Models', 'Vector Indexing', 'Supervised', 'Similarity Learning', 'Hashing']
---
We propose a novel approach to charged particle tracking at high intensity
particle colliders based on Approximate Nearest Neighbors search. With hundreds
of thousands of measurements per collision to be reconstructed e.g. at the High
Luminosity Large Hadron Collider, the currently employed combinatorial track
finding approaches become inadequate. Here, we use hashing techniques to
separate measurements into buckets of 20-50 hits and increase their purity
using metric learning. Two different approaches are studied to further resolve
tracks inside buckets: Local Fisher Discriminant Analysis and Neural Networks
for triplet similarity learning. We demonstrate the proposed approach on
simulated collisions and show significant speed improvement with bucket
tracking efficiency of 96% and a fake rate of 8% on unseen particle events.
