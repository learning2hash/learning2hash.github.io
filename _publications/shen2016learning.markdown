---
layout: publication
title: Learning Binary Codes and Binary Weights for Efficient Classification
authors: Shen Fumin, Mu Yadong, Liu Wei, Yang Yang, Shen Heng Tao
conference: "Arxiv"
year: 2016
bibkey: shen2016learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1603.04116"}
tags: ['ARXIV']
---
This paper proposes a generic formulation that significantly expedites the training and deployment of image classification models, particularly under the scenarios of many image categories and high feature dimensions. As a defining property, our method represents both the images and learned classifiers using binary hash codes, which are simultaneously learned from the training data. Classifying an image thereby reduces to computing the Hamming distance between the binary codes of the image and classifiers and selecting the class with minimal Hamming distance. Conventionally, compact hash codes are primarily used for accelerating image search. Our work is first of its kind to represent classifiers using binary codes. Specifically, we formulate multi-class image classification as an optimization problem over binary variables. The optimization alternatively proceeds over the binary classifiers and image hash codes. Profiting from the special property of binary codes, we show that the sub-problems can be efficiently solved through either a binary quadratic program (BQP) or linear program. In particular, for attacking the BQP problem, we propose a novel bit-flipping procedure which enjoys high efficacy and local optimality guarantee. Our formulation supports a large family of empirical loss functions and is here instantiated by exponential / hinge losses. Comprehensive evaluations are conducted on several representative image benchmarks. The experiments consistently observe reduced complexities of model training and deployment, without sacrifice of accuracies.
