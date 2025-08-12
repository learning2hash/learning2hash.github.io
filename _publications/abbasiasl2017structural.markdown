---
layout: publication
title: Structural Compression Of Convolutional Neural Networks
authors: Reza Abbasi-Asl, Bin Yu
conference: Arxiv
year: 2017
bibkey: abbasiasl2017structural
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.07356'}]
tags: []
short_authors: Reza Abbasi-Asl, Bin Yu
---
Deep convolutional neural networks (CNNs) have been successful in many tasks
in machine vision, however, millions of weights in the form of thousands of
convolutional filters in CNNs makes them difficult for human intepretation or
understanding in science. In this article, we introduce CAR, a greedy
structural compression scheme to obtain smaller and more interpretable CNNs,
while achieving close to original accuracy. The compression is based on pruning
filters with the least contribution to the classification accuracy. We
demonstrate the interpretability of CAR-compressed CNNs by showing that our
algorithm prunes filters with visually redundant functionalities such as color
filters. These compressed networks are easier to interpret because they retain
the filter diversity of uncompressed networks with order of magnitude less
filters. Finally, a variant of CAR is introduced to quantify the importance of
each image category to each CNN filter. Specifically, the most and the least
important class labels are shown to be meaningful interpretations of each
filter.