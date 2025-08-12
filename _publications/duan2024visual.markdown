---
layout: publication
title: Visual-semantic Graph Matching Net For Zero-shot Learning
authors: Bowen Duan, Shiming Chen, Yufei Guo, Guo-Sen Xie, Weiping Ding, Yisong Wang
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2024
bibkey: duan2024visual
citations: 0
additional_links: [{name: Code, url: 'https://github.com/dbwfd/VSGMN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.11351'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Duan et al.
---
Zero-shot learning (ZSL) aims to leverage additional semantic information to
recognize unseen classes. To transfer knowledge from seen to unseen classes,
most ZSL methods often learn a shared embedding space by simply aligning visual
embeddings with semantic prototypes. However, methods trained under this
paradigm often struggle to learn robust embedding space because they align the
two modalities in an isolated manner among classes, which ignore the crucial
class relationship during the alignment process. To address the aforementioned
challenges, this paper proposes a Visual-Semantic Graph Matching Net, termed as
VSGMN, which leverages semantic relationships among classes to aid in
visual-semantic embedding. VSGMN employs a Graph Build Network (GBN) and a
Graph Matching Network (GMN) to achieve two-stage visual-semantic alignment.
Specifically, GBN first utilizes an embedding-based approach to build visual
and semantic graphs in the semantic space and align the embedding with its
prototype for first-stage alignment. Additionally, to supplement unseen class
relations in these graphs, GBN also build the unseen class nodes based on
semantic relationships. In the second stage, GMN continuously integrates
neighbor and cross-graph information into the constructed graph nodes, and
aligns the node relationships between the two graphs under the class
relationship constraint. Extensive experiments on three benchmark datasets
demonstrate that VSGMN achieves superior performance in both conventional and
generalized ZSL scenarios. The implementation of our VSGMN and experimental
results are available at github: https://github.com/dbwfd/VSGMN