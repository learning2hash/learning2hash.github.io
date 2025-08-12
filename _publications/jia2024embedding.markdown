---
layout: publication
title: Embedding Generalized Semantic Knowledge Into Few-shot Remote Sensing Segmentation
authors: Yuyu Jia, Wei Huang, Junyu Gao, Qi Wang, Qiang Li
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2024
bibkey: jia2024embedding
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.13686'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Jia et al.
---
Few-shot segmentation (FSS) for remote sensing (RS) imagery leverages
supporting information from limited annotated samples to achieve query
segmentation of novel classes. Previous efforts are dedicated to mining
segmentation-guiding visual cues from a constrained set of support samples.
However, they still struggle to address the pronounced intra-class differences
in RS images, as sparse visual cues make it challenging to establish robust
class-specific representations. In this paper, we propose a holistic semantic
embedding (HSE) approach that effectively harnesses general semantic knowledge,
i.e., class description (CD) embeddings.Instead of the naive combination of CD
embeddings and visual features for segmentation decoding, we investigate
embedding the general semantic knowledge during the feature extraction
stage.Specifically, in HSE, a spatial dense interaction module allows the
interaction of visual support features with CD embeddings along the spatial
dimension via self-attention.Furthermore, a global content modulation module
efficiently augments the global information of the target category in both
support and query features, thanks to the transformative fusion of visual
features and CD embeddings.These two components holistically synergize general
CD embeddings and visual cues, constructing a robust class-specific
representation.Through extensive experiments on the standard FSS benchmark, the
proposed HSE approach demonstrates superior performance compared to peer work,
setting a new state-of-the-art.