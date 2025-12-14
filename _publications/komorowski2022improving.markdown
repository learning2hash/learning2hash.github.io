---
layout: publication
title: Improving Point Cloud Based Place Recognition With Ranking-based Loss And Large
  Batch Training
authors: Jacek Komorowski
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: komorowski2022improving
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.00972'}]
tags: [Evaluation, Image Retrieval]
short_authors: Jacek Komorowski
---
The paper presents a simple and effective learning-based method for computing
a discriminative 3D point cloud descriptor for place recognition purposes.
Recent state-of-the-art methods have relatively complex architectures such as
multi-scale oyramid of point Transformers combined with a pyramid of feature
aggregation modules. Our method uses a simple and efficient 3D convolutional
feature extraction, based on a sparse voxelized representation, enhanced with
channel attention blocks. We employ recent advances in image retrieval and
propose a modified version of a loss function based on a differentiable average
precision approximation. Such loss function requires training with very large
batches for the best results. This is enabled by using multistaged
backpropagation. Experimental evaluation on the popular benchmarks proves the
effectiveness of our approach, with a consistent improvement over the state of
the art