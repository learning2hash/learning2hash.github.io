---
layout: publication
title: Self-localization From Images With Small Overlap
authors: Tanaka Kanji
conference: 2016 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2016
bibkey: kanji2016self
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.00993'}]
tags: ["Distance Metric Learning", "Evaluation", "IROS", "Tools & Libraries"]
short_authors: Tanaka Kanji
---
With the recent success of visual features from deep convolutional neural
networks (DCNN) in visual robot self-localization, it has become important and
practical to address more general self-localization scenarios. In this paper,
we address the scenario of self-localization from images with small overlap. We
explicitly introduce a localization difficulty index as a decreasing function
of view overlap between query and relevant database images and investigate
performance versus difficulty for challenging cross-view self-localization
tasks. We then reformulate the self-localization as a scalable
bag-of-visual-features (BoVF) scene retrieval and present an efficient solution
called PCA-NBNN, aiming to facilitate fast and yet discriminative
correspondence between partially overlapping images. The proposed approach
adopts recent findings in discriminativity preserving encoding of DCNN features
using principal component analysis (PCA) and cross-domain scene matching using
naive Bayes nearest neighbor distance metric (NBNN). We experimentally
demonstrate that the proposed PCA-NBNN framework frequently achieves comparable
results to previous DCNN features and that the BoVF model is significantly more
efficient. We further address an important alternative scenario of
"self-localization from images with NO overlap" and report the result.