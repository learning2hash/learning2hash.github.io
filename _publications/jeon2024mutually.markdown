---
layout: publication
title: Mutually-aware Feature Learning For Few-shot Object Counting
authors: Yerim Jeon, Subeen Lee, Jihwan Kim, Jae-Pil Heo
conference: Pattern Recognition
year: 2024
bibkey: jeon2024mutually
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.09734'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jeon et al.
---
Few-shot object counting has garnered significant attention for its
practicality as it aims to count target objects in a query image based on given
exemplars without the need for additional training. However, there is a
shortcoming in the prevailing extract-and-match approach: query and exemplar
features lack interaction during feature extraction since they are extracted
unaware of each other and later correlated based on similarity. This can lead
to insufficient target awareness of the extracted features, resulting in target
confusion in precisely identifying the actual target when multiple class
objects coexist. To address this limitation, we propose a novel framework,
Mutually-Aware FEAture learning(MAFEA), which encodes query and exemplar
features mutually aware of each other from the outset. By encouraging
interaction between query and exemplar features throughout the entire pipeline,
we can obtain target-aware features that are robust to a multi-category
scenario. Furthermore, we introduce a background token to effectively associate
the target region of query with exemplars and decouple its background region
from them. Our extensive experiments demonstrate that our model reaches a new
state-of-the-art performance on the two challenging benchmarks, FSCD-LVIS and
FSC-147, with a remarkably reduced degree of the target confusion problem.