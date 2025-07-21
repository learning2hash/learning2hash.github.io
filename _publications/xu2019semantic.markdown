---
layout: publication
title: Semantic Adversarial Network for Zero-Shot Sketch-Based Image Retrieval
authors: Xu et al.
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2019
bibkey: xu2019semantic
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.02327'}]
tags: ["Image Retrieval", "Robustness", "Few Shot & Zero Shot"]
---
Zero-shot sketch-based image retrieval (ZS-SBIR) is a specific cross-modal
retrieval task for retrieving natural images with free-hand sketches under
zero-shot scenario. Previous works mostly focus on modeling the correspondence
between images and sketches or synthesizing image features with sketch
features. However, both of them ignore the large intra-class variance of
sketches, thus resulting in unsatisfactory retrieval performance. In this
paper, we propose a novel end-to-end semantic adversarial approach for ZS-SBIR.
Specifically, we devise a semantic adversarial module to maximize the
consistency between learned semantic features and category-level word vectors.
Moreover, to preserve the discriminability of synthesized features within each
training category, a triplet loss is employed for the generative module.
Additionally, the proposed model is trained in an end-to-end strategy to
exploit better semantic features suitable for ZS-SBIR. Extensive experiments
conducted on two large-scale popular datasets demonstrate that our proposed
approach remarkably outperforms state-of-the-art approaches by more than 12%
on Sketchy dataset and about 3% on TU-Berlin dataset in the retrieval.