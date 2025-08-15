---
layout: publication
title: 'Edtformer: An Efficient Decoder Transformer For Visual Place Recognition'
authors: Tong Jin, Feng Lu, Shuyu Hu, Chun Yuan, Yunpeng Liu
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2025
bibkey: jin2024edtformer
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.00784'}]
tags: ["Datasets", "Evaluation", "Re-Ranking", "Robustness"]
short_authors: Jin et al.
---
Visual place recognition (VPR) aims to determine the general geographical location of a query image by retrieving visually similar images from a large geo-tagged database. To obtain a global representation for each place image, most approaches typically focus on the aggregation of deep features extracted from a backbone through using current prominent architectures (e.g., CNNs, MLPs, pooling layer, and transformer encoder), giving little attention to the transformer decoder. However, we argue that its strong capability to capture contextual dependencies and generate accurate features holds considerable potential for the VPR task. To this end, we propose an Efficient Decoder Transformer (EDTformer) for feature aggregation, which consists of several stacked simplified decoder blocks followed by two linear layers to directly produce robust and discriminative global representations. Specifically, we do this by formulating deep features as the keys and values, as well as a set of learnable parameters as the queries. Our EDTformer can fully utilize the contextual information within deep features, then gradually decode and aggregate the effective features into the learnable queries to output the global representations. Moreover, to provide more powerful deep features for EDTformer and further facilitate the robustness, we use the foundation model DINOv2 as the backbone and propose a Low-rank Parallel Adaptation (LoPA) method to enhance its performance in VPR, which can refine the intermediate features of the backbone progressively in a memory- and parameter-efficient way. As a result, our method not only outperforms single-stage VPR methods on multiple benchmark datasets, but also outperforms two-stage VPR methods which add a re-ranking with considerable cost. Code will be available at https://github.com/Tong-Jin01/EDTformer.