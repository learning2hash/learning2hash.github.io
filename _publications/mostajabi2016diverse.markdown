---
layout: publication
title: Diverse Sampling For Self-supervised Learning Of Semantic Segmentation
authors: Mohammadreza Mostajabi, Nicholas Kolkin, Gregory Shakhnarovich
conference: Arxiv
year: 2016
bibkey: mostajabi2016diverse
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.01991'}]
tags: ["Self-Supervised"]
short_authors: Mohammadreza Mostajabi, Nicholas Kolkin, Gregory Shakhnarovich
---
We propose an approach for learning category-level semantic segmentation
purely from image-level classification tags indicating presence of categories.
It exploits localization cues that emerge from training classification-tasked
convolutional networks, to drive a "self-supervision" process that
automatically labels a sparse, diverse training set of points likely to belong
to classes of interest. Our approach has almost no hyperparameters, is modular,
and allows for very fast training of segmentation in less than 3 minutes. It
obtains competitive results on the VOC 2012 segmentation benchmark. More,
significantly the modularity and fast training of our framework allows new
classes to efficiently added for inference.