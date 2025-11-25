---
layout: publication
title: Satellite Image-based Localization Via Learned Embeddings
authors: Dong-Ki Kim, Matthew R. Walter
conference: 2017 IEEE International Conference on Robotics and Automation (ICRA)
year: 2017
bibkey: kim2017satellite
citations: 75
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.01133'}]
tags: ["Evaluation", "ICRA"]
short_authors: Dong-Ki Kim, Matthew R. Walter
---
We propose a vision-based method that localizes a ground vehicle using
publicly available satellite imagery as the only prior knowledge of the
environment. Our approach takes as input a sequence of ground-level images
acquired by the vehicle as it navigates, and outputs an estimate of the
vehicle's pose relative to a georeferenced satellite image. We overcome the
significant viewpoint and appearance variations between the images through a
neural multi-view model that learns location-discriminative embeddings in which
ground-level images are matched with their corresponding satellite view of the
scene. We use this learned function as an observation model in a filtering
framework to maintain a distribution over the vehicle's pose. We evaluate our
method on different benchmark datasets and demonstrate its ability localize
ground-level images in environments novel relative to training, despite the
challenges of significant viewpoint and appearance variations.