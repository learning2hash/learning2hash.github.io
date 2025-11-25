---
layout: publication
title: Improve Supervised Representation Learning With Masked Image Modeling
authors: Kaifeng Chen, Daniel Salz, Huiwen Chang, Kihyuk Sohn, Dilip Krishnan, Mojtaba
  Seyedhosseini
conference: Arxiv
year: 2023
bibkey: chen2023improve
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.00950'}]
tags: ["Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Chen et al.
---
Training visual embeddings with labeled data supervision has been the de
facto setup for representation learning in computer vision. Inspired by recent
success of adopting masked image modeling (MIM) in self-supervised
representation learning, we propose a simple yet effective setup that can
easily integrate MIM into existing supervised training paradigms. In our
design, in addition to the original classification task applied to a vision
transformer image encoder, we add a shallow transformer-based decoder on top of
the encoder and introduce an MIM task which tries to reconstruct image tokens
based on masked image inputs. We show with minimal change in architecture and
no overhead in inference that this setup is able to improve the quality of the
learned representations for downstream tasks such as classification, image
retrieval, and semantic segmentation. We conduct a comprehensive study and
evaluation of our setup on public benchmarks. On ImageNet-1k, our ViT-B/14
model achieves 81.72% validation accuracy, 2.01% higher than the baseline
model. On K-Nearest-Neighbor image retrieval evaluation with ImageNet-1k, the
same model outperforms the baseline by 1.32%. We also show that this setup can
be easily scaled to larger models and datasets. Code and checkpoints will be
released.