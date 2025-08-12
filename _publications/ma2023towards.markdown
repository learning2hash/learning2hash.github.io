---
layout: publication
title: Towards Local Visual Modeling For Image Captioning
authors: Yiwei Ma, Jiayi Ji, Xiaoshuai Sun, Yiyi Zhou, Rongrong Ji
conference: Pattern Recognition
year: 2023
bibkey: ma2023towards
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.06098'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ma et al.
---
In this paper, we study the local visual modeling with grid features for
image captioning, which is critical for generating accurate and detailed
captions. To achieve this target, we propose a Locality-Sensitive Transformer
Network (LSTNet) with two novel designs, namely Locality-Sensitive Attention
(LSA) and Locality-Sensitive Fusion (LSF). LSA is deployed for the intra-layer
interaction in Transformer via modeling the relationship between each grid and
its neighbors. It reduces the difficulty of local object recognition during
captioning. LSF is used for inter-layer information fusion, which aggregates
the information of different encoder layers for cross-layer semantical
complementarity. With these two novel designs, the proposed LSTNet can model
the local visual information of grid features to improve the captioning
quality. To validate LSTNet, we conduct extensive experiments on the
competitive MS-COCO benchmark. The experimental results show that LSTNet is not
only capable of local visual modeling, but also outperforms a bunch of
state-of-the-art captioning models on offline and online testings, i.e., 134.8
CIDEr and 136.3 CIDEr, respectively. Besides, the generalization of LSTNet is
also verified on the Flickr8k and Flickr30k datasets