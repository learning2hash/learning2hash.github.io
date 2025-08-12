---
layout: publication
title: 'Jacobinerf: Nerf Shaping With Mutual Information Gradients'
authors: Xiaomeng Xu, Yanchao Yang, Kaichun Mo, Boxiao Pan, Li Yi, Leonidas Guibas
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: xu2023jacobinerf
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.00341'}]
tags: ["CVPR"]
short_authors: Xu et al.
---
We propose a method that trains a neural radiance field (NeRF) to encode not
only the appearance of the scene but also semantic correlations between scene
points, regions, or entities -- aiming to capture their mutual co-variation
patterns. In contrast to the traditional first-order photometric reconstruction
objective, our method explicitly regularizes the learning dynamics to align the
Jacobians of highly-correlated entities, which proves to maximize the mutual
information between them under random scene perturbations. By paying attention
to this second-order information, we can shape a NeRF to express semantically
meaningful synergies when the network weights are changed by a delta along the
gradient of a single entity, region, or even a point. To demonstrate the merit
of this mutual information modeling, we leverage the coordinated behavior of
scene entities that emerges from our shaping to perform label propagation for
semantic and instance segmentation. Our experiments show that a JacobiNeRF is
more efficient in propagating annotations among 2D pixels and 3D points
compared to NeRFs without mutual information shaping, especially in extremely
sparse label regimes -- thus reducing annotation burden. The same machinery can
further be used for entity selection or scene modifications.