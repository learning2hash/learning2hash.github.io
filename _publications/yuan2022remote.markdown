---
layout: publication
title: Remote Sensing Cross-modal Text-image Retrieval Based On Global And Local Information
authors: Zhiqiang Yuan, Wenkai Zhang, Changyuan Tian, Xuee Rong, Zhengyuan Zhang,
  Hongqi Wang, Kun Fu, Xian Sun
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2022
bibkey: yuan2022remote
citations: 149
additional_links: [{name: Code, url: 'https://github.com/xiaoyuan1996/GaLR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2204.09860'}]
tags: [Evaluation, Image Retrieval, Re-ranking, Datasets, Tools & Libraries]
short_authors: Yuan et al.
---
Cross-modal remote sensing text-image retrieval (RSCTIR) has recently become
an urgent research hotspot due to its ability of enabling fast and flexible
information extraction on remote sensing (RS) images. However, current RSCTIR
methods mainly focus on global features of RS images, which leads to the
neglect of local features that reflect target relationships and saliency. In
this article, we first propose a novel RSCTIR framework based on global and
local information (GaLR), and design a multi-level information dynamic fusion
(MIDF) module to efficaciously integrate features of different levels. MIDF
leverages local information to correct global information, utilizes global
information to supplement local information, and uses the dynamic addition of
the two to generate prominent visual representation. To alleviate the pressure
of the redundant targets on the graph convolution network (GCN) and to improve
the model s attention on salient instances during modeling local features, the
de-noised representation matrix and the enhanced adjacency matrix (DREA) are
devised to assist GCN in producing superior local representations. DREA not
only filters out redundant features with high similarity, but also obtains more
powerful local features by enhancing the features of prominent objects.
Finally, to make full use of the information in the similarity matrix during
inference, we come up with a plug-and-play multivariate rerank (MR) algorithm.
The algorithm utilizes the k nearest neighbors of the retrieval results to
perform a reverse search, and improves the performance by combining multiple
components of bidirectional retrieval. Extensive experiments on public datasets
strongly demonstrate the state-of-the-art performance of GaLR methods on the
RSCTIR task. The code of GaLR method, MR algorithm, and corresponding files
have been made available at https://github.com/xiaoyuan1996/GaLR .