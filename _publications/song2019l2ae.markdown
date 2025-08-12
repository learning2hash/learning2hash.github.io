---
layout: publication
title: 'L2AE-D: Learning To Aggregate Embeddings For Few-shot Learning With Meta-level
  Dropout'
authors: "Heda Song, Mercedes Torres Torres, Ender \xD6zcan, Isaac Triguero"
conference: Neurocomputing
year: 2021
bibkey: song2019l2ae
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.04339'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Song et al.
---
Few-shot learning focuses on learning a new visual concept with very limited
labelled examples. A successful approach to tackle this problem is to compare
the similarity between examples in a learned metric space based on
convolutional neural networks. However, existing methods typically suffer from
meta-level overfitting due to the limited amount of training tasks and do not
normally consider the importance of the convolutional features of different
examples within the same channel. To address these limitations, we make the
following two contributions: (a) We propose a novel meta-learning approach for
aggregating useful convolutional features and suppressing noisy ones based on a
channel-wise attention mechanism to improve class representations. The proposed
model does not require fine-tuning and can be trained in an end-to-end manner.
The main novelty lies in incorporating a shared weight generation module that
learns to assign different weights to the feature maps of different examples
within the same channel. (b) We also introduce a simple meta-level dropout
technique that reduces meta-level overfitting in several few-shot learning
approaches. In our experiments, we find that this simple technique
significantly improves the performance of the proposed method as well as
various state-of-the-art meta-learning algorithms. Applying our method to
few-shot image recognition using Omniglot and miniImageNet datasets shows that
it is capable of delivering a state-of-the-art classification performance.