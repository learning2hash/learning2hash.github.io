---
layout: publication
title: 'Shallowblocker: Improving Set Similarity Joins For Blocking'
authors: Nils Barlaug
conference: Arxiv
year: 2023
bibkey: barlaug2023shallowblocker
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.15835'}]
tags: []
short_authors: Nils Barlaug
---
Blocking is a crucial step in large-scale entity matching but often requires
significant manual engineering from an expert for each new dataset. Recent work
has show that deep learning is state-of-the-art and has great potential for
achieving hands-off and accurate blocking compared to classical methods.
However, in practice, such deep learning methods are often unstable, offers
little interpretability, and require hyperparameter tuning and significant
computational resources.
  In this paper, we propose a hands-off blocking method based on classical
string similarity measures: ShallowBlocker. It uses a novel hybrid set
similarity join combining absolute similarity, relative similarity, and local
cardinality conditions with a new effective pre-candidate filter replacing size
filter. We show that the method achieves state-of-the-art pair effectiveness on
both unsupervised and supervised blocking in a scalable way.