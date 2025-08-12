---
layout: publication
title: Exploring Hierarchical Graph Representation For Large-scale Zero-shot Image
  Classification
authors: Kai Yi, Xiaoqian Shen, Yunhao Gou, Mohamed Elhoseiny
conference: Lecture Notes in Computer Science
year: 2022
bibkey: yi2022exploring
citations: 8
additional_links: [{name: Code, url: 'https://kaiyi.me/p/hgrnet.html'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.01386'}]
tags: ["Few Shot & Zero Shot", "Scalability"]
short_authors: Yi et al.
---
The main question we address in this paper is how to scale up visual
recognition of unseen classes, also known as zero-shot learning, to tens of
thousands of categories as in the ImageNet-21K benchmark. At this scale,
especially with many fine-grained categories included in ImageNet-21K, it is
critical to learn quality visual semantic representations that are
discriminative enough to recognize unseen classes and distinguish them from
seen ones. We propose a *H*ierarchical *G*raphical knowledge
*R*epresentation framework for the confidence-based classification method,
dubbed as HGR-Net. Our experimental results demonstrate that HGR-Net can grasp
class inheritance relations by utilizing hierarchical conceptual knowledge. Our
method significantly outperformed all existing techniques, boosting the
performance by 7% compared to the runner-up approach on the ImageNet-21K
benchmark. We show that HGR-Net is learning-efficient in few-shot scenarios. We
also analyzed our method on smaller datasets like ImageNet-21K-P, 2-hops and
3-hops, demonstrating its generalization ability. Our benchmark and code are
available at https://kaiyi.me/p/hgrnet.html.