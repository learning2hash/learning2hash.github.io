---
layout: publication
title: Reliable And Efficient Evaluation Of Adversarial Robustness For Deep Hashing-based
  Retrieval
authors: Xunguang Wang, Jiawang Bai, Xinyue Xu, Xiaomeng Li
conference: Arxiv
year: 2023
bibkey: wang2023reliable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.12658'}]
tags: ["Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Robustness"]
short_authors: Wang et al.
---
Deep hashing has been extensively applied to massive image retrieval due to
its efficiency and effectiveness. Recently, several adversarial attacks have
been presented to reveal the vulnerability of deep hashing models against
adversarial examples. However, existing attack methods suffer from degraded
performance or inefficiency because they underutilize the semantic relations
between original samples or spend a lot of time learning these relations with a
deep neural network. In this paper, we propose a novel Pharos-guided Attack,
dubbed PgA, to evaluate the adversarial robustness of deep hashing networks
reliably and efficiently. Specifically, we design pharos code to represent the
semantics of the benign image, which preserves the similarity to semantically
relevant samples and dissimilarity to irrelevant ones. It is proven that we can
quickly calculate the pharos code via a simple math formula. Accordingly, PgA
can directly conduct a reliable and efficient attack on deep hashing-based
retrieval by maximizing the similarity between the hash code of the adversarial
example and the pharos code. Extensive experiments on the benchmark datasets
verify that the proposed algorithm outperforms the prior state-of-the-arts in
both attack strength and speed.