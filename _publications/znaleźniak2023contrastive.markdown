---
layout: publication
title: Contrastive Hierarchical Clustering
authors: "Micha\u0142 Znale\u017Aniak, Przemys\u0142aw Rola, Patryk Kaszuba, Jacek\
  \ Tabor, Marek \u015Amieja"
conference: Lecture Notes in Computer Science
year: 2023
bibkey: "znale\u017Aniak2023contrastive"
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.03389'}]
tags: []
short_authors: "Znale\u017Aniak et al."
---
Deep clustering has been dominated by flat models, which split a dataset into
a predefined number of groups. Although recent methods achieve an extremely
high similarity with the ground truth on popular benchmarks, the information
contained in the flat partition is limited. In this paper, we introduce
CoHiClust, a Contrastive Hierarchical Clustering model based on deep neural
networks, which can be applied to typical image data. By employing a
self-supervised learning approach, CoHiClust distills the base network into a
binary tree without access to any labeled data. The hierarchical clustering
structure can be used to analyze the relationship between clusters, as well as
to measure the similarity between data points. Experiments demonstrate that
CoHiClust generates a reasonable structure of clusters, which is consistent
with our intuition and image semantics. Moreover, it obtains superior
clustering accuracy on most of the image datasets compared to the
state-of-the-art flat clustering models.