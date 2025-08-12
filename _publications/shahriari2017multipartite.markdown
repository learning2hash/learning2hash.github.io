---
layout: publication
title: Multipartite Pooling For Deep Convolutional Neural Networks
authors: Arash Shahriari, Fatih Porikli
conference: Arxiv
year: 2017
bibkey: shahriari2017multipartite
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.07435'}]
tags: []
short_authors: Arash Shahriari, Fatih Porikli
---
We propose a novel pooling strategy that learns how to adaptively rank deep
convolutional features for selecting more informative representations. To this
end, we exploit discriminative analysis to project the features onto a space
spanned by the number of classes in the dataset under study. This maps the
notion of labels in the feature space into instances in the projected space. We
employ these projected distances as a measure to rank the existing features
with respect to their specific discriminant power for each individual class. We
then apply multipartite ranking to score the separability of the instances and
aggregate one-versus-all scores to compute an overall distinction score for
each feature. For the pooling, we pick features with the highest scores in a
pooling window instead of maximum, average or stochastic random assignments.
Our experiments on various benchmarks confirm that the proposed strategy of
multipartite pooling is highly beneficial to consistently improve the
performance of deep convolutional networks via better generalization of the
trained models for the test-time data.