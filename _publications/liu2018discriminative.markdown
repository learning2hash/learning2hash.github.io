---
layout: publication
title: Discriminative Cross45;view Binary Representation Learning
authors: Liu Liu, Qi Hairong
conference: "WACV"
year: 2018
bibkey: liu2018discriminative
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1804.01233"}
tags: ['CNN', 'Image Retrieval', 'Quantisation', 'Supervised']
---
Learning compact representation is vital and challenging for large scale multimedia data. Cross45;view/cross45;modal hashing for effective binary representation learning has received significant attention with exponentially growing availability of multimedia content. Most existing cross45;view hashing algorithms emphasize the similarities in individual views which are then connected via cross45;view similarities. In this work we focus on the exploitation of the discriminative information from different views and propose an end45;to45;end method to learn semantic45;preserving and discriminative binary representation dubbed Discriminative Cross45;View Hashing (DCVH) in light of learning multitasking binary representation for various tasks including cross45;view retrieval image45;to45;image retrieval and image annotation/tagging. The proposed DCVH has the following key components. First it uses convolutional neural network (CNN) based nonlinear hashing functions and multilabel classification for both images and texts simultaneously. Such hashing functions achieve effective continuous relaxation during training without explicit quantization loss by using Direct Binary Embedding (DBE) layers. Second we propose an effective view alignment via Hamming distance minimization which is efficiently accomplished by bit45;wise XOR operation. Extensive experiments on two image45;text benchmark datasets demonstrate that DCVH outperforms state45;of45;the45;art cross45;view hashing algorithms as well as single45;view image hashing algorithms. In addition DCVH can provide competitive performance for image annotation/tagging.
