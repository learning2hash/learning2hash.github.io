---
layout: publication
title: Leveraging Semantic Cues From Foundation Vision Models For Enhanced Local Feature
  Correspondence
authors: "Felipe Cadar, Guilherme Potje, Renato Martins, C\xE9dric Demonceaux, Erickson\
  \ R. Nascimento"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: cadar2024leveraging
citations: 1
additional_links: [{name: Code, url: 'https://www.verlab.dcc.ufmg.br/descriptors/reasoning_accv24'},
  {name: Paper, url: 'https://arxiv.org/abs/2410.09533'}]
tags: ["Evaluation", "Similarity Search"]
short_authors: Cadar et al.
---
Visual correspondence is a crucial step in key computer vision tasks,
including camera localization, image registration, and structure from motion.
The most effective techniques for matching keypoints currently involve using
learned sparse or dense matchers, which need pairs of images. These neural
networks have a good general understanding of features from both images, but
they often struggle to match points from different semantic areas. This paper
presents a new method that uses semantic cues from foundation vision model
features (like DINOv2) to enhance local feature matching by incorporating
semantic reasoning into existing descriptors. Therefore, the learned
descriptors do not require image pairs at inference time, allowing feature
caching and fast matching using similarity search, unlike learned matchers. We
present adapted versions of six existing descriptors, with an average increase
in performance of 29% in camera localization, with comparable accuracy to
existing matchers as LightGlue and LoFTR in two existing benchmarks. Both code
and trained models are available at
https://www.verlab.dcc.ufmg.br/descriptors/reasoning_accv24