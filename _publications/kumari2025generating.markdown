---
layout: publication
title: Generating Multi-image Synthetic Data For Text-to-image Customization
authors: Nupur Kumari, Xi Yin, Jun-Yan Zhu, Ishan Misra, Samaneh Azadi
conference: Arxiv
year: 2025
bibkey: kumari2025generating
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.01720'}]
tags: ["Datasets"]
short_authors: Kumari et al.
---
Customization of text-to-image models enables users to insert custom concepts
and generate the concepts in unseen settings. Existing methods either rely on
costly test-time optimization or train encoders on single-image training
datasets without multi-image supervision, leading to worse image quality. We
propose a simple approach that addresses both limitations. We first leverage
existing text-to-image models and 3D datasets to create a high-quality
Synthetic Customization Dataset (SynCD) consisting of multiple images of the
same object in different lighting, backgrounds, and poses. We then propose a
new encoder architecture based on shared attention mechanisms that better
incorporate fine-grained visual details from input images. Finally, we propose
a new inference technique that mitigates overexposure issues during inference
by normalizing the text and image guidance vectors. Through extensive
experiments, we show that our model, trained on the synthetic dataset with the
proposed encoder and inference algorithm, outperforms existing tuning-free
methods on standard customization benchmarks.