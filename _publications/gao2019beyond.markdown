---
layout: publication
title: 'Beyond Product Quantization: Deep Progressive Quantization For Image Retrieval'
authors: Lianli Gao, Xiaosu Zhu, Jingkuan Song, Zhou Zhao, Heng Tao Shen
conference: "Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence 1 (2019) 723-729"
year: 2019
citations: 23
bibkey: gao2019beyond
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1906.06698'}
  - {name: "Code", url: 'https://github.com/cfm-uestc/DPQ'}
tags: ['Applications', 'Evaluation Metrics', 'Quantization and Compression', 'Tools and Libraries', 'ANN Search', 'Benchmarks and Datasets', 'Quantization', 'Has Code']
---
Product Quantization (PQ) has long been a mainstream for generating an
exponentially large codebook at very low memory/time cost. Despite its success,
PQ is still tricky for the decomposition of high-dimensional vector space, and
the retraining of model is usually unavoidable when the code length changes. In
this work, we propose a deep progressive quantization (DPQ) model, as an
alternative to PQ, for large scale image retrieval. DPQ learns the quantization
codes sequentially and approximates the original feature space progressively.
Therefore, we can train the quantization codes with different code lengths
simultaneously. Specifically, we first utilize the label information for
guiding the learning of visual features, and then apply several quantization
blocks to progressively approach the visual features. Each quantization block
is designed to be a layer of a convolutional neural network, and the whole
framework can be trained in an end-to-end manner. Experimental results on the
benchmark datasets show that our model significantly outperforms the
state-of-the-art for image retrieval. Our model is trained once for different
code lengths and therefore requires less computation time. Additional ablation
study demonstrates the effect of each component of our proposed model. Our code
is released at https://github.com/cfm-uestc/DPQ.
