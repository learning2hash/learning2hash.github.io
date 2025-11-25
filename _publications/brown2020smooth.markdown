---
layout: publication
title: 'Smooth-ap: Smoothing The Path Towards Large-scale Image Retrieval'
authors: Andrew Brown, Weidi Xie, Vicky Kalogeiton, Andrew Zisserman
conference: Arxiv
year: 2020
bibkey: brown2020smooth
citations: 127
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.12163'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval", "Scalability"]
short_authors: Brown et al.
---
Optimising a ranking-based metric, such as Average Precision (AP), is
notoriously challenging due to the fact that it is non-differentiable, and
hence cannot be optimised directly using gradient-descent methods. To this end,
we introduce an objective that optimises instead a smoothed approximation of
AP, coined Smooth-AP. Smooth-AP is a plug-and-play objective function that
allows for end-to-end training of deep networks with a simple and elegant
implementation. We also present an analysis for why directly optimising the
ranking based metric of AP offers benefits over other deep metric learning
losses. We apply Smooth-AP to standard retrieval benchmarks: Stanford Online
products and VehicleID, and also evaluate on larger-scale datasets: INaturalist
for fine-grained category retrieval, and VGGFace2 and IJB-C for face retrieval.
In all cases, we improve the performance over the state-of-the-art, especially
for larger-scale datasets, thus demonstrating the effectiveness and scalability
of Smooth-AP to real-world scenarios.