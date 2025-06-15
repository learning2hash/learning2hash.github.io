---
layout: publication
title: 'Pixel Embedding: Fully Quantized Convolutional Neural Network With Differentiable Lookup Table'
authors: Hiroyuki Tokunaga, Joel Nicholls, Daria Vazhenina, Atsunori Kanemura
conference: "Arxiv"
year: 2024
citations: 0
bibkey: tokunaga2024pixel
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2407.16174'}
tags: ['Evaluation and Benchmarks', 'Evaluation Metrics', 'Efficient Learning', 'Quantization and Compression', 'Tools and Libraries', 'Benchmarks and Datasets', 'Quantization']
---
By quantizing network weights and activations to low bitwidth, we can obtain
hardware-friendly and energy-efficient networks. However, existing quantization
techniques utilizing the straight-through estimator and piecewise constant
functions face the issue of how to represent originally high-bit input data
with low-bit values. To fully quantize deep neural networks, we propose pixel
embedding, which replaces each float-valued input pixel with a vector of
quantized values by using a lookup table. The lookup table or low-bit
representation of pixels is differentiable and trainable by backpropagation.
Such replacement of inputs with vectors is similar to word embedding in the
natural language processing field. Experiments on ImageNet and CIFAR-100 show
that pixel embedding reduces the top-5 error gap caused by quantizing the
floating points at the first layer to only 1% for the ImageNet dataset, and the
top-1 error gap caused by quantizing first and last layers to slightly over 1%
for the CIFAR-100 dataset. The usefulness of pixel embedding is further
demonstrated by inference time measurements, which demonstrate over 1.7 times
speedup compared to floating point precision first layer.
