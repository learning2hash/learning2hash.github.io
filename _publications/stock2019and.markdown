---
layout: publication
title: 'And The Bit Goes Down: Revisiting The Quantization Of Neural Networks'
authors: "Pierre Stock, Armand Joulin, R\xE9mi Gribonval, Benjamin Graham, Herv\xE9\
  \ J\xE9gou"
conference: Arxiv
year: 2019
bibkey: stock2019and
citations: 68
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.05686'}]
tags: ["Memory Efficiency", "Quantization"]
short_authors: Stock et al.
---
In this paper, we address the problem of reducing the memory footprint of
convolutional network architectures. We introduce a vector quantization method
that aims at preserving the quality of the reconstruction of the network
outputs rather than its weights. The principle of our approach is that it
minimizes the loss reconstruction error for in-domain inputs. Our method only
requires a set of unlabelled data at quantization time and allows for efficient
inference on CPU by using byte-aligned codebooks to store the compressed
weights. We validate our approach by quantizing a high performing ResNet-50
model to a memory size of 5MB (20x compression factor) while preserving a top-1
accuracy of 76.1% on ImageNet object classification and by compressing a Mask
R-CNN with a 26x factor.