---
layout: publication
title: Adversarial Soft-detection-based Aggregation Network For Image Retrieval
authors: Jian Xu, Chunheng Wang, Cunzhao Shi, Baihua Xiao
conference: Arxiv
year: 2018
bibkey: xu2018adversarial
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.07619'}]
tags: [Evaluation, Supervised, Image Retrieval, Datasets, Robustness]
short_authors: Xu et al.
---
In recent year, the compact representations based on activations of
Convolutional Neural Network (CNN) achieve remarkable performance in image
retrieval. However, retrieval of some interested object that only takes up a
small part of the whole image is still a challenging problem. Therefore, it is
significant to extract the discriminative representations that contain regional
information of the pivotal small object. In this paper, we propose a novel
adversarial soft-detection-based aggregation (ASDA) method free from bounding
box annotations for image retrieval, based on adversarial detector and soft
region proposal layer. Our trainable adversarial detector generates semantic
maps based on adversarial erasing strategy to preserve more discriminative and
detailed information. Computed based on semantic maps corresponding to various
discriminative patterns and semantic contents, our soft region proposal is
arbitrary shape rather than only rectangle and it reflects the significance of
objects. The aggregation based on trainable soft region proposal highlights
discriminative semantic contents and suppresses the noise of background.
  We conduct comprehensive experiments on standard image retrieval datasets.
Our weakly supervised ASDA method achieves state-of-the-art performance on most
datasets. The results demonstrate that the proposed ASDA method is effective
for image retrieval.