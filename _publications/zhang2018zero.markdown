---
layout: publication
title: Zero-shot Kernel Learning
authors: Hongguang Zhang, Piotr Koniusz
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: zhang2018zero
citations: 107
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.01279'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Hongguang Zhang, Piotr Koniusz
---
In this paper, we address an open problem of zero-shot learning. Its
principle is based on learning a mapping that associates feature vectors
extracted from i.e. images and attribute vectors that describe objects and/or
scenes of interest. In turns, this allows classifying unseen object classes
and/or scenes by matching feature vectors via mapping to a newly defined
attribute vector describing a new class. Due to importance of such a learning
task, there exist many methods that learn semantic, probabilistic, linear or
piece-wise linear mappings. In contrast, we apply well-established kernel
methods to learn a non-linear mapping between the feature and attribute spaces.
We propose an easy learning objective inspired by the Linear Discriminant
Analysis, Kernel-Target Alignment and Kernel Polarization methods that promotes
incoherence. We evaluate performance of our algorithm on the Polynomial as well
as shift-invariant Gaussian and Cauchy kernels. Despite simplicity of our
approach, we obtain state-of-the-art results on several zero-shot learning
datasets and benchmarks including a recent AWA2 dataset.