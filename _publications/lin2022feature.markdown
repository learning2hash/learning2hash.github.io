---
layout: publication
title: Feature Selective Transformer For Semantic Image Segmentation
authors: Fangjian Lin, Tianyi Wu, Sitong Wu, Shengwei Tian, Guodong Guo
conference: Arxiv
year: 2022
bibkey: lin2022feature
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14124'}]
tags: ["Transformer Based ANN"]
short_authors: Lin et al.
---
Recently, it has attracted more and more attentions to fuse multi-scale
features for semantic image segmentation. Various works were proposed to employ
progressive local or global fusion, but the feature fusions are not rich enough
for modeling multi-scale context features. In this work, we focus on fusing
multi-scale features from Transformer-based backbones for semantic
segmentation, and propose a Feature Selective Transformer (FeSeFormer), which
aggregates features from all scales (or levels) for each query feature.
Specifically, we first propose a Scale-level Feature Selection (SFS) module,
which can choose an informative subset from the whole multi-scale feature set
for each scale, where those features that are important for the current scale
(or level) are selected and the redundant are discarded. Furthermore, we
propose a Full-scale Feature Fusion (FFF) module, which can adaptively fuse
features of all scales for queries. Based on the proposed SFS and FFF modules,
we develop a Feature Selective Transformer (FeSeFormer), and evaluate our
FeSeFormer on four challenging semantic segmentation benchmarks, including
PASCAL Context, ADE20K, COCO-Stuff 10K, and Cityscapes, outperforming the
state-of-the-art.