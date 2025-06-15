---
layout: publication
title: 'Discriminative Cross-view Binary Representation Learning'
authors: Liu Liu, Hairong Qi
conference: "WACV2018"
year: 2018
citations: 4
bibkey: liu2018discriminative
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1804.01233'}
tags: ['Hashing Methods', 'Loss Functions', 'Applications', 'Evaluation Metrics', 'Modality-Specific Hashing', 'Quantization and Compression', 'Hashing Fundamentals', 'ANN Search', 'Tools and Libraries', 'Benchmarks and Datasets', 'Learning Strategies', 'Quantization', 'Multi-Modal Hashing']
---
Learning compact representation is vital and challenging for large scale
multimedia data. Cross-view/cross-modal hashing for effective binary
representation learning has received significant attention with exponentially
growing availability of multimedia content. Most existing cross-view hashing
algorithms emphasize the similarities in individual views, which are then
connected via cross-view similarities. In this work, we focus on the
exploitation of the discriminative information from different views, and
propose an end-to-end method to learn semantic-preserving and discriminative
binary representation, dubbed Discriminative Cross-View Hashing (DCVH), in
light of learning multitasking binary representation for various tasks
including cross-view retrieval, image-to-image retrieval, and image
annotation/tagging. The proposed DCVH has the following key components. First,
it uses convolutional neural network (CNN) based nonlinear hashing functions
and multilabel classification for both images and texts simultaneously. Such
hashing functions achieve effective continuous relaxation during training
without explicit quantization loss by using Direct Binary Embedding (DBE)
layers. Second, we propose an effective view alignment via Hamming distance
minimization, which is efficiently accomplished by bit-wise XOR operation.
Extensive experiments on two image-text benchmark datasets demonstrate that
DCVH outperforms state-of-the-art cross-view hashing algorithms as well as
single-view image hashing algorithms. In addition, DCVH can provide competitive
performance for image annotation/tagging.
