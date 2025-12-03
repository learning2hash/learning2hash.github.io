---
layout: publication
title: Learning Visual Composition Through Improved Semantic Guidance
authors: Austin Stone, Hagen Soltau, Robert Geirhos, Xi Yi, Ye Xia, Bingyi Cao, Kaifeng
  Chen, Abhijit Ogale, Jonathon Shlens
conference: Arxiv
year: 2024
bibkey: stone2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.15396'}]
tags: ["Evaluation", "Image Retrieval", "Self-Supervised"]
short_authors: Stone et al.
---
Visual imagery does not consist of solitary objects, but instead reflects the
composition of a multitude of fluid concepts. While there have been great
advances in visual representation learning, such advances have focused on
building better representations for a small number of discrete objects bereft
of an understanding of how these objects are interacting. One can observe this
limitation in representations learned through captions or contrastive learning
-- where the learned model treats an image essentially as a bag of words.
Several works have attempted to address this limitation through the development
of bespoke learned architectures to directly address the shortcomings in
compositional learning. In this work, we focus on simple, and scalable
approaches. In particular, we demonstrate that by substantially improving
weakly labeled data, i.e. captions, we can vastly improve the performance of
standard contrastive learning approaches. Previous CLIP models achieved near
chance rate on challenging tasks probing compositional learning. However, our
simple approach boosts performance of CLIP substantially and surpasses all
bespoke architectures. Furthermore, we showcase our results on a relatively new
captioning benchmark derived from DOCCI. We demonstrate through a series of
ablations that a standard CLIP model trained with enhanced data may demonstrate
impressive performance on image retrieval tasks.