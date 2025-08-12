---
layout: publication
title: 'Semantic Jitter: Dense Supervision For Visual Comparisons Via Synthetic Images'
authors: Aron Yu, Kristen Grauman
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: yu2016semantic
citations: 114
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.06341'}]
tags: ["ICCV"]
short_authors: Aron Yu, Kristen Grauman
---
Distinguishing subtle differences in attributes is valuable, yet learning to
make visual comparisons remains non-trivial. Not only is the number of possible
comparisons quadratic in the number of training images, but also access to
images adequately spanning the space of fine-grained visual differences is
limited. We propose to overcome the sparsity of supervision problem via
synthetically generated images. Building on a state-of-the-art image generation
engine, we sample pairs of training images exhibiting slight modifications of
individual attributes. Augmenting real training image pairs with these
examples, we then train attribute ranking models to predict the relative
strength of an attribute in novel pairs of real images. Our results on datasets
of faces and fashion images show the great promise of bootstrapping imperfect
image generators to counteract sample sparsity for learning to rank.