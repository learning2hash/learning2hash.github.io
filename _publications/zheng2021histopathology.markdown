---
layout: publication
title: Histopathology WSI Encoding Based On Gcns For Scalable And Efficient Retrieval
  Of Diagnostically Relevant Regions
authors: Yushan Zheng, Zhiguo Jiang, Haopeng Zhang, Fengying Xie, Jun Shi, Chenghai
  Xue
conference: Arxiv
year: 2021
bibkey: zheng2021histopathology
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.07878'}]
tags: ["Evaluation", "Image Retrieval", "Scalability", "Similarity Search"]
short_authors: Zheng et al.
---
Content-based histopathological image retrieval (CBHIR) has become popular in
recent years in the domain of histopathological image analysis. CBHIR systems
provide auxiliary diagnosis information for pathologists by searching for and
returning regions that are contently similar to the region of interest (ROI)
from a pre-established database. While, it is challenging and yet significant
in clinical applications to retrieve diagnostically relevant regions from a
database that consists of histopathological whole slide images (WSIs) for a
query ROI. In this paper, we propose a novel framework for regions retrieval
from WSI-database based on hierarchical graph convolutional networks (GCNs) and
Hash technique. Compared to the present CBHIR framework, the structural
information of WSI is preserved through graph embedding of GCNs, which makes
the retrieval framework more sensitive to regions that are similar in tissue
distribution. Moreover, benefited from the hierarchical GCN structures, the
proposed framework has good scalability for both the size and shape variation
of ROIs. It allows the pathologist defining query regions using free curves
according to the appearance of tissue. Thirdly, the retrieval is achieved based
on Hash technique, which ensures the framework is efficient and thereby
adequate for practical large-scale WSI-database. The proposed method was
validated on two public datasets for histopathological WSI analysis and
compared to the state-of-the-art methods. The proposed method achieved mean
average precision above 0.857 on the ACDC-LungHP dataset and above 0.864 on the
Camelyon16 dataset in the irregular region retrieval tasks, which are superior
to the state-of-the-art methods. The average retrieval time from a database
within 120 WSIs is 0.802 ms.