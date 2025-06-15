---
layout: publication
title: 'Efficient High-resolution Template Matching With Vector Quantized Nearest Neighbour Fields'
authors: Ankit Gupta, Ida-maria Sintorn
conference: "Arxiv"
year: 2023
citations: 1
bibkey: gupta2023efficient
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2306.15010'}
tags: ['Quantization', 'Quantization and Compression', 'Applications']
---
Template matching is a fundamental problem in computer vision with
applications in fields including object detection, image registration, and
object tracking. Current methods rely on nearest-neighbour (NN) matching, where
the query feature space is converted to NN space by representing each query
pixel with its NN in the template. NN-based methods have been shown to perform
better in occlusions, appearance changes, and non-rigid transformations;
however, they scale poorly with high-resolution data and high feature
dimensions. We present an NN-based method which efficiently reduces the NN
computations and introduces filtering in the NN fields (NNFs). A vector
quantization step is introduced before the NN calculation to represent the
template with \\(k\\) features, and the filter response over the NNFs is used to
compare the template and query distributions over the features. We show that
state-of-the-art performance is achieved in low-resolution data, and our method
outperforms previous methods at higher resolution.
