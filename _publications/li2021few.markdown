---
layout: publication
title: Few-shot Semantic Segmentation With Self-supervision From Pseudo-classes
authors: Yiwen Li, Gratianus Wesley Putra Data, Yunguan Fu, Yipeng Hu, Victor Adrian
  Prisacariu
conference: Arxiv
year: 2021
bibkey: li2021few
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.11742'}]
tags: ["Self-Supervised"]
short_authors: Li et al.
---
Despite the success of deep learning methods for semantic segmentation,
few-shot semantic segmentation remains a challenging task due to the limited
training data and the generalisation requirement for unseen classes. While
recent progress has been particularly encouraging, we discover that existing
methods tend to have poor performance in terms of meanIoU when query images
contain other semantic classes besides the target class. To address this issue,
we propose a novel self-supervised task that generates random pseudo-classes in
the background of the query images, providing extra training data that would
otherwise be unavailable when predicting individual target classes. To that
end, we adopted superpixel segmentation for generating the pseudo-classes. With
this extra supervision, we improved the meanIoU performance of the
state-of-the-art method by 2.5% and 5.1% on the one-shot tasks, as well as 6.7%
and 4.4% on the five-shot tasks, on the PASCAL-5i and COCO benchmarks,
respectively.