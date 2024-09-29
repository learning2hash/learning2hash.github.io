---
layout: publication
title: Deep Spherical Quantization For Image Search
authors: Eghbali Sepehr, Tahvildari Ladan
conference: "Arxiv"
year: 2019
bibkey: eghbali2019deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1906.02865"}
tags: ['ARXIV', 'Image Retrieval', 'Quantisation', 'Supervised']
---
Hashing methods which encode high45;dimensional images with compact discrete codes have been widely applied to enhance large45;scale image retrieval. In this paper we put forward Deep Spherical Quantization (DSQ) a novel method to make deep convolutional neural networks generate supervised and compact binary codes for efficient image search. Our approach simultaneously learns a mapping that transforms the input images into a low45;dimensional discriminative space and quantizes the transformed data points using multi45;codebook quantization. To eliminate the negative effect of norm variance on codebook learning we force the network to L95;2 normalize the extracted features and then quantize the resulting vectors using a new supervised quantization technique specifically designed for points lying on a unit hypersphere. Furthermore we introduce an easy45;to45;implement extension of our quantization technique that enforces sparsity on the codebooks. Extensive experiments demonstrate that DSQ and its sparse variant can generate semantically separable compact binary codes outperforming many state45;of45;the45;art image retrieval methods on three benchmarks.
