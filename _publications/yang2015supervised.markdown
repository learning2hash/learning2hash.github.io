---
layout: publication
title: Supervised Learning of Semantics-Preserving Hash via Deep Convolutional Neural Networks
authors: Yang Huei-Fang, Lin Kevin, Chen Chu-Song
conference: "Arxiv"
year: 2015
bibkey: yang2015supervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.00101"}
tags: ['ARXIV', 'Supervised', 'Unsupervised']
---
This paper presents a simple yet effective supervised deep hash approach that constructs binary hash codes from labeled data for large-scale image search. We assume that the semantic labels are governed by several latent attributes with each attribute on or off, and classification relies on these attributes. Based on this assumption, our approach, dubbed supervised semantics-preserving deep hashing (SSDH), constructs hash functions as a latent layer in a deep network and the binary codes are learned by minimizing an objective function defined over classification error and other desirable hash codes properties. With this design, SSDH has a nice characteristic that classification and retrieval are unified in a single learning model. Moreover, SSDH performs joint learning of image representations, hash codes, and classification in a point-wised manner, and thus is scalable to large-scale datasets. SSDH is simple and can be realized by a slight enhancement of an existing deep architecture for classification; yet it is effective and outperforms other hashing approaches on several benchmarks and large datasets. Compared with state-of-the-art approaches, SSDH achieves higher retrieval accuracy, while the classification performance is not sacrificed.
