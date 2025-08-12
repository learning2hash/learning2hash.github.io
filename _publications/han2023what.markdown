---
layout: publication
title: What's In A Name? Beyond Class Indices For Image Recognition
authors: Kai Han, Xiaohu Huang, Yandong Li, Sagar Vaze, Jie Li, Xuhui Jia
conference: Arxiv
year: 2023
bibkey: han2023what
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.02364'}]
tags: []
short_authors: Han et al.
---
Existing machine learning models demonstrate excellent performance in image
object recognition after training on a large-scale dataset under full
supervision. However, these models only learn to map an image to a predefined
class index, without revealing the actual semantic meaning of the object in the
image. In contrast, vision-language models like CLIP are able to assign
semantic class names to unseen objects in a 'zero-shot' manner, though they are
once again provided a pre-defined set of candidate names at test-time. In this
paper, we reconsider the recognition problem and task a vision-language model
with assigning class names to images given only a large (essentially
unconstrained) vocabulary of categories as prior information. We leverage
non-parametric methods to establish meaningful relationships between images,
allowing the model to automatically narrow down the pool of candidate names.
Our proposed approach entails iteratively clustering the data and employing a
voting mechanism to determine the most suitable class names. Additionally, we
investigate the potential of incorporating additional textual features to
enhance clustering performance. To achieve this, we employ the CLIP vision and
text encoders to retrieve relevant texts from an external database, which can
provide supplementary semantic information to inform the clustering process.
Furthermore, we tackle this problem both in unsupervised and partially
supervised settings, as well as with a coarse-grained and fine-grained search
space as the unconstrained dictionary. Remarkably, our method leads to a
roughly 50% improvement over the baseline on ImageNet in the unsupervised
setting.