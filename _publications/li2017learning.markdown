---
layout: publication
title: Learning Structured Semantic Embeddings For Visual Recognition
authors: Dong Li, Hsin-Ying Lee, Jia-Bin Huang, Shengjin Wang, Ming-Hsuan Yang
conference: Arxiv
year: 2017
bibkey: li2017learning
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.01237'}]
tags: []
short_authors: Li et al.
---
Numerous embedding models have been recently explored to incorporate semantic
knowledge into visual recognition. Existing methods typically focus on
minimizing the distance between the corresponding images and texts in the
embedding space but do not explicitly optimize the underlying structure. Our
key observation is that modeling the pairwise image-image relationship improves
the discrimination ability of the embedding model. In this paper, we propose
the structured discriminative and difference constraints to learn
visual-semantic embeddings. First, we exploit the discriminative constraints to
capture the intra- and inter-class relationships of image embeddings. The
discriminative constraints encourage separability for image instances of
different classes. Second, we align the difference vector between a pair of
image embeddings with that of the corresponding word embeddings. The difference
constraints help regularize image embeddings to preserve the semantic
relationships among word embeddings. Extensive evaluations demonstrate the
effectiveness of the proposed structured embeddings for single-label
classification, multi-label classification, and zero-shot recognition.