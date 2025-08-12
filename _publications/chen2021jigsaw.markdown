---
layout: publication
title: Jigsaw Clustering For Unsupervised Visual Representation Learning
authors: Pengguang Chen, Shu Liu, Jiaya Jia
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: chen2021jigsaw
citations: 54
additional_links: [{name: Code, url: 'https://github.com/Jia-Research-Lab/JigsawClustering'},
  {name: Paper, url: 'https://arxiv.org/abs/2104.00323'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Pengguang Chen, Shu Liu, Jiaya Jia
---
Unsupervised representation learning with contrastive learning achieved great
success. This line of methods duplicate each training batch to construct
contrastive pairs, making each training batch and its augmented version
forwarded simultaneously and leading to additional computation. We propose a
new jigsaw clustering pretext task in this paper, which only needs to forward
each training batch itself, and reduces the training cost. Our method makes use
of information from both intra- and inter-images, and outperforms previous
single-batch based ones by a large margin. It is even comparable to the
contrastive learning methods when only half of training batches are used.
  Our method indicates that multiple batches during training are not necessary,
and opens the door for future research of single-batch unsupervised methods.
Our models trained on ImageNet datasets achieve state-of-the-art results with
linear classification, outperforming previous single-batch methods by 2.6%.
Models transferred to COCO datasets outperform MoCo v2 by 0.4% with only half
of the training batches. Our pretrained models outperform supervised ImageNet
pretrained models on CIFAR-10 and CIFAR-100 datasets by 0.9% and 4.1%
respectively. Code is available at
https://github.com/Jia-Research-Lab/JigsawClustering