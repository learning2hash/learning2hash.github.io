---
layout: publication
title: Hierarchy-based Image Embeddings for Semantic Image Retrieval
authors: Barz Björn, Denzler Joachim
conference: ""
year: 2018
bibkey: barz2018hierarchy
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1809.09924"}
tags: ['Image Retrieval']
---
Deep neural networks trained for classification have been found to learn powerful image representations which are also often used for other tasks such as comparing images w.r.t. their visual similarity. However visual similarity does not imply semantic similarity. In order to learn semantically discriminative features we propose to map images onto class embeddings whose pair-wise dot products correspond to a measure of semantic similarity between classes. Such an embedding does not only improve image retrieval results but could also facilitate integrating semantics for other tasks e.g. novelty detection or few-shot learning. We introduce a deterministic algorithm for computing the class centroids directly based on prior world-knowledge encoded in a hierarchy of classes such as WordNet. Experiments on CIFAR-100 NABirds and ImageNet show that our learned semantic image embeddings improve the semantic consistency of image retrieval results by a large margin.
