---
layout: publication
title: 'Deepkspd: Learning Kernel-matrix-based SPD Representation For Fine-grained
  Image Recognition'
authors: Melih Engin, Lei Wang, Luping Zhou, Xinwang Liu
conference: Lecture Notes in Computer Science
year: 2018
bibkey: engin2017deepkspd
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.04047'}]
tags: []
short_authors: Engin et al.
---
Being symmetric positive-definite (SPD), covariance matrix has traditionally
been used to represent a set of local descriptors in visual recognition. Recent
study shows that kernel matrix can give considerably better representation by
modelling the nonlinearity in the local descriptor set. Nevertheless, neither
the descriptors nor the kernel matrix is deeply learned. Worse, they are
considered separately, hindering the pursuit of an optimal SPD representation.
This work proposes a deep network that jointly learns local descriptors,
kernel-matrix-based SPD representation, and the classifier via an end-to-end
training process. We derive the derivatives for the mapping from a local
descriptor set to the SPD representation to carry out backpropagation. Also, we
exploit the Daleckii-Krein formula in operator theory to give a concise and
unified result on differentiating SPD matrix functions, including the matrix
logarithm to handle the Riemannian geometry of kernel matrix. Experiments not
only show the superiority of kernel-matrix-based SPD representation with deep
local descriptors, but also verify the advantage of the proposed deep network
in pursuing better SPD representations for fine-grained image recognition
tasks.