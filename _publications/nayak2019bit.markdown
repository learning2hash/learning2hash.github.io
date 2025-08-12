---
layout: publication
title: Bit Efficient Quantization For Deep Neural Networks
authors: Prateeth Nayak, David Zhang, Sek Chai
conference: 2019 Fifth Workshop on Energy Efficient Machine Learning and Cognitive
  Computing - NeurIPS Edition (EMC2-NIPS)
year: 2019
bibkey: nayak2019bit
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.04877'}]
tags: ["Quantization"]
short_authors: Prateeth Nayak, David Zhang, Sek Chai
---
Quantization for deep neural networks have afforded models for edge devices
that use less on-board memory and enable efficient low-power inference. In this
paper, we present a comparison of model-parameter driven quantization
approaches that can achieve as low as 3-bit precision without affecting
accuracy. The post-training quantization approaches are data-free, and the
resulting weight values are closely tied to the dataset distribution on which
the model has converged to optimality. We show quantization results for a
number of state-of-art deep neural networks (DNN) using large dataset like
ImageNet. To better analyze quantization results, we describe the overall range
and local sparsity of values afforded through various quantization schemes. We
show the methods to lower bit-precision beyond quantization limits with object
class clustering.