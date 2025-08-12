---
layout: publication
title: Unleashing The Power Of Emojis In Texts Via Self-supervised Graph Pre-training
authors: Zhou Zhang, Dongzeng Tan, Jiaan Wang, Yilong Chen, Jiarong Xu
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: zhang2024unleashing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.14552'}]
tags: ["EMNLP", "Self-Supervised"]
short_authors: Zhang et al.
---
Emojis have gained immense popularity on social platforms, serving as a
common means to supplement or replace text. However, existing data mining
approaches generally either completely ignore or simply treat emojis as
ordinary Unicode characters, which may limit the model's ability to grasp the
rich semantic information in emojis and the interaction between emojis and
texts. Thus, it is necessary to release the emoji's power in social media data
mining. To this end, we first construct a heterogeneous graph consisting of
three types of nodes, i.e. post, word and emoji nodes to improve the
representation of different elements in posts. The edges are also well-defined
to model how these three elements interact with each other. To facilitate the
sharing of information among post, word and emoji nodes, we propose a graph
pre-train framework for text and emoji co-modeling, which contains two graph
pre-training tasks: node-level graph contrastive learning and edge-level link
reconstruction learning. Extensive experiments on the Xiaohongshu and Twitter
datasets with two types of downstream tasks demonstrate that our approach
proves significant improvement over previous strong baseline methods.