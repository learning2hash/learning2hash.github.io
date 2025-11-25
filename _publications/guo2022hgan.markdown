---
layout: publication
title: 'HGAN: Hierarchical Graph Alignment Network For Image-text Retrieval'
authors: Jie Guo, Meiting Wang, Yan Zhou, Bin Song, Yuhao Chi, Wei Fan, Jianglong
  Chang
conference: Arxiv
year: 2022
bibkey: guo2022hgan
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08281'}]
tags: ["Datasets", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Guo et al.
---
Image-text retrieval (ITR) is a challenging task in the field of multimodal
information processing due to the semantic gap between different modalities. In
recent years, researchers have made great progress in exploring the accurate
alignment between image and text. However, existing works mainly focus on the
fine-grained alignment between image regions and sentence fragments, which
ignores the guiding significance of context background information. Actually,
integrating the local fine-grained information and global context background
information can provide more semantic clues for retrieval. In this paper, we
propose a novel Hierarchical Graph Alignment Network (HGAN) for image-text
retrieval. First, to capture the comprehensive multimodal features, we
construct the feature graphs for the image and text modality respectively.
Then, a multi-granularity shared space is established with a designed
Multi-granularity Feature Aggregation and Rearrangement (MFAR) module, which
enhances the semantic corresponding relations between the local and global
information, and obtains more accurate feature representations for the image
and text modalities. Finally, the ultimate image and text features are further
refined through three-level similarity functions to achieve the hierarchical
alignment. To justify the proposed model, we perform extensive experiments on
MS-COCO and Flickr30K datasets. Experimental results show that the proposed
HGAN outperforms the state-of-the-art methods on both datasets, which
demonstrates the effectiveness and superiority of our model.