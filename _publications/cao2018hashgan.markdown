---
layout: publication
title: 'Hashgan: Deep Learning To Hash With Pair Conditional Wasserstein GAN'
authors: Cao et al.
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: cao2018hashgan
citations: 117
additional_links: [{name: Paper, url: 'http://ise.thss.tsinghua.edu.cn/~mlong/doc/hashgan-cvpr18.pdf'}]
tags: ["Hashing Methods", "CVPR"]
---
Deep learning to hash improves image retrieval performance by end-to-end representation learning and hash coding from training data with pairwise similarity information.
Subject to the scarcity of similarity information that is often
expensive to collect for many application domains, existing
deep learning to hash methods may overfit the training data
and result in substantial loss of retrieval quality. This paper
presents HashGAN, a novel architecture for deep learning
to hash, which learns compact binary hash codes from both
real images and diverse images synthesized by generative
models. The main idea is to augment the training data with
nearly real images synthesized from a new Pair Conditional
Wasserstein GAN (PC-WGAN) conditioned on the pairwise
similarity information. Extensive experiments demonstrate
that HashGAN can generate high-quality binary hash codes
and yield state-of-the-art image retrieval performance on
three benchmarks, NUS-WIDE, CIFAR-10, and MS-COCO.