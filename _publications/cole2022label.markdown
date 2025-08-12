---
layout: publication
title: On Label Granularity And Object Localization
authors: Elijah Cole, Kimberly Wilber, Grant van Horn, Xuan Yang, Marco Fornoni, Pietro
  Perona, Serge Belongie, Andrew Howard, Oisin Mac Aodha
conference: Lecture Notes in Computer Science
year: 2022
bibkey: cole2022label
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.10225'}]
tags: []
short_authors: Cole et al.
---
Weakly supervised object localization (WSOL) aims to learn representations
that encode object location using only image-level category labels. However,
many objects can be labeled at different levels of granularity. Is it an
animal, a bird, or a great horned owl? Which image-level labels should we use?
In this paper we study the role of label granularity in WSOL. To facilitate
this investigation we introduce iNatLoc500, a new large-scale fine-grained
benchmark dataset for WSOL. Surprisingly, we find that choosing the right
training label granularity provides a much larger performance boost than
choosing the best WSOL algorithm. We also show that changing the label
granularity can significantly improve data efficiency.