---
layout: publication
title: Integrative Few-shot Learning For Classification And Segmentation
authors: Dahyun Kang, Minsu Cho
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: kang2022integrative
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.15712'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Dahyun Kang, Minsu Cho
---
We introduce the integrative task of few-shot classification and segmentation
(FS-CS) that aims to both classify and segment target objects in a query image
when the target classes are given with a few examples. This task combines two
conventional few-shot learning problems, few-shot classification and
segmentation. FS-CS generalizes them to more realistic episodes with arbitrary
image pairs, where each target class may or may not be present in the query. To
address the task, we propose the integrative few-shot learning (iFSL) framework
for FS-CS, which trains a learner to construct class-wise foreground maps for
multi-label classification and pixel-wise segmentation. We also develop an
effective iFSL model, attentive squeeze network (ASNet), that leverages deep
semantic correlation and global self-attention to produce reliable foreground
maps. In experiments, the proposed method shows promising performance on the
FS-CS task and also achieves the state of the art on standard few-shot
segmentation benchmarks.