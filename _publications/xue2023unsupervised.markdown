---
layout: publication
title: Unsupervised Facial Expression Representation Learning With Contrastive Local
  Warping
authors: Fanglei Xue, Yifan Sun, Yi Yang
conference: Arxiv
year: 2023
bibkey: xue2023unsupervised
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09034'}]
tags: [Supervised, Image Retrieval, Self-Supervised, Tools & Libraries, Unsupervised]
short_authors: Fanglei Xue, Yifan Sun, Yi Yang
---
This paper investigates unsupervised representation learning for facial
expression analysis. We think Unsupervised Facial Expression Representation
(UFER) deserves exploration and has the potential to address some key
challenges in facial expression analysis, such as scaling, annotation bias, the
discrepancy between discrete labels and continuous emotions, and model
pre-training. Such motivated, we propose a UFER method with contrastive local
warping (ContraWarping), which leverages the insight that the emotional
expression is robust to current global transformation (affine transformation,
color jitter, etc.) but can be easily changed by random local warping.
Therefore, given a facial image, ContraWarping employs some global
transformations and local warping to generate its positive and negative samples
and sets up a novel contrastive learning framework. Our in-depth investigation
shows that: 1) the positive pairs from global transformations may be exploited
with general self-supervised learning (e.g., BYOL) and already bring some
informative features, and 2) the negative pairs from local warping explicitly
introduce expression-related variation and further bring substantial
improvement. Based on ContraWarping, we demonstrate the benefit of UFER under
two facial expression analysis scenarios: facial expression recognition and
image retrieval. For example, directly using ContraWarping features for linear
probing achieves 79.14% accuracy on RAF-DB, significantly reducing the gap
towards the full-supervised counterpart (88.92% / 84.81% with/without
pre-training).