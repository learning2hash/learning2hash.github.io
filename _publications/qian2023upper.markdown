---
layout: publication
title: 'Upper Bounding Barlow Twins: A Novel Filter For Multi-relational Clustering'
authors: Xiaowei Qian, Bingheng Li, Zhao Kang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: qian2023upper
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.14066'}]
tags: ["AAAI"]
short_authors: Xiaowei Qian, Bingheng Li, Zhao Kang
---
Multi-relational clustering is a challenging task due to the fact that
diverse semantic information conveyed in multi-layer graphs is difficult to
extract and fuse. Recent methods integrate topology structure and node
attribute information through graph filtering. However, they often use a
low-pass filter without fully considering the correlation among multiple
graphs. To overcome this drawback, we propose to learn a graph filter motivated
by the theoretical analysis of Barlow Twins. We find that input with a negative
semi-definite inner product provides a lower bound for Barlow Twins loss, which
prevents it from reaching a better solution. We thus learn a filter that yields
an upper bound for Barlow Twins. Afterward, we design a simple clustering
architecture and demonstrate its state-of-the-art performance on four benchmark
datasets.