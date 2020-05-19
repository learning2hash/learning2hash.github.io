---
layout: publication
title: "Targeted Attack for Deep Hashing based Retrieval"
authors: Jiawang Bai, Bin Chen, Yiming Li, Dongxian Wu, Weiwei Guo, Shu-tao Xia, En-hui Yang
conference: Arxiv
year: 2020
bibkey: bai2020bai
additional_links:
   - {name: "PDF", url: "https://arxiv.org/abs/2004.07955"}
tags: ["Deep Learning", "Adversarial Attack", "Arxiv", "Image Retrieval", "Video Retrieval"]
---
The deep hashing based retrieval method is widely adopted in large-scale image and video retrieval. However, there is little investigation on its security. In this paper, we propose a novel method, dubbed deep hashing targeted attack (DHTA), to study the targeted attack on such retrieval. Specifically, we first formulate the targeted attack as a point-to-set optimization, which minimizes the average distance between the hash code of an adversarial example and those of a set of objects with the target label. Then we design a novel component-voting scheme to obtain an anchor code as the representative of the set of hash codes of objects with the target label, whose optimality guarantee is also theoretically derived. To balance the performance and perceptibility, we propose to minimize the Hamming distance between the hash code of the adversarial example and the anchor code under the ℓ∞ restriction on the perturbation. Extensive experiments verify that DHTA is effective in attacking both deep hashing based image retrieval and video retrieval.
