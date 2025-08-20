---
layout: publication
title: A Prototypical Triplet Loss For Cover Detection
authors: Guillaume Doras, Geoffroy Peeters
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: doras2019a
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.09862'}]
tags: [Datasets, Distance Metric Learning, ICASSP]
short_authors: Guillaume Doras, Geoffroy Peeters
---
Automatic cover detection -- the task of finding in a audio dataset all
covers of a query track -- has long been a challenging theoretical problem in
MIR community. It also became a practical need for music composers societies
requiring to detect automatically if an audio excerpt embeds musical content
belonging to their catalog.
  In a recent work, we addressed this problem with a convolutional neural
network mapping each track's dominant melody to an embedding vector, and
trained to minimize cover pairs distance in the embeddings space, while
maximizing it for non-covers. We showed in particular that training this model
with enough works having five or more covers yields state-of-the-art results.
  This however does not reflect the realistic use case, where music catalogs
typically contain works with zero or at most one or two covers. We thus
introduce here a new test set incorporating these constraints, and propose two
contributions to improve our model's accuracy under these stricter conditions:
we replace dominant melody with multi-pitch representation as input data, and
describe a novel prototypical triplet loss designed to improve covers
clustering. We show that these changes improve results significantly for two
concrete use cases, large dataset lookup and live songs identification.