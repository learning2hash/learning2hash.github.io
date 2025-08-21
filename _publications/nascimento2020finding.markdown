---
layout: publication
title: Finding Non-uniform Quantization Schemes Using Multi-task Gaussian Processes
authors: Marcelo Gennari Do Nascimento, Theo W. Costain, Victor Adrian Prisacariu
conference: Lecture Notes in Computer Science
year: 2020
bibkey: nascimento2020finding
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.07743'}]
tags: ["Datasets", "Evaluation", "Quantization"]
short_authors: Marcelo Gennari Do Nascimento, Theo W. Costain, Victor Adrian Prisacariu
---
We propose a novel method for neural network quantization that casts the
neural architecture search problem as one of hyperparameter search to find
non-uniform bit distributions throughout the layers of a CNN. We perform the
search assuming a Multi-Task Gaussian Processes prior, which splits the problem
to multiple tasks, each corresponding to different number of training epochs,
and explore the space by sampling those configurations that yield maximum
information. We then show that with significantly lower precision in the last
layers we achieve a minimal loss of accuracy with appreciable memory savings.
We test our findings on the CIFAR10 and ImageNet datasets using the VGG, ResNet
and GoogLeNet architectures.