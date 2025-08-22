---
layout: publication
title: 'MUST: An Effective And Scalable Framework For Multimodal Search Of Target
  Modality'
authors: Mengzhao Wang, Xiangyu Ke, Xiaoliang Xu, Lu Chen, Yunjun Gao, Pinpin Huang,
  Runkai Zhu
conference: 2024 IEEE 40th International Conference on Data Engineering (ICDE)
year: 2024
bibkey: wang2023must
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.06397'}]
tags: ["Datasets", "Efficiency", "Graph Based ANN", "Scalability", "Tools & Libraries"]
short_authors: Wang et al.
---
We investigate the problem of multimodal search of target modality, where the
task involves enhancing a query in a specific target modality by integrating
information from auxiliary modalities. The goal is to retrieve relevant objects
whose contents in the target modality match the specified multimodal query. The
paper first introduces two baseline approaches that integrate techniques from
the Database, Information Retrieval, and Computer Vision communities. These
baselines either merge the results of separate vector searches for each
modality or perform a single-channel vector search by fusing all modalities.
However, both baselines have limitations in terms of efficiency and accuracy as
they fail to adequately consider the varying importance of fusing information
across modalities. To overcome these limitations, the paper proposes a novel
framework, called MUST. Our framework employs a hybrid fusion mechanism,
combining different modalities at multiple stages. Notably, we leverage vector
weight learning to determine the importance of each modality, thereby enhancing
the accuracy of joint similarity measurement. Additionally, the proposed
framework utilizes a fused proximity graph index, enabling efficient joint
search for multimodal queries. MUST offers several other advantageous
properties, including pluggable design to integrate any advanced embedding
techniques, user flexibility to customize weight preferences, and modularized
index construction. Extensive experiments on real-world datasets demonstrate
the superiority of MUST over the baselines in terms of both search accuracy and
efficiency. Our framework achieves over 10x faster search times while attaining
an average of 93% higher accuracy. Furthermore, MUST exhibits scalability to
datasets containing more than 10 million data elements.