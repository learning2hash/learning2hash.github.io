---
layout: publication
title: 'Coophash: Cooperative Learning Of Multipurpose Descriptor And Contrastive
  Pair Generator Via Variational MCMC Teaching For Supervised Image Hashing'
authors: Khoa D. Doan, Jianwen Xie, Yaxuan Zhu, Yang Zhao, Ping Li
conference: Arxiv
year: 2022
citations: 2
bibkey: doan2022cooperative
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.04288'}]
tags: [Hashing Methods, Deep Hashing, Supervised]
---
Leveraging supervised information can lead to superior retrieval performance
in the image hashing domain but the performance degrades significantly without
enough labeled data. One effective solution to boost performance is to employ
generative models, such as Generative Adversarial Networks (GANs), to generate
synthetic data in an image hashing model. However, GAN-based methods are
difficult to train, which prevents the hashing approaches from jointly training
the generative models and the hash functions. This limitation results in
sub-optimal retrieval performance. To overcome this limitation, we propose a
novel framework, the generative cooperative hashing network, which is based on
energy-based cooperative learning. This framework jointly learns a powerful
generative representation of the data and a robust hash function via two
components: a top-down contrastive pair generator that synthesizes contrastive
images and a bottom-up multipurpose descriptor that simultaneously represents
the images from multiple perspectives, including probability density, hash
code, latent code, and category. The two components are jointly learned via a
novel likelihood-based cooperative learning scheme. We conduct experiments on
several real-world datasets and show that the proposed method outperforms the
competing hashing supervised methods, achieving up to 10% relative improvement
over the current state-of-the-art supervised hashing methods, and exhibits a
significantly better performance in out-of-distribution retrieval.