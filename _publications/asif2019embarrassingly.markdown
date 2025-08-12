---
layout: publication
title: An Embarrassingly Simple Approach To Neural Multiple Instance Classification
authors: Amina Asif, Fayyaz Ul Amir Afsar Minhas
conference: Pattern Recognition Letters
year: 2019
bibkey: asif2019embarrassingly
citations: 14
additional_links: [{name: Code, url: 'https://github.com/amina01/ESMIL'}, {name: Paper,
    url: 'https://arxiv.org/abs/1905.01947'}]
tags: []
short_authors: Amina Asif, Fayyaz Ul Amir Afsar Minhas
---
Multiple Instance Learning (MIL) is a weak supervision learning paradigm that
allows modeling of machine learning problems in which labels are available only
for groups of examples called bags. A positive bag may contain one or more
positive examples but it is not known which examples in the bag are positive.
All examples in a negative bag belong to the negative class. Such problems
arise frequently in fields of computer vision, medical image processing and
bioinformatics. Many neural network based solutions have been proposed in the
literature for MIL, however, almost all of them rely on introducing specialized
blocks and connectivity in the architectures. In this paper, we present a novel
and effective approach to Multiple Instance Learning in neural networks.
Instead of making changes to the architectures, we propose a simple bag-level
ranking loss function that allows Multiple Instance Classification in any
neural architecture. We have demonstrated the effectiveness of our proposed
method for popular MIL benchmark datasets. In addition, we have tested the
performance of our method in convolutional neural networks used to model an MIL
problem derived from the well-known MNIST dataset. Results have shown that
despite being simpler, our proposed scheme is comparable or better than
existing methods in the literature in practical scenarios. Python code files
for all the experiments can be found at https://github.com/amina01/ESMIL.