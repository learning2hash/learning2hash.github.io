---
layout: publication
title: 'Sketch-a-classifier: Sketch-based Photo Classifier Generation'
authors: Conghui Hu, da Li, Yi-Zhe Song, Tao Xiang, Timothy M. Hospedales
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: hu2018sketch
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.11182'}]
tags: ["CVPR"]
short_authors: Hu et al.
---
Contemporary deep learning techniques have made image recognition a
reasonably reliable technology. However training effective photo classifiers
typically takes numerous examples which limits image recognition's scalability
and applicability to scenarios where images may not be available. This has
motivated investigation into zero-shot learning, which addresses the issue via
knowledge transfer from other modalities such as text. In this paper we
investigate an alternative approach of synthesizing image classifiers: almost
directly from a user's imagination, via free-hand sketch. This approach doesn't
require the category to be nameable or describable via attributes as per
zero-shot learning. We achieve this via training a \{model regression\} network
to map from \{free-hand sketch\} space to the space of photo classifiers. It
turns out that this mapping can be learned in a category-agnostic way, allowing
photo classifiers for new categories to be synthesized by user with no need for
annotated training photos. \{We also demonstrate that this modality of
classifier generation can also be used to enhance the granularity of an
existing photo classifier, or as a complement to name-based zero-shot learning.