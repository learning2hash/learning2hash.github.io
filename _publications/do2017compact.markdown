---
layout: publication
title: 'Compact Hash Code Learning With Binary Deep Neural Network'
authors: Thanh-toan Do, Tuan Hoang, Dang-khoa Le Tan, Anh-dzung Doan, Ngai-man Cheung
conference: "Arxiv"
year: 2017
citations: 14
bibkey: do2017compact
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1712.02956'}
tags: ['Cross-Modal', 'Deep', 'Independent', 'Retrieval Models', 'Datasets', 'Vector Indexing', 'Training Strategy', 'Hashing', 'Applications']
---
Learning compact binary codes for image retrieval problem using deep neural
networks has recently attracted increasing attention. However, training deep
hashing networks is challenging due to the binary constraints on the hash
codes. In this paper, we propose deep network models and learning algorithms
for learning binary hash codes given image representations under both
unsupervised and supervised manners. The novelty of our network design is that
we constrain one hidden layer to directly output the binary codes. This design
has overcome a challenging problem in some previous works: optimizing
non-smooth objective functions because of binarization. In addition, we propose
to incorporate independence and balance properties in the direct and strict
forms into the learning schemes. We also include a similarity preserving
property in our objective functions. The resulting optimizations involving
these binary, independence, and balance constraints are difficult to solve. To
tackle this difficulty, we propose to learn the networks with alternating
optimization and careful relaxation. Furthermore, by leveraging the powerful
capacity of convolutional neural networks, we propose an end-to-end
architecture that jointly learns to extract visual features and produce binary
hash codes. Experimental results for the benchmark datasets show that the
proposed methods compare favorably or outperform the state of the art.
