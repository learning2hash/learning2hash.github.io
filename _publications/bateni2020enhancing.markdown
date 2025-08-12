---
layout: publication
title: Enhancing Few-shot Image Classification With Unlabelled Examples
authors: Peyman Bateni, Jarred Barber, Jan-willem van de Meent, Frank Wood
conference: 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2022
bibkey: bateni2020enhancing
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.12245'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bateni et al.
---
We develop a transductive meta-learning method that uses unlabelled instances
to improve few-shot image classification performance. Our approach combines a
regularized Mahalanobis-distance-based soft k-means clustering procedure with a
modified state of the art neural adaptive feature extractor to achieve improved
test-time classification accuracy using unlabelled data. We evaluate our method
on transductive few-shot learning tasks, in which the goal is to jointly
predict labels for query (test) examples given a set of support (training)
examples. We achieve state of the art performance on the Meta-Dataset,
mini-ImageNet and tiered-ImageNet benchmarks. All trained models and code have
been made publicly available at github.com/plai-group/simple-cnaps.