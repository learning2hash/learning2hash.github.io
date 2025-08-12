---
layout: publication
title: 'Line As A Visual Sentence: Context-aware Line Descriptor For Visual Localization'
authors: Sungho Yoon, Ayoung Kim
conference: IEEE Robotics and Automation Letters
year: 2021
bibkey: yoon2021line
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.04753'}]
tags: ["ICRA"]
short_authors: Sungho Yoon, Ayoung Kim
---
Along with feature points for image matching, line features provide
additional constraints to solve visual geometric problems in robotics and
computer vision (CV). Although recent convolutional neural network (CNN)-based
line descriptors are promising for viewpoint changes or dynamic environments,
we claim that the CNN architecture has innate disadvantages to abstract
variable line length into the fixed-dimensional descriptor. In this paper, we
effectively introduce Line-Transformers dealing with variable lines. Inspired
by natural language processing (NLP) tasks where sentences can be understood
and abstracted well in neural nets, we view a line segment as a sentence that
contains points (words). By attending to well-describable points on aline
dynamically, our descriptor performs excellently on variable line length. We
also propose line signature networks sharing the line's geometric attributes to
neighborhoods. Performing as group descriptors, the networks enhance line
descriptors by understanding lines' relative geometries. Finally, we present
the proposed line descriptor and matching in a Point and Line Localization
(PL-Loc). We show that the visual localization with feature points can be
improved using our line features. We validate the proposed method for
homography estimation and visual localization.