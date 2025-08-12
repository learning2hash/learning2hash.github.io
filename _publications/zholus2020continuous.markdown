---
layout: publication
title: 'Continuous Histogram Loss: Beyond Neural Similarity'
authors: Artem Zholus, Evgeny Putin
conference: Arxiv
year: 2020
bibkey: zholus2020continuous
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.02830'}]
tags: []
short_authors: Artem Zholus, Evgeny Putin
---
Similarity learning has gained a lot of attention from researches in recent
years and tons of successful approaches have been recently proposed. However,
the majority of the state-of-the-art similarity learning methods consider only
a binary similarity. In this paper we introduce a new loss function called
Continuous Histogram Loss (CHL) which generalizes recently proposed Histogram
loss to multiple-valued similarities, i.e. allowing the acceptable values of
similarity to be continuously distributed within some range. The novel loss
function is computed by aggregating pairwise distances and similarities into 2D
histograms in a differentiable manner and then computing the probability of
condition that pairwise distances will not decrease as the similarities
increase. The novel loss is capable of solving a wider range of tasks including
similarity learning, representation learning and data visualization.