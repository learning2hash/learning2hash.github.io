---
layout: publication
title: Impostor Networks For Fast Fine-grained Recognition
authors: Vadim Lebedev, Artem Babenko, Victor Lempitsky
conference: Arxiv
year: 2018
bibkey: lebedev2018impostor
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.05217'}]
tags: []
short_authors: Vadim Lebedev, Artem Babenko, Victor Lempitsky
---
In this work we introduce impostor networks, an architecture that allows to
perform fine-grained recognition with high accuracy and using a light-weight
convolutional network, making it particularly suitable for fine-grained
applications on low-power and non-GPU enabled platforms. Impostor networks
compensate for the lightness of its `backend' network by combining it with a
lightweight non-parametric classifier. The combination of a convolutional
network and such non-parametric classifier is trained in an end-to-end fashion.
Similarly to convolutional neural networks, impostor networks can fit
large-scale training datasets very well, while also being able to generalize to
new data points. At the same time, the bulk of computations within impostor
networks happen through nearest neighbor search in high-dimensions. Such search
can be performed efficiently on a variety of architectures including standard
CPUs, where deep convolutional networks are inefficient. In a series of
experiments with three fine-grained datasets, we show that impostor networks
are able to boost the classification accuracy of a moderate-sized convolutional
network considerably at a very small computational cost.