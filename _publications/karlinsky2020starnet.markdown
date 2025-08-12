---
layout: publication
title: 'Starnet: Towards Weakly Supervised Few-shot Object Detection'
authors: Leonid Karlinsky, Joseph Shtok, Amit Alfassy, Moshe Lichtenstein, Sivan Harary,
  Eli Schwartz, Sivan Doveh, Prasanna Sattigeri, Rogerio Feris, Alexander Bronstein,
  Raja Giryes
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: karlinsky2020starnet
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.06798'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Karlinsky et al.
---
Few-shot detection and classification have advanced significantly in recent
years. Yet, detection approaches require strong annotation (bounding boxes)
both for pre-training and for adaptation to novel classes, and classification
approaches rarely provide localization of objects in the scene. In this paper,
we introduce StarNet - a few-shot model featuring an end-to-end differentiable
non-parametric star-model detection and classification head. Through this head,
the backbone is meta-trained using only image-level labels to produce good
features for jointly localizing and classifying previously unseen categories of
few-shot test tasks using a star-model that geometrically matches between the
query and support images (to find corresponding object instances). Being a
few-shot detector, StarNet does not require any bounding box annotations,
neither during pre-training nor for novel classes adaptation. It can thus be
applied to the previously unexplored and challenging task of Weakly Supervised
Few-Shot Object Detection (WS-FSOD), where it attains significant improvements
over the baselines. In addition, StarNet shows significant gains on few-shot
classification benchmarks that are less cropped around the objects (where
object localization is key).