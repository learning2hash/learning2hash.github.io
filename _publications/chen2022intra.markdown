---
layout: publication
title: Intra-modal Constraint Loss For Image-text Retrieval
authors: Jianan Chen, Lu Zhang, Qiong Wang, Cong Bai, Kidiyo Kpalma
conference: 2022 IEEE International Conference on Image Processing (ICIP)
year: 2022
bibkey: chen2022intra
citations: 6
additional_links: [{name: Code, url: 'https://github.com/CanonChen/IMC.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.05024'}]
tags: ["Datasets", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Chen et al.
---
Cross-modal retrieval has drawn much attention in both computer vision and
natural language processing domains. With the development of convolutional and
recurrent neural networks, the bottleneck of retrieval across image-text
modalities is no longer the extraction of image and text features but an
efficient loss function learning in embedding space. Many loss functions try to
closer pairwise features from heterogeneous modalities. This paper proposes a
method for learning joint embedding of images and texts using an intra-modal
constraint loss function to reduce the violation of negative pairs from the
same homogeneous modality. Experimental results show that our approach
outperforms state-of-the-art bi-directional image-text retrieval methods on
Flickr30K and Microsoft COCO datasets. Our code is publicly available:
https://github.com/CanonChen/IMC.