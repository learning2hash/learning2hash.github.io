---
layout: publication
title: Salient Object Detection For Images Taken By People With Vision Impairments
authors: Jarek Reynolds, Chandra Kanth Nagesh, Danna Gurari
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: reynolds2023salient
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.05323'}]
tags: ["Datasets"]
short_authors: Jarek Reynolds, Chandra Kanth Nagesh, Danna Gurari
---
Salient object detection is the task of producing a binary mask for an image
that deciphers which pixels belong to the foreground object versus background.
We introduce a new salient object detection dataset using images taken by
people who are visually impaired who were seeking to better understand their
surroundings, which we call VizWiz-SalientObject. Compared to seven existing
datasets, VizWiz-SalientObject is the largest (i.e., 32,000 human-annotated
images) and contains unique characteristics including a higher prevalence of
text in the salient objects (i.e., in 68% of images) and salient objects that
occupy a larger ratio of the images (i.e., on average, \\(\sim\\)50% coverage). We
benchmarked seven modern salient object detection methods on our dataset and
found they struggle most with images featuring salient objects that are large,
have less complex boundaries, and lack text as well as for lower quality
images. We invite the broader community to work on our new dataset challenge by
publicly sharing the dataset at
https://vizwiz.org/tasks-and-datasets/salient-object .