---
layout: publication
title: 'Social Fabric: Tubelet Compositions For Video Relation Detection'
authors: Shuo Chen, Zenglin Shi, Pascal Mettes, Cees G. M. Snoek
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: chen2021social
citations: 17
additional_links: [{name: Code, url: 'https://github.com/shanshuo/Social-Fabric'},
  {name: Paper, url: 'https://arxiv.org/abs/2108.08363'}]
tags: ["ICCV"]
short_authors: Chen et al.
---
This paper strives to classify and detect the relationship between object
tubelets appearing within a video as a <subject-predicate-object> triplet.
Where existing works treat object proposals or tubelets as single entities and
model their relations a posteriori, we propose to classify and detect
predicates for pairs of object tubelets a priori. We also propose Social
Fabric: an encoding that represents a pair of object tubelets as a composition
of interaction primitives. These primitives are learned over all relations,
resulting in a compact representation able to localize and classify relations
from the pool of co-occurring object tubelets across all timespans in a video.
The encoding enables our two-stage network. In the first stage, we train Social
Fabric to suggest proposals that are likely interacting. We use the Social
Fabric in the second stage to simultaneously fine-tune and predict predicate
labels for the tubelets. Experiments demonstrate the benefit of early video
relation modeling, our encoding and the two-stage architecture, leading to a
new state-of-the-art on two benchmarks. We also show how the encoding enables
query-by-primitive-example to search for spatio-temporal video relations. Code:
https://github.com/shanshuo/Social-Fabric.