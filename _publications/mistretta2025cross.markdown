---
layout: publication
title: 'Cross The Gap: Exposing The Intra-modal Misalignment In CLIP Via Modality
  Inversion'
authors: Marco Mistretta, Alberto Baldrati, Lorenzo Agnolucci, Marco Bertini, Andrew
  D. Bagdanov
conference: Arxiv
year: 2025
bibkey: mistretta2025cross
citations: 0
additional_links: [{name: Code, url: 'https://github.com/miccunifi/Cross-the-Gap'},
  {name: Paper, url: 'https://arxiv.org/abs/2502.04263'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Distance Metric Learning,
  Datasets, Text Retrieval]
short_authors: Mistretta et al.
---
Pre-trained multi-modal Vision-Language Models like CLIP are widely used
off-the-shelf for a variety of applications. In this paper, we show that the
common practice of individually exploiting the text or image encoders of these
powerful multi-modal models is highly suboptimal for intra-modal tasks like
image-to-image retrieval. We argue that this is inherently due to the
CLIP-style inter-modal contrastive loss that does not enforce any intra-modal
constraints, leading to what we call intra-modal misalignment. To demonstrate
this, we leverage two optimization-based modality inversion techniques that map
representations from their input modality to the complementary one without any
need for auxiliary data or additional trained adapters. We empirically show
that, in the intra-modal tasks of image-to-image and text-to-text retrieval,
approaching these tasks inter-modally significantly improves performance with
respect to intra-modal baselines on more than fifteen datasets. Additionally,
we demonstrate that approaching a native inter-modal task (e.g. zero-shot image
classification) intra-modally decreases performance, further validating our
findings. Finally, we show that incorporating an intra-modal term in the
pre-training objective or narrowing the modality gap between the text and image
feature embedding spaces helps reduce the intra-modal misalignment. The code is
publicly available at: https://github.com/miccunifi/Cross-the-Gap.