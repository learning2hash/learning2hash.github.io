---
layout: publication
title: Supervised Auto-Encoding Twin-Bottleneck Hashing
authors: Chen Yuan, Marchand-Maillet Stéphane
conference: "Arxiv"
year: 2023
bibkey: chen2023supervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.11122"}
tags: ['ARXIV', 'Graph', 'Supervised', 'Unsupervised']
---
Deep hashing has shown to be a complexity-efficient solution for the Approximate Nearest Neighbor search problem in high dimensional space. Many methods usually build the loss function from pairwise or triplet data points to capture the local similarity structure. Other existing methods construct the similarity graph and consider all points simultaneously. Auto-encoding Twin-bottleneck Hashing is one such method that dynamically builds the graph. Specifically each input data is encoded into a binary code and a continuous variable or the so-called twin bottlenecks. The similarity graph is then computed from these binary codes which get updated consistently during the training. In this work we generalize the original model into a supervised deep hashing network by incorporating the label information. In addition we examine the differences of codes structure between these two networks and consider the class imbalance problem especially in multi-labeled datasets. Experiments on three datasets yield statistically significant improvement against the original model. Results are also comparable and competitive to other supervised methods.
