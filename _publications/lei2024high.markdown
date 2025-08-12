---
layout: publication
title: High-discriminative Attribute Feature Learning For Generalized Zero-shot Learning
authors: Yu Lei, Guoshuai Sheng, Fangfang Li, Quanxue Gao, Cheng Deng, Qin Li
conference: Arxiv
year: 2024
bibkey: lei2024high
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.04953'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Lei et al.
---
Zero-shot learning(ZSL) aims to recognize new classes without prior exposure
to their samples, relying on semantic knowledge from observed classes. However,
current attention-based models may overlook the transferability of visual
features and the distinctiveness of attribute localization when learning
regional features in images. Additionally, they often overlook shared
attributes among different objects. Highly discriminative attribute features
are crucial for identifying and distinguishing unseen classes. To address these
issues, we propose an innovative approach called High-Discriminative Attribute
Feature Learning for Generalized Zero-Shot Learning (HDAFL). HDAFL optimizes
visual features by learning attribute features to obtain discriminative visual
embeddings. Specifically, HDAFL utilizes multiple convolutional kernels to
automatically learn discriminative regions highly correlated with attributes in
images, eliminating irrelevant interference in image features. Furthermore, we
introduce a Transformer-based attribute discrimination encoder to enhance the
discriminative capability among attributes. Simultaneously, the method employs
contrastive loss to alleviate dataset biases and enhance the transferability of
visual features, facilitating better semantic transfer between seen and unseen
classes. Experimental results demonstrate the effectiveness of HDAFL across
three widely used datasets.