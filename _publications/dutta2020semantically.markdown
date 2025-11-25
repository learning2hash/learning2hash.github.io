---
layout: publication
title: Semantically Tied Paired Cycle Consistency For Any-shot Sketch-based Image
  Retrieval
authors: Anjan Dutta, Zeynep Akata
conference: International Journal of Computer Vision
year: 2020
bibkey: dutta2020semantically
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11397'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Anjan Dutta, Zeynep Akata
---
Low-shot sketch-based image retrieval is an emerging task in computer vision,
allowing to retrieve natural images relevant to hand-drawn sketch queries that
are rarely seen during the training phase. Related prior works either require
aligned sketch-image pairs that are costly to obtain or inefficient memory
fusion layer for mapping the visual information to a semantic space. In this
paper, we address any-shot, i.e. zero-shot and few-shot, sketch-based image
retrieval (SBIR) tasks, where we introduce the few-shot setting for SBIR. For
solving these tasks, we propose a semantically aligned paired cycle-consistent
generative adversarial network (SEM-PCYC) for any-shot SBIR, where each branch
of the generative adversarial network maps the visual information from sketch
and image to a common semantic space via adversarial training. Each of these
branches maintains cycle consistency that only requires supervision at the
category level, and avoids the need of aligned sketch-image pairs. A
classification criteria on the generators' outputs ensures the visual to
semantic space mapping to be class-specific. Furthermore, we propose to combine
textual and hierarchical side information via an auto-encoder that selects
discriminating side information within a same end-to-end model. Our results
demonstrate a significant boost in any-shot SBIR performance over the
state-of-the-art on the extended version of the challenging Sketchy, TU-Berlin
and QuickDraw datasets.