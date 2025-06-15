---
layout: publication
title: 'Netvlad: CNN Architecture For Weakly Supervised Place Recognition'
authors: Relja Arandjelović, Petr Gronat, Akihiko Torii, Tomas Pajdla, Josef Sivic
conference: "Arxiv"
year: 2015
citations: 438
bibkey: arandjelović2015cnn
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1511.07247'}
tags: ['Loss Functions', 'Applications', 'Evaluation Metrics', 'ANN Search', 'Learning Strategies']
---
We tackle the problem of large scale visual place recognition, where the task
is to quickly and accurately recognize the location of a given query
photograph. We present the following three principal contributions. First, we
develop a convolutional neural network (CNN) architecture that is trainable in
an end-to-end manner directly for the place recognition task. The main
component of this architecture, NetVLAD, is a new generalized VLAD layer,
inspired by the "Vector of Locally Aggregated Descriptors" image representation
commonly used in image retrieval. The layer is readily pluggable into any CNN
architecture and amenable to training via backpropagation. Second, we develop a
training procedure, based on a new weakly supervised ranking loss, to learn
parameters of the architecture in an end-to-end manner from images depicting
the same places over time downloaded from Google Street View Time Machine.
Finally, we show that the proposed architecture significantly outperforms
non-learnt image representations and off-the-shelf CNN descriptors on two
challenging place recognition benchmarks, and improves over current
state-of-the-art compact image representations on standard image retrieval
benchmarks.
