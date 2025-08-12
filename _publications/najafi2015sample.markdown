---
layout: publication
title: 'Sample And Filter: Nonparametric Scene Parsing Via Efficient Filtering'
authors: Mohammad Najafi, Sarah Taghavi Namin, Mathieu Salzmann, Lars Petersson
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: najafi2015sample
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.04960'}]
tags: ["CVPR"]
short_authors: Najafi et al.
---
Scene parsing has attracted a lot of attention in computer vision. While
parametric models have proven effective for this task, they cannot easily
incorporate new training data. By contrast, nonparametric approaches, which
bypass any learning phase and directly transfer the labels from the training
data to the query images, can readily exploit new labeled samples as they
become available. Unfortunately, because of the computational cost of their
label transfer procedures, state-of-the-art nonparametric methods typically
filter out most training images to only keep a few relevant ones to label the
query. As such, these methods throw away many images that still contain
valuable information and generally obtain an unbalanced set of labeled samples.
In this paper, we introduce a nonparametric approach to scene parsing that
follows a sample-and-filter strategy. More specifically, we propose to sample
labeled superpixels according to an image similarity score, which allows us to
obtain a balanced set of samples. We then formulate label transfer as an
efficient filtering procedure, which lets us exploit more labeled samples than
existing techniques. Our experiments evidence the benefits of our approach over
state-of-the-art nonparametric methods on two benchmark datasets.