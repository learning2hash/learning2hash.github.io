---
layout: publication
title: 'Autonovel: Automatically Discovering And Learning Novel Visual Categories'
authors: "Kai Han, Sylvestre-Alvise Rebuffi, S\xE9bastien Ehrhardt, Andrea Vedaldi,\
  \ Andrew Zisserman"
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2021
bibkey: han2021autonovel
citations: 90
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.15252'}]
tags: []
short_authors: Han et al.
---
We tackle the problem of discovering novel classes in an image collection
given labelled examples of other classes. We present a new approach called
AutoNovel to address this problem by combining three ideas: (1) we suggest that
the common approach of bootstrapping an image representation using the labelled
data only introduces an unwanted bias, and that this can be avoided by using
self-supervised learning to train the representation from scratch on the union
of labelled and unlabelled data; (2) we use ranking statistics to transfer the
model's knowledge of the labelled classes to the problem of clustering the
unlabelled images; and, (3) we train the data representation by optimizing a
joint objective function on the labelled and unlabelled subsets of the data,
improving both the supervised classification of the labelled data, and the
clustering of the unlabelled data. Moreover, we propose a method to estimate
the number of classes for the case where the number of new categories is not
known a priori. We evaluate AutoNovel on standard classification benchmarks and
substantially outperform current methods for novel category discovery. In
addition, we also show that AutoNovel can be used for fully unsupervised image
clustering, achieving promising results.