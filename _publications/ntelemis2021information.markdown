---
layout: publication
title: Information Maximization Clustering Via Multi-view Self-labelling
authors: Foivos Ntelemis, Yaochu Jin, Spencer A. Thomas
conference: Knowledge-Based Systems
year: 2022
bibkey: ntelemis2021information
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.07368'}]
tags: []
short_authors: Foivos Ntelemis, Yaochu Jin, Spencer A. Thomas
---
Image clustering is a particularly challenging computer vision task, which
aims to generate annotations without human supervision. Recent advances focus
on the use of self-supervised learning strategies in image clustering, by first
learning valuable semantics and then clustering the image representations.
These multiple-phase algorithms, however, increase the computational time and
their final performance is reliant on the first stage. By extending the
self-supervised approach, we propose a novel single-phase clustering method
that simultaneously learns meaningful representations and assigns the
corresponding annotations. This is achieved by integrating a discrete
representation into the self-supervised paradigm through a classifier net.
Specifically, the proposed clustering objective employs mutual information, and
maximizes the dependency between the integrated discrete representation and a
discrete probability distribution. The discrete probability distribution is
derived though the self-supervised process by comparing the learnt latent
representation with a set of trainable prototypes. To enhance the learning
performance of the classifier, we jointly apply the mutual information across
multi-crop views. Our empirical results show that the proposed framework
outperforms state-of-the-art techniques with the average accuracy of 89.1% and
49.0%, respectively, on CIFAR-10 and CIFAR-100/20 datasets. Finally, the
proposed method also demonstrates attractive robustness to parameter settings,
making it ready to be applicable to other datasets.