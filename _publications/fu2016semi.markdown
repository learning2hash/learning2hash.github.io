---
layout: publication
title: Semi-supervised Vocabulary-informed Learning
authors: Yanwei Fu, Leonid Sigal
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: fu2016semi
citations: 116
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.07093'}]
tags: ["CVPR"]
short_authors: Yanwei Fu, Leonid Sigal
---
Despite significant progress in object categorization, in recent years, a
number of important challenges remain, mainly, ability to learn from limited
labeled data and ability to recognize object classes within large, potentially
open, set of labels. Zero-shot learning is one way of addressing these
challenges, but it has only been shown to work with limited sized class
vocabularies and typically requires separation between supervised and
unsupervised classes, allowing former to inform the latter but not vice versa.
We propose the notion of semi-supervised vocabulary-informed learning to
alleviate the above mentioned challenges and address problems of supervised,
zero-shot and open set recognition using a unified framework. Specifically, we
propose a maximum margin framework for semantic manifold-based recognition that
incorporates distance constraints from (both supervised and unsupervised)
vocabulary atoms, ensuring that labeled samples are projected closest to their
correct prototypes, in the embedding space, than to others. We show that
resulting model shows improvements in supervised, zero-shot, and large open set
recognition, with up to 310K class vocabulary on AwA and ImageNet datasets.