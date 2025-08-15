---
layout: publication
title: 'SSAH: Semi-supervised Adversarial Deep Hashing With Self-paced Hard Sample
  Generation'
authors: Sheng Jin, Shangchen Zhou, Yao Liu, Chao Chen, Xiaoshuai Sun, Hongxun Yao,
  Xiansheng Hua
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: jin2019ssah
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.08688'}]
tags: ["AAAI", "Datasets", "Hashing Methods", "Neural Hashing"]
short_authors: Jin et al.
---
Deep hashing methods have been proved to be effective and efficient for
large-scale Web media search. The success of these data-driven methods largely
depends on collecting sufficient labeled data, which is usually a crucial
limitation in practical cases. The current solutions to this issue utilize
Generative Adversarial Network (GAN) to augment data in semi-supervised
learning. However, existing GAN-based methods treat image generations and
hashing learning as two isolated processes, leading to generation
ineffectiveness. Besides, most works fail to exploit the semantic information
in unlabeled data. In this paper, we propose a novel Semi-supervised Self-pace
Adversarial Hashing method, named SSAH to solve the above problems in a unified
framework. The SSAH method consists of an adversarial network (A-Net) and a
hashing network (H-Net). To improve the quality of generative images, first,
the A-Net learns hard samples with multi-scale occlusions and multi-angle
rotated deformations which compete against the learning of accurate hashing
codes. Second, we design a novel self-paced hard generation policy to gradually
increase the hashing difficulty of generated samples. To make use of the
semantic information in unlabeled ones, we propose a semi-supervised consistent
loss. The experimental results show that our method can significantly improve
state-of-the-art models on both the widely-used hashing datasets and
fine-grained datasets.