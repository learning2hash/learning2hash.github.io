---
layout: publication
title: Progressive Domain-independent Feature Decomposition Network For Zero-shot
  Sketch-based Image Retrieval
authors: Xinxun Xu, Muli Yang, Yanhua Yang, Hao Wang
conference: Proceedings of the Twenty-Ninth International Joint Conference on Artificial
  Intelligence
year: 2020
bibkey: xu2020progressive
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.09869'}]
tags: [Image Retrieval, Few-shot & Zero-shot, AAAI, Similarity Search, Multimodal
    Retrieval, IJCAI]
short_authors: Xu et al.
---
Zero-shot sketch-based image retrieval (ZS-SBIR) is a specific cross-modal
retrieval task for searching natural images given free-hand sketches under the
zero-shot scenario. Most existing methods solve this problem by simultaneously
projecting visual features and semantic supervision into a low-dimensional
common space for efficient retrieval. However, such low-dimensional projection
destroys the completeness of semantic knowledge in original semantic space, so
that it is unable to transfer useful knowledge well when learning semantic from
different modalities. Moreover, the domain information and semantic information
are entangled in visual features, which is not conducive for cross-modal
matching since it will hinder the reduction of domain gap between sketch and
image. In this paper, we propose a Progressive Domain-independent Feature
Decomposition (PDFD) network for ZS-SBIR. Specifically, with the supervision of
original semantic knowledge, PDFD decomposes visual features into domain
features and semantic ones, and then the semantic features are projected into
common space as retrieval features for ZS-SBIR. The progressive projection
strategy maintains strong semantic supervision. Besides, to guarantee the
retrieval features to capture clean and complete semantic information, the
cross-reconstruction loss is introduced to encourage that any combinations of
retrieval features and domain features can reconstruct the visual features.
Extensive experiments demonstrate the superiority of our PDFD over
state-of-the-art competitors.