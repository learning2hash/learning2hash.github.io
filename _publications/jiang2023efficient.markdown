---
layout: publication
title: Efficient Match Pair Retrieval For Large-scale UAV Images Via Graph Indexed
  Global Descriptor
authors: San Jiang, Yichen Ma, Qingquan Li, Wanshou Jiang, Bingxuan Guo, Lelin Li,
  Lizhe Wang
conference: IEEE Journal of Selected Topics in Applied Earth Observations and Remote
  Sensing
year: 2023
bibkey: jiang2023efficient
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.04520'}]
tags: ["Efficiency", "Graph Based ANN", "Image Retrieval", "Scalability"]
short_authors: Jiang et al.
---
SfM (Structure from Motion) has been extensively used for UAV (Unmanned
Aerial Vehicle) image orientation. Its efficiency is directly influenced by
feature matching. Although image retrieval has been extensively used for match
pair selection, high computational costs are consumed due to a large number of
local features and the large size of the used codebook. Thus, this paper
proposes an efficient match pair retrieval method and implements an integrated
workflow for parallel SfM reconstruction. First, an individual codebook is
trained online by considering the redundancy of UAV images and local features,
which avoids the ambiguity of training codebooks from other datasets. Second,
local features of each image are aggregated into a single high-dimension global
descriptor through the VLAD (Vector of Locally Aggregated Descriptors)
aggregation by using the trained codebook, which remarkably reduces the number
of features and the burden of nearest neighbor searching in image indexing.
Third, the global descriptors are indexed via the HNSW (Hierarchical Navigable
Small World) based graph structure for the nearest neighbor searching. Match
pairs are then retrieved by using an adaptive threshold selection strategy and
utilized to create a view graph for divide-and-conquer based parallel SfM
reconstruction. Finally, the performance of the proposed solution has been
verified using three large-scale UAV datasets. The test results demonstrate
that the proposed solution accelerates match pair retrieval with a speedup
ratio ranging from 36 to 108 and improves the efficiency of SfM reconstruction
with competitive accuracy in both relative and absolute orientation.