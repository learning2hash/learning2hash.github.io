---
layout: publication
title: 'CDSM: Cascaded Deep Semantic Matching On Textual Graphs Leveraging Ad-hoc
  Neighbor Selection'
authors: Jing Yao, Zheng Liu, Junhan Yang, Zhicheng Dou, Xing Xie, Ji-Rong Wen
conference: Arxiv
year: 2022
bibkey: yao2022cdsm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.17171'}]
tags: [Tools & Libraries, Graph-based ANN]
short_authors: Yao et al.
---
Deep semantic matching aims to discriminate the relationship between
documents based on deep neural networks. In recent years, it becomes
increasingly popular to organize documents with a graph structure, then
leverage both the intrinsic document features and the extrinsic neighbor
features to derive discrimination. Most of the existing works mainly care about
how to utilize the presented neighbors, whereas limited effort is made to
filter appropriate neighbors. We argue that the neighbor features could be
highly noisy and partially useful. Thus, a lack of effective neighbor selection
will not only incur a great deal of unnecessary computation cost, but also
restrict the matching accuracy severely.
  In this work, we propose a novel framework, Cascaded Deep Semantic Matching
(CDSM), for accurate and efficient semantic matching on textual graphs. CDSM is
highlighted for its two-stage workflow. In the first stage, a lightweight
CNN-based ad-hod neighbor selector is deployed to filter useful neighbors for
the matching task with a small computation cost. We design both one-step and
multi-step selection methods. In the second stage, a high-capacity graph-based
matching network is employed to compute fine-grained relevance scores based on
the well-selected neighbors. It is worth noting that CDSM is a generic
framework which accommodates most of the mainstream graph-based semantic
matching networks. The major challenge is how the selector can learn to
discriminate the neighbors usefulness which has no explicit labels. To cope
with this problem, we design a weak-supervision strategy for optimization,
where we train the graph-based matching network at first and then the ad-hoc
neighbor selector is learned on top of the annotations from the matching
network.