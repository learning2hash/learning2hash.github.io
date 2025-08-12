---
layout: publication
title: Part-aware Prototype Network For Few-shot Semantic Segmentation
authors: Yongfei Liu, Xiangyi Zhang, Songyang Zhang, Xuming He
conference: Lecture Notes in Computer Science
year: 2020
bibkey: liu2020part
citations: 284
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.06309'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot semantic segmentation aims to learn to segment new object classes
with only a few annotated examples, which has a wide range of real-world
applications. Most existing methods either focus on the restrictive setting of
one-way few-shot segmentation or suffer from incomplete coverage of object
regions. In this paper, we propose a novel few-shot semantic segmentation
framework based on the prototype representation. Our key idea is to decompose
the holistic class representation into a set of part-aware prototypes, capable
of capturing diverse and fine-grained object features. In addition, we propose
to leverage unlabeled data to enrich our part-aware prototypes, resulting in
better modeling of intra-class variations of semantic objects. We develop a
novel graph neural network model to generate and enhance the proposed
part-aware prototypes based on labeled and unlabeled images. Extensive
experimental evaluations on two benchmarks show that our method outperforms the
prior art with a sizable margin.