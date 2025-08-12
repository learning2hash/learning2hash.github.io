---
layout: publication
title: Boosting Entity Linking Performance By Leveraging Unlabeled Documents
authors: Phong Le, Ivan Titov
conference: Proceedings of the 57th Annual Meeting of the Association for Computational
  Linguistics
year: 2019
bibkey: le2019boosting
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.01250'}]
tags: []
short_authors: Phong Le, Ivan Titov
---
Modern entity linking systems rely on large collections of documents
specifically annotated for the task (e.g., AIDA CoNLL). In contrast, we propose
an approach which exploits only naturally occurring information: unlabeled
documents and Wikipedia. Our approach consists of two stages. First, we
construct a high recall list of candidate entities for each mention in an
unlabeled document. Second, we use the candidate lists as weak supervision to
constrain our document-level entity linking model. The model treats entities as
latent variables and, when estimated on a collection of unlabelled texts,
learns to choose entities relying both on local context of each mention and on
coherence with other entities in the document. The resulting approach rivals
fully-supervised state-of-the-art systems on standard test sets. It also
approaches their performance in the very challenging setting: when tested on a
test set sampled from the data used to estimate the supervised systems. By
comparing to Wikipedia-only training of our model, we demonstrate that modeling
unlabeled documents is beneficial.