---
layout: publication
title: On The Effectiveness Of Convolutional Autoencoders On Image-based Personalized
  Recommender Systems
authors: "E. Blanco-Mallo, B. Remeseiro, V. Bol\xF3n-Canedo, A. Alonso-Betanzos"
conference: 3rd XoveTIC Conference
year: 2020
bibkey: blancomallo2020effectiveness
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.06205'}]
tags: ["Recommender Systems"]
short_authors: Blanco-Mallo et al.
---
Recommender systems (RS) are increasingly present in our daily lives,
especially since the advent of Big Data, which allows for storing all kinds of
information about users' preferences. Personalized RS are successfully applied
in platforms such as Netflix, Amazon or YouTube. However, they are missing in
gastronomic platforms such as TripAdvisor, where moreover we can find millions
of images tagged with users' tastes. This paper explores the potential of using
those images as sources of information for modeling users' tastes and proposes
an image-based classification system to obtain personalized recommendations,
using a convolutional autoencoder as feature extractor. The proposed
architecture will be applied to TripAdvisor data, using users' reviews that can
be defined as a triad composed by a user, a restaurant, and an image of it
taken by the user. Since the dataset is highly unbalanced, the use of data
augmentation on the minority class is also considered in the experimentation.
Results on data from three cities of different sizes (Santiago de Compostela,
Barcelona and New York) demonstrate the effectiveness of using a convolutional
autoencoder as feature extractor, instead of the standard deep features
computed with convolutional neural networks.