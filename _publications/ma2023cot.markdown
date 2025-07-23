---
layout: publication
title: 'Cot-mote: Exploring Contextual Masked Auto-encoder Pre-training With Mixture-of-textual-experts
  For Passage Retrieval'
authors: Ma Guangyuan, Wu Xing, Wang Peng, Hu Songlin
conference: Arxiv
year: 2023
bibkey: ma2023cot
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.10195'}]
tags: ["Scalability", "Self-Supervised", "Transformer-based ANN"]
short_authors: Ma et al.
---
Passage retrieval aims to retrieve relevant passages from large collections
of the open-domain corpus. Contextual Masked Auto-Encoding has been proven
effective in representation bottleneck pre-training of a monolithic
dual-encoder for passage retrieval. Siamese or fully separated dual-encoders
are often adopted as basic retrieval architecture in the pre-training and
fine-tuning stages for encoding queries and passages into their latent
embedding spaces. However, simply sharing or separating the parameters of the
dual-encoder results in an imbalanced discrimination of the embedding spaces.
In this work, we propose to pre-train Contextual Masked Auto-Encoder with
Mixture-of-Textual-Experts (CoT-MoTE). Specifically, we incorporate
textual-specific experts for individually encoding the distinct properties of
queries and passages. Meanwhile, a shared self-attention layer is still kept
for unified attention modeling. Results on large-scale passage retrieval
benchmarks show steady improvement in retrieval performances. The quantitive
analysis also shows a more balanced discrimination of the latent embedding
spaces.