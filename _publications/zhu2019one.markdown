---
layout: publication
title: One-shot Texture Retrieval With Global Context Metric
authors: Kai Zhu, Wei Zhai, Zheng-Jun Zha, Yang Cao
conference: Proceedings of the Twenty-Eighth International Joint Conference on Artificial
  Intelligence
year: 2019
bibkey: zhu2019one
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.06656'}]
tags: ["IJCAI"]
short_authors: Zhu et al.
---
In this paper, we tackle one-shot texture retrieval: given an example of a
new reference texture, detect and segment all the pixels of the same texture
category within an arbitrary image. To address this problem, we present an
OS-TR network to encode both reference and query image, leading to achieve
texture segmentation towards the reference category. Unlike the existing
texture encoding methods that integrate CNN with orderless pooling, we propose
a directionality-aware module to capture the texture variations at each
direction, resulting in spatially invariant representation. To segment new
categories given only few examples, we incorporate a self-gating mechanism into
relation network to exploit global context information for adjusting
per-channel modulation weights of local relation features. Extensive
experiments on benchmark texture datasets and real scenarios demonstrate the
above-par segmentation performance and robust generalization across domains of
our proposed method.