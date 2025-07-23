---
layout: publication
title: 'VISER: Visual Self-regularization'
authors: Izadinia Hamid, Garrigues Pierre
conference: Arxiv
year: 2018
bibkey: izadinia2018viser
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.02568'}]
tags: ["Distance Metric Learning", "Evaluation", "Supervised"]
short_authors: Izadinia Hamid, Garrigues Pierre
---
In this work, we propose the use of large set of unlabeled images as a source
of regularization data for learning robust visual representation. Given a
visual model trained by a labeled dataset in a supervised fashion, we augment
our training samples by incorporating large number of unlabeled data and train
a semi-supervised model. We demonstrate that our proposed learning approach
leverages an abundance of unlabeled images and boosts the visual recognition
performance which alleviates the need to rely on large labeled datasets for
learning robust representation. To increment the number of image instances
needed to learn robust visual models in our approach, each labeled image
propagates its label to its nearest unlabeled image instances. These retrieved
unlabeled images serve as local perturbations of each labeled image to perform
Visual Self-Regularization (VISER). To retrieve such visual self regularizers,
we compute the cosine similarity in a semantic space defined by the penultimate
layer in a fully convolutional neural network. We use the publicly available
Yahoo Flickr Creative Commons 100M dataset as the source of our unlabeled image
set and propose a distributed approximate nearest neighbor algorithm to make
retrieval practical at that scale. Using the labeled instances and their
regularizer samples we show that we significantly improve object categorization
and localization performance on the MS COCO and Visual Genome datasets where
objects appear in context.