---
layout: publication
title: 'Less Is More: Removing Text-regions Improves CLIP Training Efficiency And
  Robustness'
authors: Liangliang Cao, Bowen Zhang, Chen Chen, Yinfei Yang, Xianzhi Du, Wencong
  Zhang, Zhiyun Lu, Yantao Zheng
conference: Arxiv
year: 2023
bibkey: cao2023less
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.05095'}]
tags: ["Datasets", "Efficiency", "Robustness"]
short_authors: Cao et al.
---
The CLIP (Contrastive Language-Image Pre-training) model and its variants are
becoming the de facto backbone in many applications. However, training a CLIP
model from hundreds of millions of image-text pairs can be prohibitively
expensive. Furthermore, the conventional CLIP model doesn't differentiate
between the visual semantics and meaning of text regions embedded in images.
This can lead to non-robustness when the text in the embedded region doesn't
match the image's visual appearance. In this paper, we discuss two effective
approaches to improve the efficiency and robustness of CLIP training: (1)
augmenting the training dataset while maintaining the same number of
optimization steps, and (2) filtering out samples that contain text regions in
the image. By doing so, we significantly improve the classification and
retrieval accuracy on public benchmarks like ImageNet and CoCo. Filtering out
images with text regions also protects the model from typographic attacks. To
verify this, we build a new dataset named ImageNet with Adversarial Text
Regions (ImageNet-Attr). Our filter-based CLIP model demonstrates a top-1
accuracy of 68.78%, outperforming previous models whose accuracy was all below
50%.