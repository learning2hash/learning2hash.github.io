---
layout: publication
title: Joint Person Objectness And Repulsion For Person Search
authors: Hantao Yao, Changsheng Xu
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: yao2020joint
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.00155'}]
tags: []
short_authors: Hantao Yao, Changsheng Xu
---
Person search targets to search the probe person from the unconstrainted
scene images, which can be treated as the combination of person detection and
person matching. However, the existing methods based on the Detection-Matching
framework ignore the person objectness and repulsion (OR) which are both
beneficial to reduce the effect of distractor images. In this paper, we propose
an OR similarity by jointly considering the objectness and repulsion
information. Besides the traditional visual similarity term, the OR similarity
also contains an objectness term and a repulsion term. The objectness term can
reduce the similarity of distractor images that not contain a person and boost
the performance of person search by improving the ranking of positive samples.
Because the probe person has a different person ID with its *neighbors*,
the gallery images having a higher similarity with the *neighbors of
probe* should have a lower similarity with the probe person. Based on this
repulsion constraint, the repulsion term is proposed to reduce the similarity
of distractor images that are not most similar to the probe person. Treating
the Faster R-CNN as the person detector, the OR similarity is evaluated on PRW
and CUHK-SYSU datasets by the Detection-Matching framework with six description
models. The extensive experiments demonstrate that the proposed OR similarity
can effectively reduce the similarity of distractor samples and further boost
the performance of person search, e.g., improve the mAP from 92.32% to 93.23%
for CUHK-SYSY dataset, and from 50.91% to 52.30% for PRW datasets.