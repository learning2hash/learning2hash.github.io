---
layout: publication
title: Prototype45;supervised Adversarial Network For Targeted Attack Of Deep Hashing
authors: Wang Xunguang, Zhang Zheng, Wu Baoyuan, Shen Fumin, Lu Guangming
conference: "Arxiv"
year: 2021
bibkey: wang2021adversarial
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.07553"}
  - {name: "Code", url: "https://github.com/xunguangwang/ProS&#45;GAN"}
tags: ['ARXIV', 'GAN', 'Has Code', 'Image Retrieval', 'Supervised']
---
Due to its powerful capability of representation learning and high45;efficiency computation deep hashing has made significant progress in large45;scale image retrieval. However deep hashing networks are vulnerable to adversarial examples which is a practical secure problem but seldom studied in hashing45;based retrieval field. In this paper we propose a novel prototype45;supervised adversarial network (ProS45;GAN) which formulates a flexible generative architecture for efficient and effective targeted hashing attack. To the best of our knowledge this is the first generation45;based method to attack deep hashing networks. Generally our proposed framework consists of three parts i.e. a PrototypeNet a generator and a discriminator. Specifically the designed PrototypeNet embeds the target label into the semantic representation and learns the prototype code as the category45;level representative of the target label. Moreover the semantic representation and the original image are jointly fed into the generator for a flexible targeted attack. Particularly the prototype code is adopted to supervise the generator to construct the targeted adversarial example by minimizing the Hamming distance between the hash code of the adversarial example and the prototype code. Furthermore the generator is against the discriminator to simultaneously encourage the adversarial examples visually realistic and the semantic representation informative. Extensive experiments verify that the proposed framework can efficiently produce adversarial examples with better targeted attack performance and transferability over state45;of45;the45;art targeted attack methods of deep hashing. The related codes could be available at https://github.com/xunguangwang/ProS&#45;GAN .
