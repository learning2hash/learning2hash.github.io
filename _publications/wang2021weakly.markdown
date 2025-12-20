---
layout: publication
title: Weakly-supervised Instance Segmentation Via Class-agnostic Learning With Salient
  Images
authors: Xinggang Wang, Jiapei Feng, Bin Hu, Qi Ding, Longjin Ran, Xiaoxin Chen, Wenyu
  Liu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: wang2021weakly
citations: 34
additional_links: [{name: Code, url: 'https://github.com/hustvl/BoxCaseg'}, {name: Paper,
    url: 'https://arxiv.org/abs/2104.01526'}]
tags: ["CVPR", "Datasets", "Supervised"]
short_authors: Wang et al.
---
Humans have a strong class-agnostic object segmentation ability and can
outline boundaries of unknown objects precisely, which motivates us to propose
a box-supervised class-agnostic object segmentation (BoxCaseg) based solution
for weakly-supervised instance segmentation. The BoxCaseg model is jointly
trained using box-supervised images and salient images in a multi-task learning
manner. The fine-annotated salient images provide class-agnostic and precise
object localization guidance for box-supervised images. The object masks
predicted by a pretrained BoxCaseg model are refined via a novel merged and
dropped strategy as proxy ground truth to train a Mask R-CNN for
weakly-supervised instance segmentation. Only using \(7991\) salient images, the
weakly-supervised Mask R-CNN is on par with fully-supervised Mask R-CNN on
PASCAL VOC and significantly outperforms previous state-of-the-art
box-supervised instance segmentation methods on COCO. The source code,
pretrained models and datasets are available at
https://github.com/hustvl/BoxCaseg.