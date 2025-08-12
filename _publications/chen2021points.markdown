---
layout: publication
title: 'Points As Queries: Weakly Semi-supervised Object Detection By Points'
authors: Liangyu Chen, Tong Yang, Xiangyu Zhang, Wei Zhang, Jian Sun
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: chen2021points
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.07434'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
We propose a novel point annotated setting for the weakly semi-supervised
object detection task, in which the dataset comprises small fully annotated
images and large weakly annotated images by points. It achieves a balance
between tremendous annotation burden and detection performance. Based on this
setting, we analyze existing detectors and find that these detectors have
difficulty in fully exploiting the power of the annotated points. To solve
this, we introduce a new detector, Point DETR, which extends DETR by adding a
point encoder. Extensive experiments conducted on MS-COCO dataset in various
data settings show the effectiveness of our method. In particular, when using
20% fully labeled data from COCO, our detector achieves a promising
performance, 33.3 AP, which outperforms a strong baseline (FCOS) by 2.0 AP, and
we demonstrate the point annotations bring over 10 points in various AR
metrics.