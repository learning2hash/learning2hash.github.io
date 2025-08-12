---
layout: publication
title: A Multimodal Approach For Multi-label Movie Genre Classification
authors: "Rafael B. Mangolin, Rodolfo M. Pereira, Alceu S. Britto, Carlos N. Silla,\
  \ Val\xE9ria D. Feltrim, Diego Bertolini, Yandre M. G. Costa"
conference: Multimedia Tools and Applications
year: 2020
bibkey: mangolin2020multimodal
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.00654'}]
tags: ["Datasets", "Evaluation"]
short_authors: Mangolin et al.
---
Movie genre classification is a challenging task that has increasingly
attracted the attention of researchers. In this paper, we addressed the
multi-label classification of the movie genres in a multimodal way. For this
purpose, we created a dataset composed of trailer video clips, subtitles,
synopses, and movie posters taken from 152,622 movie titles from The Movie
Database. The dataset was carefully curated and organized, and it was also made
available as a contribution of this work. Each movie of the dataset was labeled
according to a set of eighteen genre labels. We extracted features from these
data using different kinds of descriptors, namely Mel Frequency Cepstral
Coefficients, Statistical Spectrum Descriptor , Local Binary Pattern with
spectrograms, Long-Short Term Memory, and Convolutional Neural Networks. The
descriptors were evaluated using different classifiers, such as BinaryRelevance
and ML-kNN. We have also investigated the performance of the combination of
different classifiers/features using a late fusion strategy, which obtained
encouraging results. Based on the F-Score metric, our best result, 0.628, was
obtained by the fusion of a classifier created using LSTM on the synopses, and
a classifier created using CNN on movie trailer frames. When considering the
AUC-PR metric, the best result, 0.673, was also achieved by combining those
representations, but in addition, a classifier based on LSTM created from the
subtitles was used. These results corroborate the existence of complementarity
among classifiers based on different sources of information in this field of
application. As far as we know, this is the most comprehensive study developed
in terms of the diversity of multimedia sources of information to perform movie
genre classification.