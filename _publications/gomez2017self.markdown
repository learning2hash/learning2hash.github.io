---
layout: publication
title: Self-supervised Learning Of Visual Features Through Embedding Images Into Text
  Topic Spaces
authors: "Lluis Gomez, Yash Patel, Mar\xE7al Rusi\xF1ol, Dimosthenis Karatzas, C.\
  \ V. Jawahar"
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: gomez2017self
citations: 96
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.08631'}]
tags: ["CVPR", "Datasets", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: Gomez et al.
---
End-to-end training from scratch of current deep architectures for new
computer vision problems would require Imagenet-scale datasets, and this is not
always possible. In this paper we present a method that is able to take
advantage of freely available multi-modal content to train computer vision
algorithms without human supervision. We put forward the idea of performing
self-supervised learning of visual features by mining a large scale corpus of
multi-modal (text and image) documents. We show that discriminative visual
features can be learnt efficiently by training a CNN to predict the semantic
context in which a particular image is more probable to appear as an
illustration. For this we leverage the hidden semantic structures discovered in
the text corpus with a well-known topic modeling technique. Our experiments
demonstrate state of the art performance in image classification, object
detection, and multi-modal retrieval compared to recent self-supervised or
natural-supervised approaches.