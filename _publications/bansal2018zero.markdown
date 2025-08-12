---
layout: publication
title: Zero-shot Object Detection
authors: Ankan Bansal, Karan Sikka, Gaurav Sharma, Rama Chellappa, Ajay Divakaran
conference: Lecture Notes in Computer Science
year: 2018
bibkey: bansal2018zero
citations: 321
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04340'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bansal et al.
---
We introduce and tackle the problem of zero-shot object detection (ZSD),
which aims to detect object classes which are not observed during training. We
work with a challenging set of object classes, not restricting ourselves to
similar and/or fine-grained categories as in prior works on zero-shot
classification. We present a principled approach by first adapting
visual-semantic embeddings for ZSD. We then discuss the problems associated
with selecting a background class and motivate two background-aware approaches
for learning robust detectors. One of these models uses a fixed background
class and the other is based on iterative latent assignments. We also outline
the challenge associated with using a limited number of training classes and
propose a solution based on dense sampling of the semantic label space using
auxiliary data with a large number of categories. We propose novel splits of
two standard detection datasets - MSCOCO and VisualGenome, and present
extensive empirical results in both the traditional and generalized zero-shot
settings to highlight the benefits of the proposed methods. We provide useful
insights into the algorithm and conclude by posing some open questions to
encourage further research.