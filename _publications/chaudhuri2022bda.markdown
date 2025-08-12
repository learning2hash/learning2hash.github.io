---
layout: publication
title: 'Bda-sketret: Bi-level Domain Adaptation For Zero-shot SBIR'
authors: Ushasi Chaudhuri, Ruchika Chavan, Biplab Banerjee, Anjan Dutta, Zeynep Akata
conference: Neurocomputing
year: 2022
bibkey: chaudhuri2022bda
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.06570'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Chaudhuri et al.
---
The efficacy of zero-shot sketch-based image retrieval (ZS-SBIR) models is
governed by two challenges. The immense distributions-gap between the sketches
and the images requires a proper domain alignment. Moreover, the fine-grained
nature of the task and the high intra-class variance of many categories
necessitates a class-wise discriminative mapping among the sketch, image, and
the semantic spaces. Under this premise, we propose BDA-SketRet, a novel
ZS-SBIR framework performing a bi-level domain adaptation for aligning the
spatial and semantic features of the visual data pairs progressively. In order
to highlight the shared features and reduce the effects of any sketch or
image-specific artifacts, we propose a novel symmetric loss function based on
the notion of information bottleneck for aligning the semantic features while a
cross-entropy-based adversarial loss is introduced to align the spatial feature
maps. Finally, our CNN-based model confirms the discriminativeness of the
shared latent space through a novel topology-preserving semantic projection
network. Experimental results on the extended Sketchy, TU-Berlin, and QuickDraw
datasets exhibit sharp improvements over the literature.