---
layout: publication
title: Cross-lingual Emotion Intensity Prediction
authors: Irean Navas Alejo, Toni Badia, Jeremy Barnes
conference: Arxiv
year: 2020
bibkey: alejo2020cross
citations: 4
additional_links: [{name: Code, url: 'https://github.com/jerbarnes/fine-grained_cross-lingual_emotion'},
  {name: Paper, url: 'https://arxiv.org/abs/2004.04103'}]
tags: []
short_authors: Irean Navas Alejo, Toni Badia, Jeremy Barnes
---
Emotion intensity prediction determines the degree or intensity of an emotion
that the author expresses in a text, extending previous categorical approaches
to emotion detection. While most previous work on this topic has concentrated
on English texts, other languages would also benefit from fine-grained emotion
classification, preferably without having to recreate the amount of annotated
data available in English in each new language. Consequently, we explore
cross-lingual transfer approaches for fine-grained emotion detection in Spanish
and Catalan tweets. To this end we annotate a test set of Spanish and Catalan
tweets using Best-Worst scaling. We compare six cross-lingual approaches, e.g.,
machine translation and cross-lingual embeddings, which have varying
requirements for parallel data -- from millions of parallel sentences to
completely unsupervised. The results show that on this data, methods with low
parallel-data requirements perform surprisingly better than methods that use
more parallel data, which we explain through an in-depth error analysis. We
make the dataset and the code available at
https://github.com/jerbarnes/fine-grained_cross-lingual_emotion