---
layout: publication
title: Unsupervised Object Discovery For Instance Recognition
authors: "Oriane Sim\xE9oni, Ahmet Iscen, Giorgos Tolias, Yannis Avrithis, Ondrej\
  \ Chum"
conference: 2018 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2018
bibkey: "sim\xE9oni2017unsupervised"
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.04725'}]
tags: ["Datasets", "Efficiency", "Image Retrieval", "Scalability", "Unsupervised"]
short_authors: "Sim\xE9oni et al."
---
Severe background clutter is challenging in many computer vision tasks,
including large-scale image retrieval. Global descriptors, that are popular due
to their memory and search efficiency, are especially prone to corruption by
such a clutter. Eliminating the impact of the clutter on the image descriptor
increases the chance of retrieving relevant images and prevents topic drift due
to actually retrieving the clutter in the case of query expansion. In this
work, we propose a novel salient region detection method. It captures, in an
unsupervised manner, patterns that are both discriminative and common in the
dataset. Saliency is based on a centrality measure of a nearest neighbor graph
constructed from regional CNN representations of dataset images. The
descriptors derived from the salient regions improve particular object
retrieval, most noticeably in a large collections containing small objects.