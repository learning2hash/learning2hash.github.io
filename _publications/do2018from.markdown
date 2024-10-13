---
layout: publication
title: From Selective Deep Convolutional Features To Compact Binary Representations For Image Retrieval
authors: Do Thanh-toan, Hoang Tuan, Tan Dang-khoa Le, Le Huu, Nguyen Tam V., Cheung Ngai-man
conference: "Arxiv"
year: 2018
bibkey: do2018from
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1802.02899"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Supervised']
---
In the large-scale image retrieval task, the two most important requirements
are the discriminability of image representations and the efficiency in
computation and storage of representations. Regarding the former requirement,
Convolutional Neural Network (CNN) is proven to be a very powerful tool to
extract highly discriminative local descriptors for effective image search.
Additionally, in order to further improve the discriminative power of the
descriptors, recent works adopt fine-tuned strategies. In this paper, taking a
different approach, we propose a novel, computationally efficient, and
competitive framework. Specifically, we firstly propose various strategies to
compute masks, namely SIFT-mask, SUM-mask, and MAX-mask, to select a
representative subset of local convolutional features and eliminate redundant
features. Our in-depth analyses demonstrate that proposed masking schemes are
effective to address the burstiness drawback and improve retrieval accuracy.
Secondly, we propose to employ recent embedding and aggregating methods which
can significantly boost the feature discriminability. Regarding the computation
and storage efficiency, we include a hashing module to produce very compact
binary image representations. Extensive experiments on six image retrieval
benchmarks demonstrate that our proposed framework achieves the
state-of-the-art retrieval performances.
