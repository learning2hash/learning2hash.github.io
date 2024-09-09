---
layout: publication
title: "CNN Based Hashing for Image Retrieval"
authors: Guo Jinma, Li Jianmin
conference: Arxiv
year: 2015
bibkey: guo2015cnn
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1509.01354"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Supervised']
---
Along with data on the web increasing dramatically, hashing is becoming more and
more popular as a method of approximate nearest neighbor search. Previous
supervised hashing methods utilized similarity/dissimilarity matrix to get
semantic information. But the matrix is not easy to construct for a new dataset.
Rather than to reconstruct the matrix, we proposed a straightforward CNN-based
hashing method, i.e. binarilizing the activations of a fully connected layer
with threshold 0 and taking the binary result as hash codes. This method
achieved the best performance on CIFAR-10 and was comparable with the state-of-
the-art on MNIST. And our experiments on CIFAR-10 suggested that the signs of
activations may carry more information than the relative values of activations
between samples, and that the co-adaption between feature extractor and hash
functions is important for hashing.
