---
layout: publication
title: Improving Biomedical Entity Linking With Retrieval-enhanced Learning
authors: Zhenxi Lin, Ziheng Zhang, Xian Wu, Yefeng Zheng
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: lin2024improving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.09806'}]
tags: [Self-Supervised, ICASSP, Datasets]
short_authors: Lin et al.
---
Biomedical entity linking (BioEL) has achieved remarkable progress with the
help of pre-trained language models. However, existing BioEL methods usually
struggle to handle rare and difficult entities due to long-tailed distribution.
To address this limitation, we introduce a new scheme \(k\)NN-BioEL, which
provides a BioEL model with the ability to reference similar instances from the
entire training corpus as clues for prediction, thus improving the
generalization capabilities. Moreover, we design a contrastive learning
objective with dynamic hard negative sampling (DHNS) that improves the quality
of the retrieved neighbors during inference. Extensive experimental results
show that \(k\)NN-BioEL outperforms state-of-the-art baselines on several
datasets.