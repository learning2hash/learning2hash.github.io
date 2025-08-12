---
layout: publication
title: One-shot Learning In Discriminative Neural Networks
authors: Jordan Burgess, James Robert Lloyd, Zoubin Ghahramani
conference: Arxiv
year: 2017
bibkey: burgess2017one
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05562'}]
tags: []
short_authors: Jordan Burgess, James Robert Lloyd, Zoubin Ghahramani
---
We consider the task of one-shot learning of visual categories. In this paper
we explore a Bayesian procedure for updating a pretrained convnet to classify a
novel image category for which data is limited. We decompose this convnet into
a fixed feature extractor and softmax classifier. We assume that the target
weights for the new task come from the same distribution as the pretrained
softmax weights, which we model as a multivariate Gaussian. By using this as a
prior for the new weights, we demonstrate competitive performance with
state-of-the-art methods whilst also being consistent with 'normal' methods for
training deep networks on large data.