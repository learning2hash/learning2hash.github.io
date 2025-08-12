---
layout: publication
title: 'A Strong Inductive Bias: Gzip For Binary Image Classification'
authors: Marco Scilipoti, Marina Fuster, Rodrigo Ramele
conference: Arxiv
year: 2024
bibkey: scilipoti2024strong
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.07392'}]
tags: []
short_authors: Marco Scilipoti, Marina Fuster, Rodrigo Ramele
---
Deep learning networks have become the de-facto standard in Computer Vision
for industry and research. However, recent developments in their cousin,
Natural Language Processing (NLP), have shown that there are areas where
parameter-less models with strong inductive biases can serve as computationally
cheaper and simpler alternatives. We propose such a model for binary image
classification: a nearest neighbor classifier combined with a general purpose
compressor like Gzip. We test and compare it against popular deep learning
networks like Resnet, EfficientNet and Mobilenet and show that it achieves
better accuracy and utilizes significantly less space, more than two order of
magnitude, within a few-shot setting. As a result, we believe that this
underlines the untapped potential of models with stronger inductive biases in
few-shot scenarios.