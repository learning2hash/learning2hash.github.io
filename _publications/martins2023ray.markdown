---
layout: publication
title: 'Ray-patch: An Efficient Querying For Light Field Transformers'
authors: T. Berriel Martins, Javier Civera
conference: Arxiv
year: 2023
bibkey: martins2023ray
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.09566'}]
tags: []
short_authors: T. Berriel Martins, Javier Civera
---
In this paper we propose the Ray-Patch querying, a novel model to efficiently
query transformers to decode implicit representations into target views. Our
Ray-Patch decoding reduces the computational footprint and increases inference
speed up to one order of magnitude compared to previous models, without losing
global attention, and hence maintaining specific task metrics. The key idea of
our novel querying is to split the target image into a set of patches, then
querying the transformer for each patch to extract a set of feature vectors,
which are finally decoded into the target image using convolutional layers. Our
experimental results, implementing Ray-Patch in 3 different architectures and
evaluating it in 2 different tasks and datasets, demonstrate and quantify the
effectiveness of our method, specifically a notable boost in rendering speed
for the same task metrics.