---
layout: publication
title: Chunk-based Nearest Neighbor Machine Translation
authors: "Pedro Henrique Martins, Zita Marinho, Andr\xE9 F. T. Martins"
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: martins2022chunk
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.12230'}]
tags: ["EMNLP"]
short_authors: "Pedro Henrique Martins, Zita Marinho, Andr\xE9 F. T. Martins"
---
Semi-parametric models, which augment generation with retrieval, have led to
impressive results in language modeling and machine translation, due to their
ability to retrieve fine-grained information from a datastore of examples. One
of the most prominent approaches, \(k\)NN-MT, exhibits strong domain adaptation
capabilities by retrieving tokens from domain-specific datastores
\citep\{khandelwal2020nearest\}. However, \(k\)NN-MT requires an expensive
retrieval operation for every single generated token, leading to a very low
decoding speed (around 8 times slower than a parametric model). In this paper,
we introduce a \textit\{chunk-based\} \(k\)NN-MT model which retrieves chunks of
tokens from the datastore, instead of a single token. We propose several
strategies for incorporating the retrieved chunks into the generation process,
and for selecting the steps at which the model needs to search for neighbors in
the datastore. Experiments on machine translation in two settings, static and
``on-the-fly'' domain adaptation, show that the chunk-based \(k\)NN-MT model
leads to significant speed-ups (up to 4 times) with only a small drop in
translation quality.