---
layout: publication
title: HHF Hashing45;guided Hinge Function For Deep Hashing Retrieval
authors: Xu Chengyin, Chai Zenghao, Xu Zhengzhuo, Li Hongjia, Zuo Qiruyi, Yang Lingyu, Yuan Chun
conference: "Arxiv"
year: 2021
bibkey: xu2021hhf
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.02225"}
  - {name: "Code", url: "https://github.com/JerryXu0129/HHF"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval', 'Quantisation', 'Supervised']
---
Deep hashing has shown promising performance in large45;scale image retrieval. However latent codes extracted by Deep Neural Networks (DNNs) will inevitably lose semantic information during the binarization process which damages the retrieval accuracy and makes it challenging. Although many existing approaches perform regularization to alleviate quantization errors we figure out an incompatible conflict between metric learning and quantization learning. The metric loss penalizes the inter45;class distances to push different classes unconstrained far away. Worse still it tends to map the latent code deviate from ideal binarization point and generate severe ambiguity in the binarization process. Based on the minimum distance of the binary linear code we creatively propose Hashing45;guided Hinge Function (HHF) to avoid such conflict. In detail the carefully45;designed inflection point which relies on the hash bit length and category numbers is explicitly adopted to balance the metric term and quantization term. Such a modification prevents the network from falling into local metric optimal minima in deep hashing. Extensive experiments in CIFAR45;10 CIFAR45;100 ImageNet and MS45;COCO show that HHF consistently outperforms existing techniques and is robust and flexible to transplant into other methods. Code is available at https://github.com/JerryXu0129/HHF.
