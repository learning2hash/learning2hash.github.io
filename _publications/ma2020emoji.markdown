---
layout: publication
title: 'Emoji Prediction: Extensions And Benchmarking'
authors: Weicheng Ma, Ruibo Liu, Lili Wang, Soroush Vosoughi
conference: Arxiv
year: 2020
bibkey: ma2020emoji
citations: 10
additional_links: [{name: Code, url: 'https://github.com/hikari-NYU/Emoji_Prediction_Datasets_MMS'},
  {name: Paper, url: 'https://arxiv.org/abs/2007.07389'}]
tags: ["Datasets"]
short_authors: Ma et al.
---
Emojis are a succinct form of language which can express concrete meanings,
emotions, and intentions. Emojis also carry signals that can be used to better
understand communicative intent. They have become a ubiquitous part of our
daily lives, making them an important part of understanding user-generated
content. The emoji prediction task aims at predicting the proper set of emojis
associated with a piece of text. Through emoji prediction, models can learn
rich representations of the communicative intent of the written text. While
existing research on the emoji prediction task focus on a small subset of emoji
types closely related to certain emotions, this setting oversimplifies the task
and wastes the expressive power of emojis. In this paper, we extend the
existing setting of the emoji prediction task to include a richer set of emojis
and to allow multi-label classification on the task. We propose novel models
for multi-class and multi-label emoji prediction based on Transformer networks.
We also construct multiple emoji prediction datasets from Twitter using
heuristics. The BERT models achieve state-of-the-art performances on all our
datasets under all the settings, with relative improvements of 27.21% to
236.36% in accuracy, 2.01% to 88.28% in top-5 accuracy and 65.19% to 346.79% in
F-1 score, compared to the prior state-of-the-art. Our results demonstrate the
efficacy of deep Transformer-based models on the emoji prediction task. We also
release our datasets at
https://github.com/hikari-NYU/Emoji_Prediction_Datasets_MMS for future
researchers.