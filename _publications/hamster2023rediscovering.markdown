---
layout: publication
title: 'Rediscovering Hashed Random Projections For Efficient Quantization Of Contextualized Sentence Embeddings'
authors: Ulf A. Hamster, Ji-ung Lee, Alexander Geyken, Iryna Gurevych
conference: "Arxiv"
year: 2023
citations: 0
bibkey: hamster2023rediscovering
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2304.02481'}
tags: ['Quantization', 'Quantization and Compression']
---
Training and inference on edge devices often requires an efficient setup due
to computational limitations. While pre-computing data representations and
caching them on a server can mitigate extensive edge device computation, this
leads to two challenges. First, the amount of storage required on the server
that scales linearly with the number of instances. Second, the bandwidth
required to send extensively large amounts of data to an edge device. To reduce
the memory footprint of pre-computed data representations, we propose a simple,
yet effective approach that uses randomly initialized hyperplane projections.
To further reduce their size by up to 98.96%, we quantize the resulting
floating-point representations into binary vectors. Despite the greatly reduced
size, we show that the embeddings remain effective for training models across
various English and German sentence classification tasks that retain 94%--99%
of their floating-point.
