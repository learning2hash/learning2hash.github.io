---
layout: publication
title: "A Feature Consistency Driven Attention Erasing Network for Fine-Grained Image Retrieval"
authors: Zhao Qi, Wang Xu, Lyu Shuchang, Liu Binghao, Yang Yifan
conference: Arxiv
year: 2021
bibkey: zhao2021a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2110.04479"}
tags: ['ARXIV', 'Image Retrieval']
---
Large-scale fine-grained image retrieval has two main problems. First, low dimensional feature embedding can fasten the retrieval process but bring accuracy reduce due to overlooking the feature of significant attention regions of images in fine-grained datasets. Second, fine-grained images lead to the same category query hash codes mapping into the different cluster in database hash latent space. To handle these two issues, we propose a feature consistency driven attention erasing network (FCAENet) for fine-grained image retrieval. For the first issue, we propose an adaptive augmentation module in FCAENet, which is selective region erasing module (SREM). SREM makes the network more robust on subtle differences of fine-grained task by adaptively covering some regions of raw images. The feature extractor and hash layer can learn more representative hash code for fine-grained images by SREM. With regard to the second issue, we fully exploit the pair-wise similarity information and add the enhancing space relation loss (ESRL) in FCAENet to make the vulnerable relation stabler between the query hash code and database hash code. We conduct extensive experiments on five fine-grained benchmark datasets (CUB2011, Aircraft, NABirds, VegFru, Food101) for 12bits, 24bits, 32bits, 48bits hash code. The results show that FCAENet achieves the state-of-the-art (SOTA) fine-grained retrieval performance compared with other methods.