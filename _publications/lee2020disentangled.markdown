---
layout: publication
title: Disentangled Multidimensional Metric Learning For Music Similarity
authors: Jongpil Lee, Nicholas J. Bryan, Justin Salamon, Zeyu Jin, Juhan Nam
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: lee2020disentangled
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.03720'}]
tags: [Distance Metric Learning, Similarity Search, ICASSP]
short_authors: Lee et al.
---
Music similarity search is useful for a variety of creative tasks such as
replacing one music recording with another recording with a similar "feel", a
common task in video editing. For this task, it is typically necessary to
define a similarity metric to compare one recording to another. Music
similarity, however, is hard to define and depends on multiple simultaneous
notions of similarity (i.e. genre, mood, instrument, tempo). While prior work
ignore this issue, we embrace this idea and introduce the concept of
multidimensional similarity and unify both global and specialized similarity
metrics into a single, semantically disentangled multidimensional similarity
metric. To do so, we adapt a variant of deep metric learning called conditional
similarity networks to the audio domain and extend it using track-based
information to control the specificity of our model. We evaluate our method and
show that our single, multidimensional model outperforms both specialized
similarity spaces and alternative baselines. We also run a user-study and show
that our approach is favored by human annotators as well.