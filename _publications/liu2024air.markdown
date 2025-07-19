---
layout: publication
title: 'Air-hloc: Adaptive Retrieved Images Selection For Efficient Visual Localisation'
authors: Liu et al.
conference: Lecture Notes in Computer Science
year: 2024
bibkey: liu2024air
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.18281'}]
---
State-of-the-art hierarchical localisation pipelines (HLoc) employ image
retrieval (IR) to establish 2D-3D correspondences by selecting the top-\\(k\\) most
similar images from a reference database. While increasing \\(k\\) improves
localisation robustness, it also linearly increases computational cost and
runtime, creating a significant bottleneck. This paper investigates the
relationship between global and local descriptors, showing that greater
similarity between the global descriptors of query and database images
increases the proportion of feature matches. Low similarity queries
significantly benefit from increasing \\(k\\), while high similarity queries
rapidly experience diminishing returns. Building on these observations, we
propose an adaptive strategy that adjusts \\(k\\) based on the similarity between
the query's global descriptor and those in the database, effectively mitigating
the feature-matching bottleneck. Our approach optimizes processing time without
sacrificing accuracy. Experiments on three indoor and outdoor datasets show
that AIR-HLoc reduces feature matching time by up to 30%, while preserving
state-of-the-art accuracy. The results demonstrate that AIR-HLoc facilitates a
latency-sensitive localisation system.