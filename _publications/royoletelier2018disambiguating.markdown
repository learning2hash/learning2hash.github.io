---
layout: publication
title: Disambiguating Music Artists at Scale with Audio Metric Learning
authors: Royo-letelier et al.
conference: Arxiv
year: 2018
bibkey: royoletelier2018disambiguating
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.01807'}]
tags: ["Distance Metric Learning"]
---
We address the problem of disambiguating large scale catalogs through the
definition of an unknown artist clustering task. We explore the use of metric
learning techniques to learn artist embeddings directly from audio, and using a
dedicated homonym artists dataset, we compare our method with a recent approach
that learn similar embeddings using artist classifiers. While both systems have
the ability to disambiguate unknown artists relying exclusively on audio, we
show that our system is more suitable in the case when enough audio data is
available for each artist in the train dataset. We also propose a new negative
sampling method for metric learning that takes advantage of side information
such as music genre during the learning phase and shows promising results for
the artist clustering task.