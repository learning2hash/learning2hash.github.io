---
layout: publication
title: A Convolutional Approach To Melody Line Identification In Symbolic Scores
authors: "Federico Simonetta, Carlos Cancino-Chac\xF3n, Stavros Ntalampiras, Gerhard\
  \ Widmer"
conference: Arxiv
year: 2019
bibkey: simonetta2019convolutional
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.10547'}]
tags: []
short_authors: Simonetta et al.
---
In many musical traditions, the melody line is of primary significance in a
piece. Human listeners can readily distinguish melodies from accompaniment;
however, making this distinction given only the written score -- i.e. without
listening to the music performed -- can be a difficult task. Solving this task
is of great importance for both Music Information Retrieval and musicological
applications. In this paper, we propose an automated approach to identifying
the most salient melody line in a symbolic score. The backbone of the method
consists of a convolutional neural network (CNN) estimating the probability
that each note in the score (more precisely: each pixel in a piano roll
encoding of the score) belongs to the melody line. We train and evaluate the
method on various datasets, using manual annotations where available and solo
instrument parts where not. We also propose a method to inspect the CNN and to
analyze the influence exerted by notes on the prediction of other notes; this
method can be applied whenever the output of a neural network has the same size
as the input.