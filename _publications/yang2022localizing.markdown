---
layout: publication
title: Localizing Semantic Patches For Accelerating Image Classification
authors: Chuanguang Yang, Zhulin An, Yongjun Xu
conference: 2022 IEEE International Conference on Multimedia and Expo (ICME)
year: 2022
bibkey: yang2022localizing
citations: 1
additional_links: [{name: Code, url: 'https://github.com/winycg/AnchorNet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2206.03367'}]
tags: ["Efficiency", "Image Retrieval"]
short_authors: Chuanguang Yang, Zhulin An, Yongjun Xu
---
Existing works often focus on reducing the architecture redundancy for
accelerating image classification but ignore the spatial redundancy of the
input image. This paper proposes an efficient image classification pipeline to
solve this problem. We first pinpoint task-aware regions over the input image
by a lightweight patch proposal network called AnchorNet. We then feed these
localized semantic patches with much smaller spatial redundancy into a general
classification network. Unlike the popular design of deep CNN, we aim to
carefully design the Receptive Field of AnchorNet without intermediate
convolutional paddings. This ensures the exact mapping from a high-level
spatial location to the specific input image patch. The contribution of each
patch is interpretable. Moreover, AnchorNet is compatible with any downstream
architecture. Experimental results on ImageNet show that our method outperforms
SOTA dynamic inference methods with fewer inference costs. Our code is
available at https://github.com/winycg/AnchorNet.