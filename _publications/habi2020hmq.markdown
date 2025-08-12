---
layout: publication
title: 'HMQ: Hardware Friendly Mixed Precision Quantization Block For Cnns'
authors: Hai Victor Habi, Roy H. Jennings, Arnon Netzer
conference: Lecture Notes in Computer Science
year: 2020
bibkey: habi2020hmq
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.09952'}]
tags: ["Quantization"]
short_authors: Hai Victor Habi, Roy H. Jennings, Arnon Netzer
---
Recent work in network quantization produced state-of-the-art results using
mixed precision quantization. An imperative requirement for many efficient edge
device hardware implementations is that their quantizers are uniform and with
power-of-two thresholds. In this work, we introduce the Hardware Friendly Mixed
Precision Quantization Block (HMQ) in order to meet this requirement. The HMQ
is a mixed precision quantization block that repurposes the Gumbel-Softmax
estimator into a smooth estimator of a pair of quantization parameters, namely,
bit-width and threshold. HMQs use this to search over a finite space of
quantization schemes. Empirically, we apply HMQs to quantize classification
models trained on CIFAR10 and ImageNet. For ImageNet, we quantize four
different architectures and show that, in spite of the added restrictions to
our quantization scheme, we achieve competitive and, in some cases,
state-of-the-art results.