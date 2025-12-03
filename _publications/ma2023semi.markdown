---
layout: publication
title: Semi-supervised 3D Video Information Retrieval With Deep Neural Network And
  Bi-directional Dynamic-time Warping Algorithm
authors: Yintai Ma, Diego Klabjan
conference: 2023 IEEE International Conference on Big Data (BigData)
year: 2023
bibkey: ma2023semi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01063'}]
tags: ["Datasets", "Evaluation", "Neural Hashing", "Supervised", "Video Retrieval"]
short_authors: Yintai Ma, Diego Klabjan
---
This paper presents a novel semi-supervised deep learning algorithm for
retrieving similar 2D and 3D videos based on visual content. The proposed
approach combines the power of deep convolutional and recurrent neural networks
with dynamic time warping as a similarity measure. The proposed algorithm is
designed to handle large video datasets and retrieve the most related videos to
a given inquiry video clip based on its graphical frames and contents. We split
both the candidate and the inquiry videos into a sequence of clips and convert
each clip to a representation vector using an autoencoder-backed deep neural
network. We then calculate a similarity measure between the sequences of
embedding vectors using a bi-directional dynamic time-warping method. This
approach is tested on multiple public datasets, including CC\_WEB\_VIDEO,
Youtube-8m, S3DIS, and Synthia, and showed good results compared to
state-of-the-art. The algorithm effectively solves video retrieval tasks and
outperforms the benchmarked state-of-the-art deep learning model.