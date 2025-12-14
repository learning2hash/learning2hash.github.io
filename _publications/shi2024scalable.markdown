---
layout: publication
title: Scalable Image Tokenization With Index Backpropagation Quantization
authors: Fengyuan Shi, Zhuoyan Luo, Yixiao Ge, Yujiu Yang, Ying Shan, Limin Wang
conference: Arxiv
year: 2024
bibkey: shi2024scalable
citations: 0
additional_links: [{name: Code, url: 'https://github.com/TencentARC/SEED-Voken'},
  {name: Paper, url: 'https://arxiv.org/abs/2412.02692'}]
tags: [Scalability, Evaluation, Quantization]
short_authors: Shi et al.
---
Existing vector quantization (VQ) methods struggle with scalability, largely
attributed to the instability of the codebook that undergoes partial updates
during training. The codebook is prone to collapse as utilization decreases,
due to the progressively widening distribution gap between non-activated codes
and visual features. To solve the problem, we propose Index Backpropagation
Quantization (IBQ), a new VQ method for the joint optimization of all codebook
embeddings and the visual encoder. Applying a straight-through estimator on the
one-hot categorical distribution between the encoded feature and codebook, all
codes are differentiable and maintain a consistent latent space with the visual
encoder. IBQ enables scalable training of visual tokenizers and, for the first
time, achieves a large-scale codebook (\(2^\{18\}\)) with high dimension (\(256\))
and high utilization. Experiments on the standard ImageNet benchmark
demonstrate the scalability and superiority of IBQ, achieving competitive
results on reconstruction and the application of autoregressive visual
generation. The code and models are available at
https://github.com/TencentARC/SEED-Voken.