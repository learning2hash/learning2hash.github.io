---
layout: publication
title: 'Clustering Comparable Corpora Of Russian And Ukrainian Academic Texts: Word
  Embeddings And Semantic Fingerprints'
authors: Andrey Kutuzov, Mikhail Kopotev, Tatyana Sviridenko, Lyubov Ivanova
conference: Arxiv
year: 2016
bibkey: kutuzov2016clustering
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.05372'}]
tags: ["Datasets", "Unsupervised"]
short_authors: Kutuzov et al.
---
We present our experience in applying distributional semantics (neural word
embeddings) to the problem of representing and clustering documents in a
bilingual comparable corpus. Our data is a collection of Russian and Ukrainian
academic texts, for which topics are their academic fields. In order to build
language-independent semantic representations of these documents, we train
neural distributional models on monolingual corpora and learn the optimal
linear transformation of vectors from one language to another. The resulting
vectors are then used to produce `semantic fingerprints' of documents, serving
as input to a clustering algorithm.
  The presented method is compared to several baselines including `orthographic
translation' with Levenshtein edit distance and outperforms them by a large
margin. We also show that language-independent `semantic fingerprints' are
superior to multi-lingual clustering algorithms proposed in the previous work,
at the same time requiring less linguistic resources.