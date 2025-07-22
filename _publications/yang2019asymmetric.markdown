---
layout: publication
title: Asymmetric Deep Semantic Quantization for Image Retrieval
authors: Yang et al.
conference: IEEE Access
year: 2019
bibkey: yang2019asymmetric
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.12493'}]
tags: ["Quantization", "Image-Retrieval"]
---
Due to its fast retrieval and storage efficiency capabilities, hashing has
been widely used in nearest neighbor retrieval tasks. By using deep learning
based techniques, hashing can outperform non-learning based hashing technique
in many applications. However, we argue that the current deep learning based
hashing methods ignore some critical problems (e.g., the learned hash codes are
not discriminative due to the hashing methods being unable to discover rich
semantic information and the training strategy having difficulty optimizing the
discrete binary codes). In this paper, we propose a novel image hashing method,
termed as \textbf\{\underline\{A\}\}symmetric \textbf\{\underline\{D\}\}eep
\textbf\{\underline\{S\}\}emantic \textbf\{\underline\{Q\}\}uantization
(\textbf\{ADSQ\}). \textbf\{ADSQ\} is implemented using three stream frameworks,
which consist of one *LabelNet* and two *ImgNets*. The
*LabelNet* leverages the power of three fully-connected layers, which are
used to capture rich semantic information between image pairs. For the two
*ImgNets*, they each adopt the same convolutional neural network
structure, but with different weights (i.e., asymmetric convolutional neural
networks). The two *ImgNets* are used to generate discriminative compact
hash codes. Specifically, the function of the *LabelNet* is to capture
rich semantic information that is used to guide the two *ImgNets* in
minimizing the gap between the real-continuous features and the discrete binary
codes. Furthermore, \textbf\{ADSQ\} can utilize the most critical semantic
information to guide the feature learning process and consider the consistency
of the common semantic space and Hamming space. Experimental results on three
benchmarks (i.e., CIFAR-10, NUS-WIDE, and ImageNet) demonstrate that the
proposed \textbf\{ADSQ\} can outperforms current state-of-the-art methods.