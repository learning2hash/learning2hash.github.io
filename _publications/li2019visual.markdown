---
layout: publication
title: Visual Semantic Reasoning For Image-text Matching
authors: Kunpeng Li, Yulun Zhang, Kai Li, Yuanyuan Li, Yun Fu
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: li2019visual
citations: 495
additional_links: [{name: Code, url: 'https://github.com/KunpengLi1994/VSRN'}, {name: Paper,
    url: 'https://arxiv.org/abs/1909.02701'}]
tags: ["ICCV", "Image Retrieval"]
short_authors: Li et al.
---
Image-text matching has been a hot research topic bridging the vision and
language areas. It remains challenging because the current representation of
image usually lacks global semantic concepts as in its corresponding text
caption. To address this issue, we propose a simple and interpretable reasoning
model to generate visual representation that captures key objects and semantic
concepts of a scene. Specifically, we first build up connections between image
regions and perform reasoning with Graph Convolutional Networks to generate
features with semantic relationships. Then, we propose to use the gate and
memory mechanism to perform global semantic reasoning on these
relationship-enhanced features, select the discriminative information and
gradually generate the representation for the whole scene. Experiments validate
that our method achieves a new state-of-the-art for the image-text matching on
MS-COCO and Flickr30K datasets. It outperforms the current best method by 6.8%
relatively for image retrieval and 4.8% relatively for caption retrieval on
MS-COCO (Recall@1 using 1K test set). On Flickr30K, our model improves image
retrieval by 12.6% relatively and caption retrieval by 5.8% relatively
(Recall@1). Our code is available at https://github.com/KunpengLi1994/VSRN.