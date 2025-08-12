---
layout: publication
title: 'Transformatcher: Match-to-match Attention For Semantic Correspondence'
authors: Seungwook Kim, Juhong Min, Minsu Cho
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: kim2022transformatcher
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.11634'}]
tags: ["CVPR"]
short_authors: Seungwook Kim, Juhong Min, Minsu Cho
---
Establishing correspondences between images remains a challenging task,
especially under large appearance changes due to different viewpoints or
intra-class variations. In this work, we introduce a strong semantic image
matching learner, dubbed TransforMatcher, which builds on the success of
transformer networks in vision domains. Unlike existing convolution- or
attention-based schemes for correspondence, TransforMatcher performs global
match-to-match attention for precise match localization and dynamic refinement.
To handle a large number of matches in a dense correlation map, we develop a
light-weight attention architecture to consider the global match-to-match
interactions. We also propose to utilize a multi-channel correlation map for
refinement, treating the multi-level scores as features instead of a single
score to fully exploit the richer layer-wise semantics. In experiments,
TransforMatcher sets a new state of the art on SPair-71k while performing on
par with existing SOTA methods on the PF-PASCAL dataset.