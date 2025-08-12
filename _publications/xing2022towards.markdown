---
layout: publication
title: Towards Accurate Binary Neural Networks Via Modeling Contextual Dependencies
authors: Xingrun Xing, Yangguang Li, Wei Li, Wenrui Ding, Yalong Jiang, Yufeng Wang,
  Jing Shao, Chunlei Liu, Xianglong Liu
conference: Lecture Notes in Computer Science
year: 2022
bibkey: xing2022towards
citations: 4
additional_links: [{name: Code, url: 'https://github.com/Sense-GVT/BCDN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2209.01404'}]
tags: ["Evaluation", "Robustness"]
short_authors: Xing et al.
---
Existing Binary Neural Networks (BNNs) mainly operate on local convolutions
with binarization function. However, such simple bit operations lack the
ability of modeling contextual dependencies, which is critical for learning
discriminative deep representations in vision models. In this work, we tackle
this issue by presenting new designs of binary neural modules, which enables
BNNs to learn effective contextual dependencies. First, we propose a binary
multi-layer perceptron (MLP) block as an alternative to binary convolution
blocks to directly model contextual dependencies. Both short-range and
long-range feature dependencies are modeled by binary MLPs, where the former
provides local inductive bias and the latter breaks limited receptive field in
binary convolutions. Second, to improve the robustness of binary models with
contextual dependencies, we compute the contextual dynamic embeddings to
determine the binarization thresholds in general binary convolutional blocks.
Armed with our binary MLP blocks and improved binary convolution, we build the
BNNs with explicit Contextual Dependency modeling, termed as BCDNet. On the
standard ImageNet-1K classification benchmark, the BCDNet achieves 72.3% Top-1
accuracy and outperforms leading binary methods by a large margin. In
particular, the proposed BCDNet exceeds the state-of-the-art ReActNet-A by 2.9%
Top-1 accuracy with similar operations. Our code is available at
https://github.com/Sense-GVT/BCDN