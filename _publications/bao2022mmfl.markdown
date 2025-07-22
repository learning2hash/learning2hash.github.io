---
layout: publication
title: 'Mmfl-net: Multi-scale And Multi-granularity Feature Learning For Cross-domain
  Fashion Retrieval'
authors: Bao et al.
conference: Multimedia Tools and Applications
year: 2022
bibkey: bao2022mmfl
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.15128'}]
---
Instance-level image retrieval in fashion is a challenging issue owing to its
increasing importance in real-scenario visual fashion search. Cross-domain
fashion retrieval aims to match the unconstrained customer images as queries
for photographs provided by retailers; however, it is a difficult task due to a
wide range of consumer-to-shop (C2S) domain discrepancies and also considering
that clothing image is vulnerable to various non-rigid deformations. To this
end, we propose a novel multi-scale and multi-granularity feature learning
network (MMFL-Net), which can jointly learn global-local aggregation feature
representations of clothing images in a unified framework, aiming to train a
cross-domain model for C2S fashion visual similarity. First, a new
semantic-spatial feature fusion part is designed to bridge the semantic-spatial
gap by applying top-down and bottom-up bidirectional multi-scale feature
fusion. Next, a multi-branch deep network architecture is introduced to capture
global salient, part-informed, and local detailed information, and extracting
robust and discrimination feature embedding by integrating the similarity
learning of coarse-to-fine embedding with the multiple granularities. Finally,
the improved trihard loss, center loss, and multi-task classification loss are
adopted for our MMFL-Net, which can jointly optimize intra-class and
inter-class distance and thus explicitly improve intra-class compactness and
inter-class discriminability between its visual representations for feature
learning. Furthermore, our proposed model also combines the multi-task
attribute recognition and classification module with multi-label semantic
attributes and product ID labels. Experimental results demonstrate that our
proposed MMFL-Net achieves significant improvement over the state-of-the-art
methods on the two datasets, DeepFashion-C2S and Street2Shop.