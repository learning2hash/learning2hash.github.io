---
layout: publication
title: 'Cplanet: Enhancing Image Geolocalization By Combinatorial Partitioning Of
  Maps'
authors: Paul Hongsuck Seo, Tobias Weyand, Jack Sim, Bohyung Han
conference: Lecture Notes in Computer Science
year: 2018
bibkey: seo2018cplanet
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.02130'}]
tags: []
short_authors: Seo et al.
---
Image geolocalization is the task of identifying the location depicted in a
photo based only on its visual information. This task is inherently challenging
since many photos have only few, possibly ambiguous cues to their geolocation.
Recent work has cast this task as a classification problem by partitioning the
earth into a set of discrete cells that correspond to geographic regions. The
granularity of this partitioning presents a critical trade-off; using fewer but
larger cells results in lower location accuracy while using more but smaller
cells reduces the number of training examples per class and increases model
size, making the model prone to overfitting. To tackle this issue, we propose a
simple but effective algorithm, combinatorial partitioning, which generates a
large number of fine-grained output classes by intersecting multiple
coarse-grained partitionings of the earth. Each classifier votes for the
fine-grained classes that overlap with their respective coarse-grained ones.
This technique allows us to predict locations at a fine scale while maintaining
sufficient training examples per class. Our algorithm achieves the
state-of-the-art performance in location recognition on multiple benchmark
datasets.