---
layout: publication
title: General Multi-label Image Classification With Transformers
authors: Jack Lanchantin, Tianlu Wang, Vicente Ordonez, Yanjun Qi
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: lanchantin2020general
citations: 264
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.14027'}]
tags: ["CVPR"]
short_authors: Lanchantin et al.
---
Multi-label image classification is the task of predicting a set of labels
corresponding to objects, attributes or other entities present in an image. In
this work we propose the Classification Transformer (C-Tran), a general
framework for multi-label image classification that leverages Transformers to
exploit the complex dependencies among visual features and labels. Our approach
consists of a Transformer encoder trained to predict a set of target labels
given an input set of masked labels, and visual features from a convolutional
neural network. A key ingredient of our method is a label mask training
objective that uses a ternary encoding scheme to represent the state of the
labels as positive, negative, or unknown during training. Our model shows
state-of-the-art performance on challenging datasets such as COCO and Visual
Genome. Moreover, because our model explicitly represents the uncertainty of
labels during training, it is more general by allowing us to produce improved
results for images with partial or extra label annotations during inference. We
demonstrate this additional capability in the COCO, Visual Genome, News500, and
CUB image datasets.