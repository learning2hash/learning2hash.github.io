---
layout: publication
title: Spatial Entity Resolution Between Restaurant Locations And Transportation Destinations
  In Southeast Asia
authors: Emily Gao, Dominic Widdows
conference: Proceedings of the 6th International Conference on Geographical Information
  Systems Theory, Applications and Management
year: 2020
bibkey: gao2020spatial
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.08537'}]
tags: ["Datasets"]
short_authors: Emily Gao, Dominic Widdows
---
As a tech company, Grab has expanded from transportation to food delivery,
aiming to serve Southeast Asia with hyperlocalized applications. Information
about places as transportation destinations can help to improve our knowledge
about places as restaurants, so long as the spatial entity resolution problem
between these datasets can be solved. In this project, we attempted to
recognize identical place entities from databases of Points-of-Interest (POI)
and GrabFood restaurants, using their spatial and textual attributes, i.e.,
latitude, longitude, place name, and street address.
  Distance metrics were calculated for these attributes and fed to tree-based
classifiers. POI-restaurant matching was conducted separately for Singapore,
Philippines, Indonesia, and Malaysia. Experimental estimates demonstrate that a
matching POI can be found for over 35% of restaurants in these countries. As
part of these estimates, test datasets were manually created, and RandomForest,
AdaBoost, Gradient Boosting, and XGBoost perform well, with most accuracy,
precision, and recall scores close to or higher than 90% for matched vs.
unmatched classification. To the authors' knowledge, there are no previous
published scientific papers devoted to matching of spatial entities for the
Southeast Asia region.