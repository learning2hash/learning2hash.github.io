---
layout: publication
title: 'Revisit Visual Representation In Analytics Taxonomy: A Compression Perspective'
authors: Yueyu Hu, Wenhan Yang, Haofeng Huang, Jiaying Liu
conference: Arxiv
year: 2021
bibkey: hu2021revisit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.08512'}]
tags: ["Efficiency"]
short_authors: Hu et al.
---
Visual analytics have played an increasingly critical role in the Internet of
Things, where massive visual signals have to be compressed and fed into
machines. But facing such big data and constrained bandwidth capacity, existing
image/video compression methods lead to very low-quality representations, while
existing feature compression techniques fail to support diversified visual
analytics applications/tasks with low-bit-rate representations. In this paper,
we raise and study the novel problem of supporting multiple machine vision
analytics tasks with the compressed visual representation, namely, the
information compression problem in analytics taxonomy. By utilizing the
intrinsic transferability among different tasks, our framework successfully
constructs compact and expressive representations at low bit-rates to support a
diversified set of machine vision tasks, including both high-level
semantic-related tasks and mid-level geometry analytic tasks. In order to
impose compactness in the representations, we propose a codebook-based
hyperprior, which helps map the representation into a low-dimensional manifold.
As it well fits the signal structure of the deep visual feature, it facilitates
more accurate entropy estimation, and results in higher compression efficiency.
With the proposed framework and the codebook-based hyperprior, we further
investigate the relationship of different task features owning different levels
of abstraction granularity. Experimental results demonstrate that with the
proposed scheme, a set of diversified tasks can be supported at a significantly
lower bit-rate, compared with existing compression schemes.