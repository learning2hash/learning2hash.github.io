---
layout: publication
title: Semantically Tied Paired Cycle Consistency For Zero-shot Sketch-based Image
  Retrieval
authors: Anjan Dutta, Zeynep Akata
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: dutta2019semantically
citations: 159
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.03372'}]
tags: ["CVPR", "Datasets", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Anjan Dutta, Zeynep Akata
---
Zero-shot sketch-based image retrieval (SBIR) is an emerging task in computer
vision, allowing to retrieve natural images relevant to sketch queries that
might not been seen in the training phase. Existing works either require
aligned sketch-image pairs or inefficient memory fusion layer for mapping the
visual information to a semantic space. In this work, we propose a semantically
aligned paired cycle-consistent generative (SEM-PCYC) model for zero-shot SBIR,
where each branch maps the visual information to a common semantic space via an
adversarial training. Each of these branches maintains a cycle consistency that
only requires supervision at category levels, and avoids the need of
highly-priced aligned sketch-image pairs. A classification criteria on the
generators' outputs ensures the visual to semantic space mapping to be
discriminating. Furthermore, we propose to combine textual and hierarchical
side information via a feature selection auto-encoder that selects
discriminating side information within a same end-to-end model. Our results
demonstrate a significant boost in zero-shot SBIR performance over the
state-of-the-art on the challenging Sketchy and TU-Berlin datasets.