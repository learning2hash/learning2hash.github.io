---
layout: publication
title: Deep Metric Learning For Ground Images
authors: Raaghav Radhakrishnan, Jan Fabian Schmid, Randolf Scholz, Lars Schmidt-Thieme
conference: Arxiv
year: 2021
bibkey: radhakrishnan2021deep
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.01569'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Radhakrishnan et al.
---
Ground texture based localization methods are potential prospects for
low-cost, high-accuracy self-localization solutions for robots. These methods
estimate the pose of a given query image, i.e. the current observation of the
ground from a downward-facing camera, in respect to a set of reference images
whose poses are known in the application area. In this work, we deal with the
initial localization task, in which we have no prior knowledge about the
current robot positioning. In this situation, the localization method would
have to consider all available reference images. However, in order to reduce
computational effort and the risk of receiving a wrong result, we would like to
consider only those reference images that are actually overlapping with the
query image. For this purpose, we propose a deep metric learning approach that
retrieves the most similar reference images to the query image. In contrast to
existing approaches to image retrieval for ground images, our approach achieves
significantly better recall performance and improves the localization
performance of a state-of-the-art ground texture based localization method.