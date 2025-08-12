---
layout: publication
title: Contrastive Learning For Unsupervised Radar Place Recognition
authors: Matthew Gadd, Daniele de Martini, Paul Newman
conference: 2021 20th International Conference on Advanced Robotics (ICAR)
year: 2021
bibkey: gadd2021contrastive
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.02744'}]
tags: ["Unsupervised"]
short_authors: Matthew Gadd, Daniele de Martini, Paul Newman
---
We learn, in an unsupervised way, an embedding from sequences of radar images
that is suitable for solving the place recognition problem with complex radar
data. Our method is based on invariant instance feature learning but is
tailored for the task of re-localisation by exploiting for data augmentation
the temporal successivity of data as collected by a mobile platform moving
through the scene smoothly. We experiment across two prominent urban radar
datasets totalling over 400 km of driving and show that we achieve a new radar
place recognition state-of-the-art. Specifically, the proposed system proves
correct for 98.38% of the queries that it is presented with over a challenging
re-localisation sequence, using only the single nearest neighbour in the
learned metric space. We also find that our learned model shows better
understanding of out-of-lane loop closures at arbitrary orientation than
non-learned radar scan descriptors.