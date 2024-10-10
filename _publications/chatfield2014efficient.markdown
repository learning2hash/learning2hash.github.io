---
layout: publication
title: Efficient On-the-fly Category Retrieval Using Convnets And Gpus
authors: Chatfield Ken, Simonyan Karen, Zisserman Andrew
conference: "Arxiv"
year: 2014
bibkey: chatfield2014efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1407.4764"}
tags: ['ARXIV', 'Quantisation', 'Supervised']
---
We investigate the gains in precision and speed that can be obtained by using Convolutional Networks (ConvNets) for on-the-fly retrieval - where classifiers are learnt at run time for a textual query from downloaded images and used to rank large image or video datasets. We make three contributions (i) we present an evaluation of state-of-the-art image representations for object category retrieval over standard benchmark datasets containing 1M+ images; (ii) we show that ConvNets can be used to obtain features which are incredibly performant and yet much lower dimensional than previous state-of-the-art image representations and that their dimensionality can be reduced further without loss in performance by compression using product quantization or binarization. Consequently features with the state-of-the-art performance on large-scale datasets of millions of images can fit in the memory of even a commodity GPU card; (iii) we show that an SVM classifier can be learnt within a ConvNet framework on a GPU in parallel with downloading the new training images allowing for a continuous refinement of the model as more images become available and simultaneous training and ranking. The outcome is an on-the-fly system that significantly outperforms its predecessors in terms of precision of retrieval memory requirements and speed facilitating accurate on-the-fly learning and ranking in under a second on a single GPU.
