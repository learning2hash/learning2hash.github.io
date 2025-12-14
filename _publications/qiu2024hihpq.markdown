---
layout: publication
title: 'Hihpq: Hierarchical Hyperbolic Product Quantization For Unsupervised Image
  Retrieval'
authors: Zexuan Qiu, Jiahong Liu, Yankai Chen, Irwin King
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: qiu2024hihpq
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.07212'}]
tags: [Evaluation, Supervised, Image Retrieval, Self-Supervised, Quantization, Unsupervised,
  AAAI]
short_authors: Qiu et al.
---
Existing unsupervised deep product quantization methods primarily aim for the
increased similarity between different views of the identical image, whereas
the delicate multi-level semantic similarities preserved between images are
overlooked. Moreover, these methods predominantly focus on the Euclidean space
for computational convenience, compromising their ability to map the
multi-level semantic relationships between images effectively. To mitigate
these shortcomings, we propose a novel unsupervised product quantization method
dubbed \textbf\{Hi\}erarchical \textbf\{H\}yperbolic \textbf\{P\}roduct
\textbf\{Q\}uantization (HiHPQ), which learns quantized representations by
incorporating hierarchical semantic similarity within hyperbolic geometry.
Specifically, we propose a hyperbolic product quantizer, where the hyperbolic
codebook attention mechanism and the quantized contrastive learning on the
hyperbolic product manifold are introduced to expedite quantization.
Furthermore, we propose a hierarchical semantics learning module, designed to
enhance the distinction between similar and non-matching images for a query by
utilizing the extracted hierarchical semantics as an additional training
supervision. Experiments on benchmarks show that our proposed method
outperforms state-of-the-art baselines.