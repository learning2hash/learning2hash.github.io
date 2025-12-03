---
layout: publication
title: Weakly Supervised Cross-modal Learning In High-content Screening
authors: Watkinson Gabriel, Cohen Ethan, Bourriez Nicolas, Bendidi Ihab, Bollot Guillaume,
  Genovesio Auguste
conference: Arxiv
year: 2023
bibkey: gabriel2023weakly
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.04678'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Supervised"]
short_authors: Gabriel et al.
---
With the surge in available data from various modalities, there is a growing
need to bridge the gap between different data types. In this work, we introduce
a novel approach to learn cross-modal representations between image data and
molecular representations for drug discovery. We propose EMM and IMM, two
innovative loss functions built on top of CLIP that leverage weak supervision
and cross sites replicates in High-Content Screening. Evaluating our model
against known baseline on cross-modal retrieval, we show that our proposed
approach allows to learn better representations and mitigate batch effect. In
addition, we also present a preprocessing method for the JUMP-CP dataset that
effectively reduce the required space from 85Tb to a mere usable 7Tb size,
still retaining all perturbations and most of the information content.