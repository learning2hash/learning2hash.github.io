---
layout: publication
title: Prototype-supervised Adversarial Network For Targeted Attack Of Deep Hashing
authors: Xunguang Wang, Zhang, Wu, Shen, Lu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: wang2021prototype
citations: 43
additional_links: [{name: Paper, url: 'https://openaccess.thecvf.com/content/CVPR2021/papers/Wang_Prototype-Supervised_Adversarial_Network_for_Targeted_Attack_of_Deep_Hashing_CVPR_2021_paper.pdf'}]
tags: ["CVPR", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Supervised"]
short_authors: Wang et al.
---
Due to its powerful capability of representation learning and high-efficiency computation, deep hashing has made significant progress in large-scale image retrieval. However, deep hashing networks are vulnerable to adversarial examples, which is a practical secure problem but seldom studied in hashing-based retrieval field. In this paper, we propose a novel prototype-supervised adversarial network (ProS-GAN), which formulates a flexible generative architecture for efficient and effective targeted hashing attack. To the best of our knowledge, this is the first generation-based method to attack deep hashing networks. Generally, our proposed framework consists of three parts, i.e., a PrototypeNet, a generator and a discriminator. Specifically, the designed PrototypeNet embeds the target label into the semantic representation and learns the prototype code as the category-level representative of the target label. Moreover, the semantic representation and the original image are jointly fed into the generator for flexible targeted attack. Particularly, the prototype code is adopted to supervise the generator to construct the targeted adversarial example by minimizing the Hamming distance between the hash code of the adversarial example and the prototype code. Furthermore, the generator is against the discriminator to simultaneously encourage the adversarial examples visually realistic and the semantic representation informative. Extensive experiments verify that the proposed framework can efficiently produce adversarial examples with better targeted attack performance and transferability over state-of-the-art targeted attack methods of deep hashing.