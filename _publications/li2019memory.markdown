---
layout: publication
title: Memory-based Neighbourhood Embedding For Visual Recognition
authors: Suichan Li, Dapeng Chen, Bin Liu, Nenghai Yu, Rui Zhao
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: li2019memory
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.04992'}]
tags: ["ICCV"]
short_authors: Li et al.
---
Learning discriminative image feature embeddings is of great importance to
visual recognition. To achieve better feature embeddings, most current methods
focus on designing different network structures or loss functions, and the
estimated feature embeddings are usually only related to the input images. In
this paper, we propose Memory-based Neighbourhood Embedding (MNE) to enhance a
general CNN feature by considering its neighbourhood. The method aims to solve
two critical problems, i.e., how to acquire more relevant neighbours in the
network training and how to aggregate the neighbourhood information for a more
discriminative embedding. We first augment an episodic memory module into the
network, which can provide more relevant neighbours for both training and
testing. Then the neighbours are organized in a tree graph with the target
instance as the root node. The neighbourhood information is gradually
aggregated to the root node in a bottom-up manner, and aggregation weights are
supervised by the class relationships between the nodes. We apply MNE on image
search and few shot learning tasks. Extensive ablation studies demonstrate the
effectiveness of each component, and our method significantly outperforms the
state-of-the-art approaches.