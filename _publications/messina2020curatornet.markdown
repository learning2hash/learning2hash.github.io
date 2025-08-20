---
layout: publication
title: 'Curatornet: Visually-aware Recommendation Of Art Images'
authors: Pablo Messina, Manuel Cartagena, Patricio Cerda-Mardini, Felipe del Rio,
  Denis Parra
conference: Arxiv
year: 2020
bibkey: messina2020curatornet
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.04426'}]
tags: [Recommender Systems, Evaluation, Datasets]
short_authors: Messina et al.
---
Although there are several visually-aware recommendation models in domains
like fashion or even movies, the art domain lacks thesame level of research
attention, despite the recent growth of the online artwork market. To reduce
this gap, in this article we introduceCuratorNet, a neural network architecture
for visually-aware recommendation of art images. CuratorNet is designed at the
core withthe goal of maximizing generalization: the network has a fixed set of
parameters that only need to be trained once, and thereafter themodel is able
to generalize to new users or items never seen before, without further
training. This is achieved by leveraging visualcontent: items are mapped to
item vectors through visual embeddings, and users are mapped to user vectors by
aggregating the visualcontent of items they have consumed. Besides the model
architecture, we also introduce novel triplet sampling strategies to build
atraining set for rank learning in the art domain, resulting in more effective
learning than naive random sampling. With an evaluationover a real-world
dataset of physical paintings, we show that CuratorNet achieves the best
performance among several baselines,including the state-of-the-art model VBPR.
CuratorNet is motivated and evaluated in the art domain, but its architecture
and trainingscheme could be adapted to recommend images in other areas