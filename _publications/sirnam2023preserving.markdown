---
layout: publication
title: Preserving Modality Structure Improves Multi-modal Learning
authors: Swetha Sirnam, Mamshad Nayeem Rizve, Nina Shvetsova, Hilde Kuehne, Mubarak
  Shah
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: sirnam2023preserving
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Swetha5/Multi_Sinkhorn_Knopp'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.13077'}]
tags: [Evaluation, Supervised, ICCV, Few-shot & Zero-shot, Self-Supervised, Datasets,
  Scalability]
short_authors: Sirnam et al.
---
Self-supervised learning on large-scale multi-modal datasets allows learning
semantically meaningful embeddings in a joint multi-modal representation space
without relying on human annotations. These joint embeddings enable zero-shot
cross-modal tasks like retrieval and classification. However, these methods
often struggle to generalize well on out-of-domain data as they ignore the
semantic structure present in modality-specific embeddings. In this context, we
propose a novel Semantic-Structure-Preserving Consistency approach to improve
generalizability by preserving the modality-specific relationships in the joint
embedding space. To capture modality-specific semantic relationships between
samples, we propose to learn multiple anchors and represent the multifaceted
relationship between samples with respect to their relationship with these
anchors. To assign multiple anchors to each sample, we propose a novel
Multi-Assignment Sinkhorn-Knopp algorithm. Our experimentation demonstrates
that our proposed approach learns semantically meaningful anchors in a
self-supervised manner. Furthermore, our evaluation on MSR-VTT and YouCook2
datasets demonstrates that our proposed multi-anchor assignment based solution
achieves state-of-the-art performance and generalizes to both inand
out-of-domain datasets. Code: https://github.com/Swetha5/Multi_Sinkhorn_Knopp