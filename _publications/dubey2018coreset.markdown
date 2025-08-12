---
layout: publication
title: Coreset-based Neural Network Compression
authors: Abhimanyu Dubey, Moitreya Chatterjee, Narendra Ahuja
conference: Lecture Notes in Computer Science
year: 2018
bibkey: dubey2018coreset
citations: 79
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.09810'}]
tags: []
short_authors: Abhimanyu Dubey, Moitreya Chatterjee, Narendra Ahuja
---
We propose a novel Convolutional Neural Network (CNN) compression algorithm
based on coreset representations of filters. We exploit the redundancies extant
in the space of CNN weights and neuronal activations (across samples) in order
to obtain compression. Our method requires no retraining, is easy to implement,
and obtains state-of-the-art compression performance across a wide variety of
CNN architectures. Coupled with quantization and Huffman coding, we create
networks that provide AlexNet-like accuracy, with a memory footprint that is
\(832\times\) smaller than the original AlexNet, while also introducing
significant reductions in inference time as well. Additionally these compressed
networks when fine-tuned, successfully generalize to other domains as well.