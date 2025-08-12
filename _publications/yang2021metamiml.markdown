---
layout: publication
title: 'Metamiml: Meta Multi-instance Multi-label Learning'
authors: Yuanlin Yang, Guoxian Yu, Jun Wang, Lei Liu, Carlotta Domeniconi, Maozu Guo
conference: Arxiv
year: 2021
bibkey: yang2021metamiml
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04112'}]
tags: []
short_authors: Yang et al.
---
Multi-Instance Multi-Label learning (MIML) models complex objects (bags),
each of which is associated with a set of interrelated labels and composed with
a set of instances. Current MIML solutions still focus on a single-type of
objects and assumes an IID distribution of training data. But these objects are
linked with objects of other types, %(i.e., pictures in Facebook link with
various users), which also encode the semantics of target objects. In addition,
they generally need abundant labeled data for training. To effectively mine
interdependent MIML objects of different types, we propose a network embedding
and meta learning based approach (MetaMIML). MetaMIML introduces the context
learner with network embedding to capture semantic information of objects of
different types, and the task learner to extract the meta knowledge for fast
adapting to new tasks. In this way, MetaMIML can naturally deal with MIML
objects at data level improving, but also exploit the power of meta-learning at
the model enhancing. Experiments on benchmark datasets demonstrate that
MetaMIML achieves a significantly better performance than state-of-the-art
algorithms.