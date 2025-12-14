---
layout: publication
title: Prototype-supervised Adversarial Network For Targeted Attack Of Deep Hashing
authors: Xunguang Wang, Zheng Zhang, Baoyuan Wu, Fumin Shen, Guangming Lu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: wang2021prototype
citations: 50
additional_links: [{name: Code, url: 'https://github.com/xunguangwang/ProS-GAN'},
  {name: Paper, url: 'https://arxiv.org/abs/2105.07553'}]
tags: [Evaluation, Supervised, Image Retrieval, Efficiency, Neural Hashing, Robustness,
  Scalability, CVPR, Tools & Libraries, Hashing Methods]
short_authors: Wang et al.
---
Due to its powerful capability of representation learning and high-efficiency
computation, deep hashing has made significant progress in large-scale image
retrieval. However, deep hashing networks are vulnerable to adversarial
examples, which is a practical secure problem but seldom studied in
hashing-based retrieval field. In this paper, we propose a novel
prototype-supervised adversarial network (ProS-GAN), which formulates a
flexible generative architecture for efficient and effective targeted hashing
attack. To the best of our knowledge, this is the first generation-based method
to attack deep hashing networks. Generally, our proposed framework consists of
three parts, i.e., a PrototypeNet, a generator, and a discriminator.
Specifically, the designed PrototypeNet embeds the target label into the
semantic representation and learns the prototype code as the category-level
representative of the target label. Moreover, the semantic representation and
the original image are jointly fed into the generator for a flexible targeted
attack. Particularly, the prototype code is adopted to supervise the generator
to construct the targeted adversarial example by minimizing the Hamming
distance between the hash code of the adversarial example and the prototype
code. Furthermore, the generator is against the discriminator to simultaneously
encourage the adversarial examples visually realistic and the semantic
representation informative. Extensive experiments verify that the proposed
framework can efficiently produce adversarial examples with better targeted
attack performance and transferability over state-of-the-art targeted attack
methods of deep hashing. The related codes could be available at
https://github.com/xunguangwang/ProS-GAN .