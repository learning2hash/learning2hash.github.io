---
layout: publication
title: Relational Self-supervised Distillation With Compact Descriptors For Image
  Copy Detection
authors: Juntae Kim, Sungwon Woo, Jongho Nang
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2025
bibkey: kim2024relational
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.17928'}]
tags: ["Self-Supervised"]
short_authors: Juntae Kim, Sungwon Woo, Jongho Nang
---
Image copy detection is the task of detecting edited copies of any image
within a reference database. While previous approaches have shown remarkable
progress, the large size of their networks and descriptors remains a
disadvantage, complicating their practical application. In this paper, we
propose a novel method that achieves competitive performance by using a
lightweight network and compact descriptors. By utilizing relational
self-supervised distillation to transfer knowledge from a large network to a
small network, we enable the training of lightweight networks with smaller
descriptor sizes. We introduce relational self-supervised distillation for
flexible representation in a smaller feature space and apply contrastive
learning with a hard negative loss to prevent dimensional collapse. For the
DISC2021 benchmark, ResNet-50 and EfficientNet-B0 are used as the teacher and
student models, respectively, with micro average precision improving by
5.0%/4.9%/5.9% for 64/128/256 descriptor sizes compared to the baseline
method. The code is available at
\href\{https://github.com/juntae9926/RDCD\}\{https://github.com/juntae9926/RDCD\}.