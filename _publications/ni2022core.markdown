---
layout: publication
title: 'CORE: Consistent Representation Learning For Face Forgery Detection'
authors: Yunsheng Ni, Depu Meng, Changqian Yu, Chengbin Quan, Dongchun Ren, Youjian
  Zhao
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: ni2022core
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.02749'}]
tags: ["CVPR"]
short_authors: Ni et al.
---
Face manipulation techniques develop rapidly and arouse widespread public
concerns. Despite that vanilla convolutional neural networks achieve acceptable
performance, they suffer from the overfitting issue. To relieve this issue,
there is a trend to introduce some erasing-based augmentations. We find that
these methods indeed attempt to implicitly induce more consistent
representations for different augmentations via assigning the same label for
different augmented images. However, due to the lack of explicit
regularization, the consistency between different representations is less
satisfactory. Therefore, we constrain the consistency of different
representations explicitly and propose a simple yet effective framework,
COnsistent REpresentation Learning (CORE). Specifically, we first capture the
different representations with different augmentations, then regularize the
cosine distance of the representations to enhance the consistency. Extensive
experiments (in-dataset and cross-dataset) demonstrate that CORE performs
favorably against state-of-the-art face forgery detection methods.