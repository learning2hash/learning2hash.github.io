---
layout: publication
title: Regressing Transformers For Data-efficient Visual Place Recognition
authors: "Mar\xEDa Leyva-vallina, Nicola Strisciuglio, Nicolai Petkov"
conference: Arxiv
year: 2024
bibkey: leyvavallina2024regressing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.16304'}]
tags: []
short_authors: "Mar\xEDa Leyva-vallina, Nicola Strisciuglio, Nicolai Petkov"
---
Visual place recognition is a critical task in computer vision, especially
for localization and navigation systems. Existing methods often rely on
contrastive learning: image descriptors are trained to have small distance for
similar images and larger distance for dissimilar ones in a latent space.
However, this approach struggles to ensure accurate distance-based image
similarity representation, particularly when training with binary pairwise
labels, and complex re-ranking strategies are required. This work introduces a
fresh perspective by framing place recognition as a regression problem, using
camera field-of-view overlap as similarity ground truth for learning. By
optimizing image descriptors to align directly with graded similarity labels,
this approach enhances ranking capabilities without expensive re-ranking,
offering data-efficient training and strong generalization across several
benchmark datasets.