---
layout: publication
title: Weak-shot Semantic Segmentation By Transferring Semantic Affinity And Boundary
authors: Siyuan Zhou, Li Niu, Jianlou Si, Chen Qian, Liqing Zhang
conference: Arxiv
year: 2021
bibkey: zhou2021weak
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.01519'}]
tags: []
short_authors: Zhou et al.
---
Weakly-supervised semantic segmentation (WSSS) with image-level labels has
been widely studied to relieve the annotation burden of the traditional
segmentation task. In this paper, we show that existing fully-annotated base
categories can help segment objects of novel categories with only image-level
labels, even if base categories and novel categories have no overlap. We refer
to this task as weak-shot semantic segmentation, which could also be treated as
WSSS with auxiliary fully-annotated categories. Recent advanced WSSS methods
usually obtain class activation maps (CAMs) and refine them by affinity
propagation. Based on the observation that semantic affinity and boundary are
class-agnostic, we propose a method under the WSSS framework to transfer
semantic affinity and boundary from base to novel categories. As a result, we
find that pixel-level annotation of base categories can facilitate affinity
learning and propagation, leading to higher-quality CAMs of novel categories.
Extensive experiments on PASCAL VOC 2012 dataset prove that our method
significantly outperforms WSSS baselines on novel categories.