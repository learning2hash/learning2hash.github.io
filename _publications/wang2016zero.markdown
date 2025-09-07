---
layout: publication
title: Zero-shot Visual Recognition Via Bidirectional Latent Embedding
authors: Qian Wang, Ke Chen
conference: International Journal of Computer Vision
year: 2017
bibkey: wang2016zero
citations: 171
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.02104'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Supervised", "Tools & Libraries"]
short_authors: Qian Wang, Ke Chen
---
Zero-shot learning for visual recognition, e.g., object and action
recognition, has recently attracted a lot of attention. However, it still
remains challenging in bridging the semantic gap between visual features and
their underlying semantics and transferring knowledge to semantic categories
unseen during learning. Unlike most of the existing zero-shot visual
recognition methods, we propose a stagewise bidirectional latent embedding
framework to two subsequent learning stages for zero-shot visual recognition.
In the bottom-up stage, a latent embedding space is first created by exploring
the topological and labeling information underlying training data of known
classes via a proper supervised subspace learning algorithm and the latent
embedding of training data are used to form landmarks that guide embedding
semantics underlying unseen classes into this learned latent space. In the
top-down stage, semantic representations of unseen-class labels in a given
label vocabulary are then embedded to the same latent space to preserve the
semantic relatedness between all different classes via our proposed
semi-supervised Sammon mapping with the guidance of landmarks. Thus, the
resultant latent embedding space allows for predicting the label of a test
instance with a simple nearest-neighbor rule. To evaluate the effectiveness of
the proposed framework, we have conducted extensive experiments on four
benchmark datasets in object and action recognition, i.e., AwA, CUB-200-2011,
UCF101 and HMDB51. The experimental results under comparative studies
demonstrate that our proposed approach yields the state-of-the-art performance
under inductive and transductive settings.