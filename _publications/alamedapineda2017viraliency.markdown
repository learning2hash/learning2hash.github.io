---
layout: publication
title: 'Viraliency: Pooling Local Virality'
authors: Xavier Alameda-Pineda, Andrea Pilzer, Dan Xu, Nicu Sebe, Elisa Ricci
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: alamedapineda2017viraliency
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.03937'}]
tags: ["CVPR"]
short_authors: Alameda-Pineda et al.
---
In our overly-connected world, the automatic recognition of virality - the
quality of an image or video to be rapidly and widely spread in social networks
- is of crucial importance, and has recently awaken the interest of the
computer vision community. Concurrently, recent progress in deep learning
architectures showed that global pooling strategies allow the extraction of
activation maps, which highlight the parts of the image most likely to contain
instances of a certain class. We extend this concept by introducing a pooling
layer that learns the size of the support area to be averaged: the learned
top-N average (LENA) pooling. We hypothesize that the latent concepts (feature
maps) describing virality may require such a rich pooling strategy. We assess
the effectiveness of the LENA layer by appending it on top of a convolutional
siamese architecture and evaluate its performance on the task of predicting and
localizing virality. We report experiments on two publicly available datasets
annotated for virality and show that our method outperforms state-of-the-art
approaches.