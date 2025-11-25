---
layout: publication
title: Experimentally Realized Memristive Memory Augmented Neural Network
authors: Ruibin Mao, Bo Wen, Yahui Zhao, Arman Kazemi, Ann Franchesca Laguna, Michael
  Neimier, X. Sharon Hu, Xia Sheng, Catherine E. Graves, John Paul Strachan, Can Li
conference: Arxiv
year: 2022
bibkey: mao2022experimentally
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.07429'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Locality-Sensitive-Hashing"]
short_authors: Mao et al.
---
Lifelong on-device learning is a key challenge for machine intelligence, and
this requires learning from few, often single, samples. Memory augmented neural
network has been proposed to achieve the goal, but the memory module has to be
stored in an off-chip memory due to its size. Therefore the practical use has
been heavily limited. Previous works on emerging memory-based implementation
have difficulties in scaling up because different modules with various
structures are difficult to integrate on the same chip and the small sense
margin of the content addressable memory for the memory module heavily limited
the degree of mismatch calculation. In this work, we implement the entire
memory augmented neural network architecture in a fully integrated memristive
crossbar platform and achieve an accuracy that closely matches standard
software on digital hardware for the Omniglot dataset. The successful
demonstration is supported by implementing new functions in crossbars in
addition to widely reported matrix multiplications. For example, the
locality-sensitive hashing operation is implemented in crossbar arrays by
exploiting the intrinsic stochasticity of memristor devices. Besides, the
content-addressable memory module is realized in crossbars, which also supports
the degree of mismatches. Simulations based on experimentally validated models
show such an implementation can be efficiently scaled up for one-shot learning
on the Mini-ImageNet dataset. The successful demonstration paves the way for
practical on-device lifelong learning and opens possibilities for novel
attention-based algorithms not possible in conventional hardware.