---
layout: publication
title: Aligning Visual Prototypes With BERT Embeddings For Few-shot Learning
authors: Kun Yan, Zied Bouraoui, Ping Wang, Shoaib Jameel, Steven Schockaert
conference: Proceedings of the 2021 International Conference on Multimedia Retrieval
year: 2021
bibkey: yan2021aligning
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.10195'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yan et al.
---
Few-shot learning (FSL) is the task of learning to recognize previously
unseen categories of images from a small number of training examples. This is a
challenging task, as the available examples may not be enough to unambiguously
determine which visual features are most characteristic of the considered
categories. To alleviate this issue, we propose a method that additionally
takes into account the names of the image classes. While the use of class names
has already been explored in previous work, our approach differs in two key
aspects. First, while previous work has aimed to directly predict visual
prototypes from word embeddings, we found that better results can be obtained
by treating visual and text-based prototypes separately. Second, we propose a
simple strategy for learning class name embeddings using the BERT language
model, which we found to substantially outperform the GloVe vectors that were
used in previous work. We furthermore propose a strategy for dealing with the
high dimensionality of these vectors, inspired by models for aligning
cross-lingual word embeddings. We provide experiments on miniImageNet, CUB and
tieredImageNet, showing that our approach consistently improves the
state-of-the-art in metric-based FSL.