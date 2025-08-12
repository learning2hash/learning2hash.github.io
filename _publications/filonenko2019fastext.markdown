---
layout: publication
title: 'Fastext: Fast And Small Text Extractor'
authors: Alexander Filonenko, Konstantin Gudkov, Aleksei Lebedev, Nikita Orlov, Ivan
  Zagaynov
conference: 2019 International Conference on Document Analysis and Recognition Workshops
  (ICDARW)
year: 2019
bibkey: filonenko2019fastext
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08994'}]
tags: []
short_authors: Filonenko et al.
---
Text detection in natural images is a challenging but necessary task for many
applications. Existing approaches utilize large deep convolutional neural
networks making it difficult to use them in real-world tasks. We propose a
small yet relatively precise text extraction method. The basic component of it
is a convolutional neural network which works in a fully-convolutional manner
and produces results at multiple scales. Each scale output predicts whether a
pixel is a part of some word, its geometry, and its relation to neighbors at
the same scale and between scales. The key factor of reducing the complexity of
the model was the utilization of depthwise separable convolution, linear
bottlenecks, and inverted residuals. Experiments on public datasets show that
the proposed network can effectively detect text while keeping the number of
parameters in the range of 1.58 to 10.59 million in different configurations.