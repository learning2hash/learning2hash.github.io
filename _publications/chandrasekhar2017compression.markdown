---
layout: publication
title: Compression Of Deep Neural Networks For Image Instance Retrieval
authors: "Chandrasekhar Vijay, Lin Jie, Liao Qianli, Mor\xE8re Olivier, Veillard Antoine,\
  \ Duan Lingyu, Poggio Tomaso"
conference: 2017 Data Compression Conference (DCC)
year: 2017
bibkey: chandrasekhar2017compression
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.04923'}]
tags: ["Efficiency", "Image Retrieval", "Quantization", "Similarity Search"]
short_authors: Chandrasekhar et al.
---
Image instance retrieval is the problem of retrieving images from a database
which contain the same object. Convolutional Neural Network (CNN) based
descriptors are becoming the dominant approach for generating \{\it global image
descriptors\} for the instance retrieval problem. One major drawback of
CNN-based \{\it global descriptors\} is that uncompressed deep neural network
models require hundreds of megabytes of storage making them inconvenient to
deploy in mobile applications or in custom hardware. In this work, we study the
problem of neural network model compression focusing on the image instance
retrieval task. We study quantization, coding, pruning and weight sharing
techniques for reducing model size for the instance retrieval problem. We
provide extensive experimental results on the trade-off between retrieval
performance and model size for different types of networks on several data sets
providing the most comprehensive study on this topic. We compress models to the
order of a few MBs: two orders of magnitude smaller than the uncompressed
models while achieving negligible loss in retrieval performance.