---
layout: publication
title: 'People And Places Of Historical Europe: Bootstrapping Annotation Pipeline
  And A New Corpus Of Named Entities In Late Medieval Texts'
authors: "V\xEDt Novotn\xFD, Krist\xFDna Luger, Michal \u0160tef\xE1nik, Tereza Vrabcov\xE1\
  , Ale\u0161 Hor\xE1k"
conference: 'Findings of the Association for Computational Linguistics: ACL 2023'
year: 2023
bibkey: "novotn\xFD2023people"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.16718'}]
tags: ["Datasets", "Evaluation"]
short_authors: "Novotn\xFD et al."
---
Although pre-trained named entity recognition (NER) models are highly
accurate on modern corpora, they underperform on historical texts due to
differences in language OCR errors. In this work, we develop a new NER corpus
of 3.6M sentences from late medieval charters written mainly in Czech, Latin,
and German.
  We show that we can start with a list of known historical figures and
locations and an unannotated corpus of historical texts, and use information
retrieval techniques to automatically bootstrap a NER-annotated corpus. Using
our corpus, we train a NER model that achieves entity-level Precision of
72.81-93.98% with 58.14-81.77% Recall on a manually-annotated test dataset.
Furthermore, we show that using a weighted loss function helps to combat class
imbalance in token classification tasks. To make it easy for others to
reproduce and build upon our work, we publicly release our corpus, models, and
experimental code.