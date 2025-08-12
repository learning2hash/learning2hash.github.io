---
layout: publication
title: Intermediate Prototype Mining Transformer For Few-shot Semantic Segmentation
authors: Yuanwei Liu, Nian Liu, Xiwen Yao, Junwei Han
conference: Arxiv
year: 2022
bibkey: liu2022intermediate
citations: 29
additional_links: [{name: Code, url: 'https://github.com/LIUYUANWEI98/IPMT'}, {name: Paper,
    url: 'https://arxiv.org/abs/2210.06780'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot semantic segmentation aims to segment the target objects in query
under the condition of a few annotated support images. Most previous works
strive to mine more effective category information from the support to match
with the corresponding objects in query. However, they all ignored the category
information gap between query and support images. If the objects in them show
large intra-class diversity, forcibly migrating the category information from
the support to the query is ineffective. To solve this problem, we are the
first to introduce an intermediate prototype for mining both deterministic
category information from the support and adaptive category knowledge from the
query. Specifically, we design an Intermediate Prototype Mining Transformer
(IPMT) to learn the prototype in an iterative way. In each IPMT layer, we
propagate the object information in both support and query features to the
prototype and then use it to activate the query feature map. By conducting this
process iteratively, both the intermediate prototype and the query feature can
be progressively improved. At last, the final query feature is used to yield
precise segmentation prediction. Extensive experiments on both PASCAL-5i and
COCO-20i datasets clearly verify the effectiveness of our IPMT and show that it
outperforms previous state-of-the-art methods by a large margin. Code is
available at https://github.com/LIUYUANWEI98/IPMT