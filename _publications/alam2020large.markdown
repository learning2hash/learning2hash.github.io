---
layout: publication
title: A Large Multi-target Dataset Of Common Bengali Handwritten Graphemes
authors: Samiul Alam, Tahsin Reasat, Asif Shahriyar Sushmit, Sadi Mohammad Siddiquee,
  Fuad Rahman, Mahady Hasan, Ahmed Imtiaz Humayun
conference: Lecture Notes in Computer Science
year: 2021
bibkey: alam2020large
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.00170'}]
tags: ["Datasets"]
short_authors: Alam et al.
---
Latin has historically led the state-of-the-art in handwritten optical
character recognition (OCR) research. Adapting existing systems from Latin to
alpha-syllabary languages is particularly challenging due to a sharp contrast
between their orthographies. The segmentation of graphical constituents
corresponding to characters becomes significantly hard due to a cursive writing
system and frequent use of diacritics in the alpha-syllabary family of
languages. We propose a labeling scheme based on graphemes (linguistic segments
of word formation) that makes segmentation in-side alpha-syllabary words linear
and present the first dataset of Bengali handwritten graphemes that are
commonly used in an everyday context. The dataset contains 411k curated samples
of 1295 unique commonly used Bengali graphemes. Additionally, the test set
contains 900 uncommon Bengali graphemes for out of dictionary performance
evaluation. The dataset is open-sourced as a part of a public Handwritten
Grapheme Classification Challenge on Kaggle to benchmark vision algorithms for
multi-target grapheme classification. The unique graphemes present in this
dataset are selected based on commonality in the Google Bengali ASR corpus.
From competition proceedings, we see that deep-learning methods can generalize
to a large span of out of dictionary graphemes which are absent during
training. Dataset and starter codes at www.kaggle.com/c/bengaliai-cv19.