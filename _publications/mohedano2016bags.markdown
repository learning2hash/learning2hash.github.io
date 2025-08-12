---
layout: publication
title: Bags Of Local Convolutional Features For Scalable Instance Search
authors: Eva Mohedano, Amaia Salvador, Kevin McGuinness, Ferran Marques, Noel E. O'Connor,
  Xavier Giro-I-Nieto
conference: Proceedings of the 2016 ACM on International Conference on Multimedia
  Retrieval
year: 2016
bibkey: mohedano2016bags
citations: 154
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.04653'}]
tags: []
short_authors: Mohedano et al.
---
This work proposes a simple instance retrieval pipeline based on encoding the
convolutional features of CNN using the bag of words aggregation scheme (BoW).
Assigning each local array of activations in a convolutional layer to a visual
word produces an \textit\{assignment map\}, a compact representation that relates
regions of an image with a visual word. We use the assignment map for fast
spatial reranking, obtaining object localizations that are used for query
expansion. We demonstrate the suitability of the BoW representation based on
local CNN features for instance retrieval, achieving competitive performance on
the Oxford and Paris buildings benchmarks. We show that our proposed system for
CNN feature aggregation with BoW outperforms state-of-the-art techniques using
sum pooling at a subset of the challenging TRECVid INS benchmark.