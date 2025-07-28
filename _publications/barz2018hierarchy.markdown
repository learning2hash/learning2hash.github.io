---
layout: publication
title: Hierarchy-based Image Embeddings For Semantic Image Retrieval
authors: "Bj\xF6rn Barz, Joachim Denzler"
conference: 2019 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2019
bibkey: barz2018hierarchy
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.09924'}]
tags: ["Image Retrieval"]
short_authors: "Bj\xF6rn Barz, Joachim Denzler"
---
Deep neural networks trained for classification have been found to learn
powerful image representations, which are also often used for other tasks such
as comparing images w.r.t. their visual similarity. However, visual similarity
does not imply semantic similarity. In order to learn semantically
discriminative features, we propose to map images onto class embeddings whose
pair-wise dot products correspond to a measure of semantic similarity between
classes. Such an embedding does not only improve image retrieval results, but
could also facilitate integrating semantics for other tasks, e.g., novelty
detection or few-shot learning. We introduce a deterministic algorithm for
computing the class centroids directly based on prior world-knowledge encoded
in a hierarchy of classes such as WordNet. Experiments on CIFAR-100, NABirds,
and ImageNet show that our learned semantic image embeddings improve the
semantic consistency of image retrieval results by a large margin.