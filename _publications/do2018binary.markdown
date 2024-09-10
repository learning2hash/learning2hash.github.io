---
layout: publication
title: Binary Constrained Deep Hashing Network for Image Retrieval without Manual Annotation
authors: Do Thanh-Toan, Hoang Tuan, Tan Dang-Khoa Le, Pham Trung, Le Huu, Cheung Ngai-Man, Reid Ian
conference: "Arxiv"
year: 2018
bibkey: do2018binary
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1802.07437"}
tags: ['ARXIV', 'Deep Learning', 'Image Retrieval', 'Quantisation', 'TOM']
---
Learning compact binary codes for image retrieval task using deep neural networks has attracted increasing attention recently. However training deep hashing networks for the task is challenging due to the binary constraints on the hash codes the similarity preserving property and the requirement for a vast amount of labelled images. To the best of our knowledge none of the existing methods has tackled all of these challenges completely in a unified framework. In this work we propose a novel end-to-end deep learning approach for the task in which the network is trained to produce binary codes directly from image pixels without the need of manual annotation. In particular to deal with the non-smoothness of binary constraints we propose a novel pairwise constrained loss function which simultaneously encodes the distances between pairs of hash codes and the binary quantization error. In order to train the network with the proposed loss function we propose an efficient parameter learning algorithm. In addition to provide similar / dissimilar training images to train the network we exploit 3D models reconstructed from unlabelled images for automatic generation of enormous training image pairs. The extensive experiments on image retrieval benchmark datasets demonstrate the improvements of the proposed method over the state-of-the-art compact representation methods on the image retrieval problem.
