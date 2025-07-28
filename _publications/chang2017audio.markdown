---
layout: publication
title: Audio Cover Song Identification Using Convolutional Neural Network
authors: Sungkyun Chang, Juheon Lee, Sang Keun Choe, Kyogu Lee
conference: Arxiv
year: 2017
bibkey: chang2017audio
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.00166'}]
tags: []
short_authors: Chang et al.
---
In this paper, we propose a new approach to cover song identification using a
CNN (convolutional neural network). Most previous studies extract the feature
vectors that characterize the cover song relation from a pair of songs and used
it to compute the (dis)similarity between the two songs. Based on the
observation that there is a meaningful pattern between cover songs and that
this can be learned, we have reformulated the cover song identification problem
in a machine learning framework. To do this, we first build the CNN using as an
input a cross-similarity matrix generated from a pair of songs. We then
construct the data set composed of cover song pairs and non-cover song pairs,
which are used as positive and negative training samples, respectively. The
trained CNN outputs the probability of being in the cover song relation given a
cross-similarity matrix generated from any two pieces of music and identifies
the cover song by ranking on the probability. Experimental results show that
the proposed algorithm achieves performance better than or comparable to the
state-of-the-art.