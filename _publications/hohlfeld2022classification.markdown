---
layout: publication
title: Classification Of Beer Bottles Using Object Detection And Transfer Learning
authors: Philipp Hohlfeld, Tobias Ostermeier, Dominik Brandl
conference: Arxiv
year: 2022
bibkey: hohlfeld2022classification
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.03791'}]
tags: ["Datasets"]
short_authors: Philipp Hohlfeld, Tobias Ostermeier, Dominik Brandl
---
Classification problems are common in Computer Vision. Despite this, there is
no dedicated work for the classification of beer bottles. As part of the
challenge of the master course Deep Learning, a dataset of 5207 beer bottle
images and brand labels was created. An image contains exactly one beer bottle.
In this paper we present a deep learning model which classifies pictures of
beer bottles in a two step approach. As the first step, a Faster-R-CNN detects
image sections relevant for classification independently of the brand. In the
second step, the relevant image sections are classified by a ResNet-18. The
image section with the highest confidence is returned as class label. We
propose a model, with which we surpass the classic one step transfer learning
approach and reached an accuracy of 99.86% during the challenge on the final
test dataset. We were able to achieve 100% accuracy after the challenge ended