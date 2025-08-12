---
layout: publication
title: Multi-level Metric Learning For Few-shot Image Recognition
authors: Haoxing Chen, Huaxiong Li, Yaohui Li, Chunlin Chen
conference: Lecture Notes in Computer Science
year: 2022
bibkey: chen2021multi
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.11383'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Few-shot learning is devoted to training a model on few samples. Most of
these approaches learn a model based on a pixel-level or global-level feature
representation. However, using global features may lose local information, and
using pixel-level features may lose the contextual semantics of the image.
Moreover, such works can only measure the relations between them on a single
level, which is not comprehensive and effective. And if query images can
simultaneously be well classified via three distinct level similarity metrics,
the query images within a class can be more tightly distributed in a smaller
feature space, generating more discriminative feature maps. Motivated by this,
we propose a novel Part-level Embedding Adaptation with Graph (PEAG) method to
generate task-specific features. Moreover, a Multi-level Metric Learning (MML)
method is proposed, which not only calculates the pixel-level similarity but
also considers the similarity of part-level features and global-level features.
Extensive experiments on popular few-shot image recognition datasets prove the
effectiveness of our method compared with the state-of-the-art methods. Our
code is available at https://github.com/chenhaoxing/M2L.