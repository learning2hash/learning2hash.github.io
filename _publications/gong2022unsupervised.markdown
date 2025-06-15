---
layout: publication
title: 'Vit2hash: Unsupervised Information-preserving Hashing'
authors: Qinkang Gong, Liangdao Wang, Hanjiang Lai, Yan Pan, Jian Yin
conference: "Arxiv"
year: 2022
citations: 1
bibkey: gong2022unsupervised
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2201.05541'}
tags: ['Hashing Methods', 'Evaluation Metrics', 'Supervision Type', 'Supervision Types', 'Quantization and Compression', 'Tools and Libraries', 'Hashing Fundamentals', 'Quantization']
---
Unsupervised image hashing, which maps images into binary codes without
supervision, is a compressor with a high compression rate. Hence, how to
preserving meaningful information of the original data is a critical problem.
Inspired by the large-scale vision pre-training model, known as ViT, which has
shown significant progress for learning visual representations, in this paper,
we propose a simple information-preserving compressor to finetune the ViT model
for the target unsupervised hashing task. Specifically, from pixels to
continuous features, we first propose a feature-preserving module, using the
corrupted image as input to reconstruct the original feature from the
pre-trained ViT model and the complete image, so that the feature extractor can
focus on preserving the meaningful information of original data. Secondly, from
continuous features to hash codes, we propose a hashing-preserving module,
which aims to keep the semantic information from the pre-trained ViT model by
using the proposed Kullback-Leibler divergence loss. Besides, the quantization
loss and the similarity loss are added to minimize the quantization error. Our
method is very simple and achieves a significantly higher degree of MAP on
three benchmark image datasets.
