---
layout: publication
title: Learning Universal And Robust 3D Molecular Representations With Graph Convolutional
  Networks
authors: Shuo Zhang, Yang Liu, Li Xie, Lei Xie
conference: Arxiv
year: 2023
bibkey: zhang2023learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.12491'}]
tags: []
short_authors: Zhang et al.
---
To learn accurate representations of molecules, it is essential to consider
both chemical and geometric features. To encode geometric information, many
descriptors have been proposed in constrained circumstances for specific types
of molecules and do not have the properties to be ``robust": 1. Invariant to
rotations and translations; 2. Injective when embedding molecular structures.
In this work, we propose a universal and robust Directional Node Pair (DNP)
descriptor based on the graph representations of 3D molecules. Our DNP
descriptor is robust compared to previous ones and can be applied to multiple
molecular types. To combine the DNP descriptor and chemical features in
molecules, we construct the Robust Molecular Graph Convolutional Network
(RoM-GCN) which is capable to take both node and edge features into
consideration when generating molecule representations. We evaluate our model
on protein and small molecule datasets. Our results validate the superiority of
the DNP descriptor in incorporating 3D geometric information of molecules.
RoM-GCN outperforms all compared baselines.