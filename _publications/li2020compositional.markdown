---
layout: publication
title: Compositional Embeddings For Multi-label One-shot Learning
authors: Zeqian Li, Michael C. Mozer, Jacob Whitehill
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: li2020compositional
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.04193'}]
tags: []
short_authors: Zeqian Li, Michael C. Mozer, Jacob Whitehill
---
We present a compositional embedding framework that infers not just a single
class per input image, but a set of classes, in the setting of one-shot
learning. Specifically, we propose and evaluate several novel models consisting
of (1) an embedding function f trained jointly with a "composition" function g
that computes set union operations between the classes encoded in two embedding
vectors; and (2) embedding f trained jointly with a "query" function h that
computes whether the classes encoded in one embedding subsume the classes
encoded in another embedding. In contrast to prior work, these models must both
perceive the classes associated with the input examples and encode the
relationships between different class label sets, and they are trained using
only weak one-shot supervision consisting of the label-set relationships among
training examples. Experiments on the OmniGlot, Open Images, and COCO datasets
show that the proposed compositional embedding models outperform existing
embedding methods. Our compositional embedding models have applications to
multi-label object recognition for both one-shot and supervised learning.