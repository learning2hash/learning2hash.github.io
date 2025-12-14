---
layout: publication
title: 'Amatformer: Efficient Feature Matching Via Anchor Matching Transformer'
authors: Bo Jiang, Shuxian Luo, Xiao Wang, Chuanfu Li, Jin Tang
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: jiang2023amatformer
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.19205'}]
tags: [Scalability, Evaluation, Efficiency]
short_authors: Jiang et al.
---
Learning based feature matching methods have been commonly studied in recent
years. The core issue for learning feature matching is to how to learn (1)
discriminative representations for feature points (or regions) within each
intra-image and (2) consensus representations for feature points across
inter-images. Recently, self- and cross-attention models have been exploited to
address this issue. However, in many scenes, features are coming with
large-scale, redundant and outliers contaminated. Previous
self-/cross-attention models generally conduct message passing on all primal
features which thus lead to redundant learning and high computational cost. To
mitigate limitations, inspired by recent seed matching methods, in this paper,
we propose a novel efficient Anchor Matching Transformer (AMatFormer) for the
feature matching problem. AMatFormer has two main aspects: First, it mainly
conducts self-/cross-attention on some anchor features and leverages these
anchor features as message bottleneck to learn the representations for all
primal features. Thus, it can be implemented efficiently and compactly. Second,
AMatFormer adopts a shared FFN module to further embed the features of two
images into the common domain and thus learn the consensus feature
representations for the matching problem. Experiments on several benchmarks
demonstrate the effectiveness and efficiency of the proposed AMatFormer
matching approach.