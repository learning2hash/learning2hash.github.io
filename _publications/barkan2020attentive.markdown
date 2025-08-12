---
layout: publication
title: 'Attentive Item2vec: Neural Attentive User Representations'
authors: Oren Barkan, Avi Caciularu, Ori Katz, Noam Koenigstein
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: barkan2020attentive
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06205'}]
tags: ["ICASSP", "Recommender Systems"]
short_authors: Barkan et al.
---
Factorization methods for recommender systems tend to represent users as a
single latent vector. However, user behavior and interests may change in the
context of the recommendations that are presented to the user. For example, in
the case of movie recommendations, it is usually true that earlier user data is
less informative than more recent data. However, it is possible that a certain
early movie may become suddenly more relevant in the presence of a popular
sequel movie. This is just a single example of a variety of possible
dynamically altering user interests in the presence of a potential new
recommendation. In this work, we present Attentive Item2vec (AI2V) - a novel
attentive version of Item2vec (I2V). AI2V employs a context-target attention
mechanism in order to learn and capture different characteristics of user
historical behavior (context) with respect to a potential recommended item
(target). The attentive context-target mechanism enables a final neural
attentive user representation. We demonstrate the effectiveness of AI2V on
several datasets, where it is shown to outperform other baselines.