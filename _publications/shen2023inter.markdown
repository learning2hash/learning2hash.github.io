---
layout: publication
title: Inter-instance Similarity Modeling For Contrastive Learning
authors: Chengchao Shen, Dawei Liu, Hao Tang, Zhe Qu, Jianxin Wang
conference: Arxiv
year: 2023
bibkey: shen2023inter
citations: 5
additional_links: [{name: Code, url: 'https://github.com/visresearch/patchmix'}, {
    name: Paper, url: 'https://arxiv.org/abs/2306.12243'}]
tags: ["Self-Supervised"]
short_authors: Shen et al.
---
The existing contrastive learning methods widely adopt one-hot instance
discrimination as pretext task for self-supervised learning, which inevitably
neglects rich inter-instance similarities among natural images, then leading to
potential representation degeneration. In this paper, we propose a novel image
mix method, PatchMix, for contrastive learning in Vision Transformer (ViT), to
model inter-instance similarities among images. Following the nature of ViT, we
randomly mix multiple images from mini-batch in patch level to construct mixed
image patch sequences for ViT. Compared to the existing sample mix methods, our
PatchMix can flexibly and efficiently mix more than two images and simulate
more complicated similarity relations among natural images. In this manner, our
contrastive framework can significantly reduce the gap between contrastive
objective and ground truth in reality. Experimental results demonstrate that
our proposed method significantly outperforms the previous state-of-the-art on
both ImageNet-1K and CIFAR datasets, e.g., 3.0% linear accuracy improvement on
ImageNet-1K and 8.7% kNN accuracy improvement on CIFAR100. Moreover, our method
achieves the leading transfer performance on downstream tasks, object detection
and instance segmentation on COCO dataset. The code is available at
https://github.com/visresearch/patchmix