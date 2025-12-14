---
layout: publication
title: A Novel Graph-theoretic Deep Representation Learning Method For Multi-label
  Remote Sensing Image Retrieval
authors: "Gencer Sumbul, Beg\xFCm Demir"
conference: 2021 IEEE International Geoscience and Remote Sensing Symposium IGARSS
year: 2021
bibkey: sumbul2021a
citations: 1
additional_links: [{name: Code, url: 'https://git.tu-berlin.de/rsim/GT-DRL-CBIR'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.00506'}]
tags: [Graph-based ANN, Tools & Libraries, RSS, Image Retrieval]
short_authors: "Gencer Sumbul, Beg\xFCm Demir"
---
This paper presents a novel graph-theoretic deep representation learning
method in the framework of multi-label remote sensing (RS) image retrieval
problems. The proposed method aims to extract and exploit multi-label
co-occurrence relationships associated to each RS image in the archive. To this
end, each training image is initially represented with a graph structure that
provides region-based image representation combining both local information and
the related spatial organization. Unlike the other graph-based methods, the
proposed method contains a novel learning strategy to train a deep neural
network for automatically predicting a graph structure of each RS image in the
archive. This strategy employs a region representation learning loss function
to characterize the image content based on its multi-label co-occurrence
relationship. Experimental results show the effectiveness of the proposed
method for retrieval problems in RS compared to state-of-the-art deep
representation learning methods. The code of the proposed method is publicly
available at https://git.tu-berlin.de/rsim/GT-DRL-CBIR .