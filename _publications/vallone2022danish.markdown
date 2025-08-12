---
layout: publication
title: 'Danish Airs And Grounds: A Dataset For Aerial-to-street-level Place Recognition
  And Localization'
authors: "Andrea Vallone, Frederik Warburg, Hans Hansen, S\xF8ren Hauberg, Javier\
  \ Civera"
conference: IEEE Robotics and Automation Letters
year: 2022
bibkey: vallone2022danish
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.01821'}]
tags: ["Datasets"]
short_authors: Vallone et al.
---
Place recognition and visual localization are particularly challenging in
wide baseline configurations. In this paper, we contribute with the
*Danish Airs and Grounds* (DAG) dataset, a large collection of
street-level and aerial images targeting such cases. Its main challenge lies in
the extreme viewing-angle difference between query and reference images with
consequent changes in illumination and perspective. The dataset is larger and
more diverse than current publicly available data, including more than 50 km of
road in urban, suburban and rural areas. All images are associated with
accurate 6-DoF metadata that allows the benchmarking of visual localization
methods.
  We also propose a map-to-image re-localization pipeline, that first estimates
a dense 3D reconstruction from the aerial images and then matches query
street-level images to street-level renderings of the 3D model. The dataset can
be downloaded at: https://frederikwarburg.github.io/DAG