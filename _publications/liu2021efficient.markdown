---
layout: publication
title: Efficient Inference Via Universal LSH Kernel
authors: Zichang Liu, Benjamin Coleman, Anshumali Shrivastava
conference: Arxiv
year: 2021
bibkey: liu2021efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.11426'}]
tags: ["Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing", "Quantization"]
short_authors: Zichang Liu, Benjamin Coleman, Anshumali Shrivastava
---
Large machine learning models achieve unprecedented performance on various
tasks and have evolved as the go-to technique. However, deploying these compute
and memory hungry models on resource constraint environments poses new
challenges. In this work, we propose mathematically provable Representer
Sketch, a concise set of count arrays that can approximate the inference
procedure with simple hashing computations and aggregations. Representer Sketch
builds upon the popular Representer Theorem from kernel literature, hence the
name, providing a generic fundamental alternative to the problem of efficient
inference that goes beyond the popular approach such as quantization, iterative
pruning and knowledge distillation. A neural network function is transformed to
its weighted kernel density representation, which can be very efficiently
estimated with our sketching algorithm. Empirically, we show that Representer
Sketch achieves up to 114x reduction in storage requirement and 59x reduction
in computation complexity without any drop in accuracy.