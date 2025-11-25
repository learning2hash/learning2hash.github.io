---
layout: publication
title: Compositional Learning Of Image-text Query For Image Retrieval
authors: Muhammad Umer Anwaar, Egor Labintcev, Martin Kleinsteuber
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: anwaar2020compositional
citations: 7
additional_links: [{name: Code, url: 'https://github.com/ecom-research/ComposeAE'},
  {name: Paper, url: 'https://arxiv.org/abs/2006.11149'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Muhammad Umer Anwaar, Egor Labintcev, Martin Kleinsteuber
---
In this paper, we investigate the problem of retrieving images from a
database based on a multi-modal (image-text) query. Specifically, the query
text prompts some modification in the query image and the task is to retrieve
images with the desired modifications. For instance, a user of an E-Commerce
platform is interested in buying a dress, which should look similar to her
friend's dress, but the dress should be of white color with a ribbon sash. In
this case, we would like the algorithm to retrieve some dresses with desired
modifications in the query dress. We propose an autoencoder based model,
ComposeAE, to learn the composition of image and text query for retrieving
images. We adopt a deep metric learning approach and learn a metric that pushes
composition of source image and text query closer to the target images. We also
propose a rotational symmetry constraint on the optimization problem. Our
approach is able to outperform the state-of-the-art method TIRG \cite\{TIRG\} on
three benchmark datasets, namely: MIT-States, Fashion200k and Fashion IQ. In
order to ensure fair comparison, we introduce strong baselines by enhancing
TIRG method. To ensure reproducibility of the results, we publish our code
here: https://github.com/ecom-research/ComposeAE.