---
layout: publication
title: Towards Low-loss 1-bit Quantization Of User-item Representations For Top-k
  Recommendation
authors: Chen Yankai et al.
conference: Arxiv
year: 2021
citations: 1
bibkey: chen2021towards
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01944'}]
tags: [Quantization, ANN Search, Has Code]
---
Due to the promising advantages in space compression and inference
acceleration, quantized representation learning for recommender systems has
become an emerging research direction recently. As the target is to embed
latent features in the discrete embedding space, developing quantization for
user-item representations with a few low-precision integers confronts the
challenge of high information loss, thus leading to unsatisfactory performance
in Top-K recommendation.
  In this work, we study the problem of representation learning for
recommendation with 1-bit quantization. We propose a model named Low-loss
Quantized Graph Convolutional Network (L^2Q-GCN). Different from previous work
that plugs quantization as the final encoder of user-item embeddings, L^2Q-GCN
learns the quantized representations whilst capturing the structural
information of user-item interaction graphs at different semantic levels. This
achieves the substantial retention of intermediate interactive information,
alleviating the feature smoothing issue for ranking caused by numerical
quantization. To further improve the model performance, we also present an
advanced solution named L^2Q-GCN-anl with quantization approximation and
annealing training strategy. We conduct extensive experiments on four
benchmarks over Top-K recommendation task. The experimental results show that,
with nearly 9x representation storage compression, L^2Q-GCN-anl attains about
90~99% performance recovery compared to the state-of-the-art model.