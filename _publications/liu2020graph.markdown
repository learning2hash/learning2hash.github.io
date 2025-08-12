---
layout: publication
title: Graph Structured Network For Image-text Matching
authors: Chunxiao Liu, Zhendong Mao, Tianzhu Zhang, Hongtao Xie, Bin Wang, Yongdong
  Zhang
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: liu2020graph
citations: 228
additional_links: [{name: Code, url: 'https://github.com/CrossmodalGroup/GSMN'}, {
    name: Paper, url: 'https://arxiv.org/abs/2004.00277'}]
tags: ["CVPR"]
short_authors: Liu et al.
---
Image-text matching has received growing interest since it bridges vision and
language. The key challenge lies in how to learn correspondence between image
and text. Existing works learn coarse correspondence based on object
co-occurrence statistics, while failing to learn fine-grained phrase
correspondence. In this paper, we present a novel Graph Structured Matching
Network (GSMN) to learn fine-grained correspondence. The GSMN explicitly models
object, relation and attribute as a structured phrase, which not only allows to
learn correspondence of object, relation and attribute separately, but also
benefits to learn fine-grained correspondence of structured phrase. This is
achieved by node-level matching and structure-level matching. The node-level
matching associates each node with its relevant nodes from another modality,
where the node can be object, relation or attribute. The associated nodes then
jointly infer fine-grained correspondence by fusing neighborhood associations
at structure-level matching. Comprehensive experiments show that GSMN
outperforms state-of-the-art methods on benchmarks, with relative Recall@1
improvements of nearly 7% and 2% on Flickr30K and MSCOCO, respectively. Code
will be released at: https://github.com/CrossmodalGroup/GSMN.