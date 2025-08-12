---
layout: publication
title: Contrastive Object Detection Using Knowledge Graph Embeddings
authors: Christopher Lang, Alexander Braun, Abhinav Valada
conference: Arxiv
year: 2021
bibkey: lang2021contrastive
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.11366'}]
tags: ["Distance Metric Learning"]
short_authors: Christopher Lang, Alexander Braun, Abhinav Valada
---
Object recognition for the most part has been approached as a one-hot problem
that treats classes to be discrete and unrelated. Each image region has to be
assigned to one member of a set of objects, including a background class,
disregarding any similarities in the object types. In this work, we compare the
error statistics of the class embeddings learned from a one-hot approach with
semantically structured embeddings from natural language processing or
knowledge graphs that are widely applied in open world object detection.
Extensive experimental results on multiple knowledge-embeddings as well as
distance metrics indicate that knowledge-based class representations result in
more semantically grounded misclassifications while performing on par compared
to one-hot methods on the challenging COCO and Cityscapes object detection
benchmarks. We generalize our findings to multiple object detection
architectures by proposing a knowledge-embedded design for keypoint-based and
transformer-based object detection architectures.