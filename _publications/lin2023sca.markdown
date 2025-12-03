---
layout: publication
title: 'Sca-pvnet: Self-and-cross Attention Based Aggregation Of Point Cloud And Multi-view
  For 3D Object Retrieval'
authors: Dongyun Lin, Yi Cheng, Aiyuan Guo, Shangbo Mao, Yiqun Li
conference: Arxiv
year: 2023
bibkey: lin2023sca
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.10601'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Lin et al.
---
To address 3D object retrieval, substantial efforts have been made to
generate highly discriminative descriptors of 3D objects represented by a
single modality, e.g., voxels, point clouds or multi-view images. It is
promising to leverage the complementary information from multi-modality
representations of 3D objects to further improve retrieval performance.
However, multi-modality 3D object retrieval is rarely developed and analyzed on
large-scale datasets. In this paper, we propose self-and-cross attention based
aggregation of point cloud and multi-view images (SCA-PVNet) for 3D object
retrieval. With deep features extracted from point clouds and multi-view
images, we design two types of feature aggregation modules, namely the
In-Modality Aggregation Module (IMAM) and the Cross-Modality Aggregation Module
(CMAM), for effective feature fusion. IMAM leverages a self-attention mechanism
to aggregate multi-view features while CMAM exploits a cross-attention
mechanism to interact point cloud features with multi-view features. The final
descriptor of a 3D object for object retrieval can be obtained via
concatenating the aggregated features from both modules. Extensive experiments
and analysis are conducted on three datasets, ranging from small to large
scale, to show the superiority of the proposed SCA-PVNet over the
state-of-the-art methods.