---
layout: publication
title: 'QPIC: Query-based Pairwise Human-object Interaction Detection With Image-wide
  Contextual Information'
authors: Masato Tamura, Hiroki Ohashi, Tomoaki Yoshinaga
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: tamura2021qpic
citations: 166
additional_links: [{name: Code, url: 'https://github.com/hitachi-rd-cv/qpic\}\{\{this'},
  {name: Paper, url: 'https://arxiv.org/abs/2103.05399'}]
tags: ["CVPR"]
short_authors: Masato Tamura, Hiroki Ohashi, Tomoaki Yoshinaga
---
We propose a simple, intuitive yet powerful method for human-object
interaction (HOI) detection. HOIs are so diverse in spatial distribution in an
image that existing CNN-based methods face the following three major drawbacks;
they cannot leverage image-wide features due to CNN's locality, they rely on a
manually defined location-of-interest for the feature aggregation, which
sometimes does not cover contextually important regions, and they cannot help
but mix up the features for multiple HOI instances if they are located closely.
To overcome these drawbacks, we propose a transformer-based feature extractor,
in which an attention mechanism and query-based detection play key roles. The
attention mechanism is effective in aggregating contextually important
information image-wide, while the queries, which we design in such a way that
each query captures at most one human-object pair, can avoid mixing up the
features from multiple instances. This transformer-based feature extractor
produces so effective embeddings that the subsequent detection heads may be
fairly simple and intuitive. The extensive analysis reveals that the proposed
method successfully extracts contextually important features, and thus
outperforms existing methods by large margins (5.37 mAP on HICO-DET, and 5.7
mAP on V-COCO). The source codes are available at
\(\href\{https://github.com/hitachi-rd-cv/qpic\}\{\text\{this https URL\}\}\).