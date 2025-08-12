---
layout: publication
title: 'Contextualized Embeddings In Named-entity Recognition: An Empirical Study
  On Generalization'
authors: "Bruno Taill\xE9, Vincent Guigue, Patrick Gallinari"
conference: Lecture Notes in Computer Science
year: 2020
bibkey: "taill\xE92020contextualized"
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.08053'}]
tags: ["Datasets", "Evaluation"]
short_authors: "Bruno Taill\xE9, Vincent Guigue, Patrick Gallinari"
---
Contextualized embeddings use unsupervised language model pretraining to
compute word representations depending on their context. This is intuitively
useful for generalization, especially in Named-Entity Recognition where it is
crucial to detect mentions never seen during training. However, standard
English benchmarks overestimate the importance of lexical over contextual
features because of an unrealistic lexical overlap between train and test
mentions. In this paper, we perform an empirical analysis of the generalization
capabilities of state-of-the-art contextualized embeddings by separating
mentions by novelty and with out-of-domain evaluation. We show that they are
particularly beneficial for unseen mentions detection, especially
out-of-domain. For models trained on CoNLL03, language model contextualization
leads to a +1.2% maximal relative micro-F1 score increase in-domain against
+13% out-of-domain on the WNUT dataset