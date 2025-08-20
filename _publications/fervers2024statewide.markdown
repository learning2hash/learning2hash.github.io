---
layout: publication
title: Statewide Visual Geolocalization In The Wild
authors: Florian Fervers, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens,
  Rainer Stiefelhagen
conference: Arxiv
year: 2024
bibkey: fervers2024statewide
citations: 0
additional_links: [{name: Code, url: 'https://github.com/fferflo/statewide-visual-geolocalization.'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.16763'}]
tags: [Evaluation]
short_authors: Fervers et al.
---
This work presents a method that is able to predict the geolocation of a
street-view photo taken in the wild within a state-sized search region by
matching against a database of aerial reference imagery. We partition the
search region into geographical cells and train a model to map cells and
corresponding photos into a joint embedding space that is used to perform
retrieval at test time. The model utilizes aerial images for each cell at
multiple levels-of-detail to provide sufficient information about the
surrounding scene. We propose a novel layout of the search region with
consistent cell resolutions that allows scaling to large geographical regions.
Experiments demonstrate that the method successfully localizes 60.6% of all
non-panoramic street-view photos uploaded to the crowd-sourcing platform
Mapillary in the state of Massachusetts to within 50m of their ground-truth
location. Source code is available at
https://github.com/fferflo/statewide-visual-geolocalization.