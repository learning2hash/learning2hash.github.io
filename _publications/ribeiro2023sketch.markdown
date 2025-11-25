---
layout: publication
title: 'Sketch-an-anchor: Sub-epoch Fast Model Adaptation For Zero-shot Sketch-based
  Image Retrieval'
authors: Leo Sampaio Ferraz Ribeiro, Moacir Antonelli Ponti
conference: Arxiv
year: 2023
bibkey: ribeiro2023sketch
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.16769'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Leo Sampaio Ferraz Ribeiro, Moacir Antonelli Ponti
---
Sketch-an-Anchor is a novel method to train state-of-the-art Zero-shot
Sketch-based Image Retrieval (ZSSBIR) models in under an epoch. Most studies
break down the problem of ZSSBIR into two parts: domain alignment between
images and sketches, inherited from SBIR, and generalization to unseen data,
inherent to the zero-shot protocol. We argue one of these problems can be
considerably simplified and re-frame the ZSSBIR problem around the
already-stellar yet underexplored Zero-shot Image-based Retrieval performance
of off-the-shelf models. Our fast-converging model keeps the single-domain
performance while learning to extract similar representations from sketches. To
this end we introduce our Semantic Anchors -- guiding embeddings learned from
word-based semantic spaces and features from off-the-shelf models -- and
combine them with our novel Anchored Contrastive Loss. Empirical evidence shows
we can achieve state-of-the-art performance on all benchmark datasets while
training for 100x less iterations than other methods.