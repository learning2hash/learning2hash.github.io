---
layout: publication
title: Towards Open-vocabulary Video Instance Segmentation
authors: Haochen Wang, Cilin Yan, Shuai Wang, Xiaolong Jiang, Xu Tang, Yao Hu, Weidi
  Xie, Efstratios Gavves
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: wang2023towards
citations: 12
additional_links: [{name: Code, url: 'https://github.com/haochenheheda/LVVIS'}, {
    name: Paper, url: 'https://arxiv.org/abs/2304.01715'}]
tags: ["ICCV"]
short_authors: Wang et al.
---
Video Instance Segmentation (VIS) aims at segmenting and categorizing objects
in videos from a closed set of training categories, lacking the generalization
ability to handle novel categories in real-world videos. To address this
limitation, we make the following three contributions. First, we introduce the
novel task of Open-Vocabulary Video Instance Segmentation, which aims to
simultaneously segment, track, and classify objects in videos from open-set
categories, including novel categories unseen during training. Second, to
benchmark Open-Vocabulary VIS, we collect a Large-Vocabulary Video Instance
Segmentation dataset (LV-VIS), that contains well-annotated objects from 1,196
diverse categories, significantly surpassing the category size of existing
datasets by more than one order of magnitude. Third, we propose an efficient
Memory-Induced Transformer architecture, OV2Seg, to first achieve
Open-Vocabulary VIS in an end-to-end manner with near real-time inference
speed. Extensive experiments on LV-VIS and four existing VIS datasets
demonstrate the strong zero-shot generalization ability of OV2Seg on novel
categories. The dataset and code are released here
https://github.com/haochenheheda/LVVIS.