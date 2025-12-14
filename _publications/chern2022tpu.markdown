---
layout: publication
title: 'TPU-KNN: K Nearest Neighbor Search At Peak Flop/s'
authors: Felix Chern, Blake Hechtman, Andy Davis, Ruiqi Guo, David Majnemer, Sanjiv
  Kumar
conference: Arxiv
year: 2022
bibkey: chern2022tpu
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.14286'}]
tags: [Evaluation]
short_authors: Chern et al.
---
This paper presents a novel nearest neighbor search algorithm achieving TPU
(Google Tensor Processing Unit) peak performance, outperforming
state-of-the-art GPU algorithms with similar level of recall. The design of the
proposed algorithm is motivated by an accurate accelerator performance model
that takes into account both the memory and instruction bottlenecks. Our
algorithm comes with an analytical guarantee of recall in expectation and does
not require maintaining sophisticated index data structure or tuning, making it
suitable for applications with frequent updates. Our work is available in the
open-source package of Jax and Tensorflow on TPU.