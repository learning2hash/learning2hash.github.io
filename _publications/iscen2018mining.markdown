---
layout: publication
title: 'Mining On Manifolds: Metric Learning Without Labels'
authors: Ahmet Iscen, Giorgos Tolias, Yannis Avrithis, Ondrej Chum
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: iscen2018mining
citations: 112
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.11095'}]
tags: ["CVPR", "Distance Metric Learning", "Unsupervised"]
short_authors: Iscen et al.
---
In this work we present a novel unsupervised framework for hard training
example mining. The only input to the method is a collection of images relevant
to the target application and a meaningful initial representation, provided
e.g. by pre-trained CNN. Positive examples are distant points on a single
manifold, while negative examples are nearby points on different manifolds.
Both types of examples are revealed by disagreements between Euclidean and
manifold similarities. The discovered examples can be used in training with any
discriminative loss. The method is applied to unsupervised fine-tuning of
pre-trained networks for fine-grained classification and particular object
retrieval. Our models are on par or are outperforming prior models that are
fully or partially supervised.