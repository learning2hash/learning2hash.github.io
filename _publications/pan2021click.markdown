---
layout: publication
title: Click-through Rate Prediction With Auto-quantized Contrastive Learning
authors: Yujie Pan, Jiangchao Yao, Bo Han, Kunyang Jia, Ya Zhang, Hongxia Yang
conference: Arxiv
year: 2021
bibkey: pan2021click
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.13921'}]
tags: ["Quantization", "Recommender Systems", "Self-Supervised"]
short_authors: Pan et al.
---
Click-through rate (CTR) prediction becomes indispensable in ubiquitous web
recommendation applications. Nevertheless, the current methods are struggling
under the cold-start scenarios where the user interactions are extremely
sparse. We consider this problem as an automatic identification about whether
the user behaviors are rich enough to capture the interests for prediction, and
propose an Auto-Quantized Contrastive Learning (AQCL) loss to regularize the
model. Different from previous methods, AQCL explores both the
instance-instance and the instance-cluster similarity to robustify the latent
representation, and automatically reduces the information loss to the active
users due to the quantization. The proposed framework is agnostic to different
model architectures and can be trained in an end-to-end fashion. Extensive
results show that it consistently improves the current state-of-the-art CTR
models.