---
layout: publication
title: Rank45;consistency Deep Hashing For Scalable Multi45;label Image Search
authors: Ma Cheng, Lu Jiwen, Zhou Jie
conference: "IEEE Transactions on Multimedia"
year: 2021
bibkey: ma2021deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2102.01486"}
tags: ['Image Retrieval', 'Unsupervised']
---
As hashing becomes an increasingly appealing technique for large45;scale image retrieval multi45;label hashing is also attracting more attention for the ability to exploit multi45;level semantic contents. In this paper we propose a novel deep hashing method for scalable multi45;label image search. Unlike existing approaches with conventional objectives such as contrast and triplet losses we employ a rank list rather than pairs or triplets to provide sufficient global supervision information for all the samples. Specifically a new rank45;consistency objective is applied to align the similarity orders from two spaces the original space and the hamming space. A powerful loss function is designed to penalize the samples whose semantic similarity and hamming distance are mismatched in two spaces. Besides a multi45;label softmax cross45;entropy loss is presented to enhance the discriminative power with a concise formulation of the derivative function. In order to manipulate the neighborhood structure of the samples with different labels we design a multi45;label clustering loss to cluster the hashing vectors of the samples with the same labels by reducing the distances between the samples and their multiple corresponding class centers. The state45;of45;the45;art experimental results achieved on three public multi45;label datasets MIRFLICKR45;25K IAPRTC12 and NUS45;WIDE demonstrate the effectiveness of the proposed method.
