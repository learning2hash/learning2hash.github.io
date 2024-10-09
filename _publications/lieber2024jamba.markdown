---
layout: publication
title: Jamba A Hybrid Transformer-mamba Language Model
authors: Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Jhonathan Osin, Itay Dalmedigos, Erez Safahi, Shaked Meirom, Yonatan Belinkov, Shai Shalev-shwartz, Omri Abend, Raz Alon, Tomer Asida, Amir Bergman, Roman Glozman, Michael Gokhman, Avashalom Manevich, Nir Ratner, Noam Rozen, Erez Shwartz, Mor Zusman, Yoav Shoham
conference: "Arxiv"
year: 2024
bibkey: lieber2024jamba
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2403.19887v2"}
tags: ['ARXIV']
---
We present Jamba a new base large language model based on a novel hybrid Transformer-Mamba mixture-of-experts (MoE) architecture. Specifically Jamba interleaves blocks of Transformer and Mamba layers enjoying the benefits of both model families. MoE is added in some of these layers to increase model capacity while keeping active parameter usage manageable. This flexible architecture allows resource- and objective-specific configurations. In the particular configuration we have implemented we end up with a powerful model that fits in a single 80GB GPU. Built at large scale Jamba provides high throughput and small memory footprint compared to vanilla Transformers and at the same time state-of-the-art performance on standard language model benchmarks and long-context evaluations. Remarkably the model presents strong results for up to 256K tokens context length. We study various architectural decisions such as how to combine Transformer and Mamba layers and how to mix experts and show that some of them are crucial in large scale modeling. We also describe several interesting properties of these architectures which the training and evaluation of Jamba have revealed and plan to release checkpoints from various ablation runs to encourage further exploration of this novel architecture. We make the weights of our implementation of Jamba publicly available under a permissive license.
