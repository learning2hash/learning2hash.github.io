---
layout: publication
title: Unsupervised Learning Of Visual Representations By Solving Jigsaw Puzzles
authors: Mehdi Noroozi, Paolo Favaro
conference: Lecture Notes in Computer Science
year: 2016
bibkey: noroozi2016unsupervised
citations: 2731
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.09246'}]
tags: ["Unsupervised"]
short_authors: Mehdi Noroozi, Paolo Favaro
---
In this paper we study the problem of image representation learning without
human annotation. By following the principles of self-supervision, we build a
convolutional neural network (CNN) that can be trained to solve Jigsaw puzzles
as a pretext task, which requires no manual labeling, and then later repurposed
to solve object classification and detection. To maintain the compatibility
across tasks we introduce the context-free network (CFN), a siamese-ennead CNN.
The CFN takes image tiles as input and explicitly limits the receptive field
(or context) of its early processing units to one tile at a time. We show that
the CFN includes fewer parameters than AlexNet while preserving the same
semantic learning capabilities. By training the CFN to solve Jigsaw puzzles, we
learn both a feature mapping of object parts as well as their correct spatial
arrangement. Our experimental evaluations show that the learned features
capture semantically relevant content. Our proposed method for learning visual
representations outperforms state of the art methods in several transfer
learning benchmarks.