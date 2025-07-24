---
layout: publication
title: Unsupervised Image Decomposition In Vector Layers
authors: Othman Sbai, Camille Couprie, Mathieu Aubry
conference: 2020 IEEE International Conference on Image Processing (ICIP)
year: 2020
bibkey: sbai2020unsupervised
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.05484'}]
tags: ["Datasets", "Efficiency", "Image Retrieval", "Unsupervised"]
short_authors: Othman Sbai, Camille Couprie, Mathieu Aubry
---
Deep image generation is becoming a tool to enhance artists and designers
creativity potential. In this paper, we aim at making the generation process
more structured and easier to interact with. Inspired by vector graphics
systems, we propose a new deep image reconstruction paradigm where the outputs
are composed from simple layers, defined by their color and a vector
transparency mask. This presents a number of advantages compared to the
commonly used convolutional network architectures. In particular, our layered
decomposition allows simple user interaction, for example to update a given
mask, or change the color of a selected layer. From a compact code, our
architecture also generates vector images with a virtually infinite resolution,
the color at each point in an image being a parametric function of its
coordinates. We validate the efficiency of our approach by comparing
reconstructions with state-of-the-art baselines given similar memory resources
on CelebA and ImageNet datasets. Most importantly, we demonstrate several
applications of our new image representation obtained in an unsupervised
manner, including editing, vectorization and image search.