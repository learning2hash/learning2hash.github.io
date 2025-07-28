---
layout: publication
title: Expressivity-aware Music Performance Retrieval Using Mid-level Perceptual Features
  And Emotion Word Embeddings
authors: Shreyan Chowdhury, Gerhard Widmer
conference: Arxiv
year: 2024
bibkey: chowdhury2024expressivity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.14826'}]
tags: ["Evaluation", "Recommender Systems"]
short_authors: Shreyan Chowdhury, Gerhard Widmer
---
This paper explores a specific sub-task of cross-modal music retrieval. We
consider the delicate task of retrieving a performance or rendition of a
musical piece based on a description of its style, expressive character, or
emotion from a set of different performances of the same piece. We observe that
a general purpose cross-modal system trained to learn a common text-audio
embedding space does not yield optimal results for this task. By introducing
two changes -- one each to the text encoder and the audio encoder -- we
demonstrate improved performance on a dataset of piano performances and
associated free-text descriptions. On the text side, we use emotion-enriched
word embeddings (EWE) and on the audio side, we extract mid-level perceptual
features instead of generic audio embeddings. Our results highlight the
effectiveness of mid-level perceptual features learnt from music and emotion
enriched word embeddings learnt from emotion-labelled text in capturing musical
expression in a cross-modal setting. Additionally, our interpretable mid-level
features provide a route for introducing explainability in the retrieval and
downstream recommendation processes.