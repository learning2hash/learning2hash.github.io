---
layout: publication
title: 'Intelligent Railway Foreign Object Detection: A Semi-supervised Convolutional
  Autoencoder Based Method'
authors: Tiange Wang, Zijun Zhang, Fangfang Yang, Kwok-Leung Tsui
conference: Arxiv
year: 2021
bibkey: wang2021intelligent
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.02421'}]
tags: []
short_authors: Wang et al.
---
Automated inspection and detection of foreign objects on railways is
important for rail transportation safety as it helps prevent potential
accidents and trains derailment. Most existing vision-based approaches focus on
the detection of frontal intrusion objects with prior labels, such as
categories and locations of the objects. In reality, foreign objects with
unknown categories can appear anytime on railway tracks. In this paper, we
develop a semi-supervised convolutional autoencoder based framework that only
requires railway track images without prior knowledge on the foreign objects in
the training process. It consists of three different modules, a bottleneck
feature generator as encoder, a photographic image generator as decoder, and a
reconstruction discriminator developed via adversarial learning. In the
proposed framework, the problem of detecting the presence, location, and shape
of foreign objects is addressed by comparing the input and reconstructed images
as well as setting thresholds based on reconstruction errors. The proposed
method is evaluated through comprehensive studies under different performance
criteria. The results show that the proposed method outperforms some well-known
benchmarking methods. The proposed framework is useful for data analytics via
the train Internet-of-Things (IoT) systems