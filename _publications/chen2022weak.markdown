---
layout: publication
title: Weak-shot Semantic Segmentation Via Dual Similarity Transfer
authors: Junjie Chen, Li Niu, Siyuan Zhou, Jianlou Si, Chen Qian, Liqing Zhang
conference: Arxiv
year: 2022
bibkey: chen2022weak
citations: 3
additional_links: [{name: Code, url: 'https://github.com/bcmi/SimFormer-Weak-Shot-Semantic-Segmentation'},
  {name: Paper, url: 'https://arxiv.org/abs/2210.02270'}]
tags: []
short_authors: Chen et al.
---
Semantic segmentation is an important and prevalent task, but severely
suffers from the high cost of pixel-level annotations when extending to more
classes in wider applications. To this end, we focus on the problem named
weak-shot semantic segmentation, where the novel classes are learnt from
cheaper image-level labels with the support of base classes having
off-the-shelf pixel-level labels. To tackle this problem, we propose SimFormer,
which performs dual similarity transfer upon MaskFormer. Specifically,
MaskFormer disentangles the semantic segmentation task into two sub-tasks:
proposal classification and proposal segmentation for each proposal. Proposal
segmentation allows proposal-pixel similarity transfer from base classes to
novel classes, which enables the mask learning of novel classes. We also learn
pixel-pixel similarity from base classes and distill such class-agnostic
semantic similarity to the semantic masks of novel classes, which regularizes
the segmentation model with pixel-level semantic relationship across images. In
addition, we propose a complementary loss to facilitate the learning of novel
classes. Comprehensive experiments on the challenging COCO-Stuff-10K and ADE20K
datasets demonstrate the effectiveness of our method. Codes are available at
https://github.com/bcmi/SimFormer-Weak-Shot-Semantic-Segmentation.