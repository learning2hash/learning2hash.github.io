---
layout: publication
title: Using Unlabeled Data For Increasing Low-shot Classification Accuracy Of Relevant
  And Open-set Irrelevant Images
authors: Spiridon Kasapis, Geng Zhang, Jonathon Smereka, Nickolas Vlahopoulos
conference: Arxiv
year: 2020
bibkey: kasapis2020using
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.00721'}]
tags: ["Few Shot & Zero Shot", "Unsupervised"]
short_authors: Kasapis et al.
---
In search, exploration, and reconnaissance tasks performed with autonomous
ground vehicles, an image classification capability is needed for specifically
identifying targeted objects (relevant classes) and at the same time recognize
when a candidate image does not belong to anyone of the relevant classes
(irrelevant images). In this paper, we present an open-set low-shot classifier
that uses, during its training, a modest number (less than 40) of labeled
images for each relevant class, and unlabeled irrelevant images that are
randomly selected at each epoch of the training process. The new classifier is
capable of identifying images from the relevant classes, determining when a
candidate image is irrelevant, and it can further recognize categories of
irrelevant images that were not included in the training (unseen). The proposed
low-shot classifier can be attached as a top layer to any pre-trained feature
extractor when constructing a Convolutional Neural Network.