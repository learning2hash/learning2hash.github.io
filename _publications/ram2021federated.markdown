---
layout: publication
title: 'Federated Nearest Neighbor Classification With A Colony Of Fruit-flies: With
  Supplement'
authors: Ram Parikshit, Sinha Kaushik
conference: Arxiv
year: 2021
bibkey: ram2021federated
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.07157'}]
tags: ["Efficiency", "Similarity Search"]
short_authors: Ram Parikshit, Sinha Kaushik
---
The mathematical formalization of a neurological mechanism in the olfactory
circuit of a fruit-fly as a locality sensitive hash (Flyhash) and bloom filter
(FBF) has been recently proposed and "reprogrammed" for various machine
learning tasks such as similarity search, outlier detection and text
embeddings. We propose a novel reprogramming of this hash and bloom filter to
emulate the canonical nearest neighbor classifier (NNC) in the challenging
Federated Learning (FL) setup where training and test data are spread across
parties and no data can leave their respective parties. Specifically, we
utilize Flyhash and FBF to create the FlyNN classifier, and theoretically
establish conditions where FlyNN matches NNC. We show how FlyNN is trained
exactly in a FL setup with low communication overhead to produce FlyNNFL, and
how it can be differentially private. Empirically, we demonstrate that (i)
FlyNN matches NNC accuracy across 70 OpenML datasets, (ii) FlyNNFL training is
highly scalable with low communication overhead, providing up to \\(8\times\\)
speedup with \\(16\\) parties.