---
layout: publication
title: 'Shufflenet: An Extremely Efficient Convolutional Neural Network For Mobile
  Devices'
authors: Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, Jian Sun
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: zhang2017shufflenet
citations: 7618
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.01083'}]
tags: ["CVPR", "Efficiency"]
short_authors: Zhang et al.
---
We introduce an extremely computation-efficient CNN architecture named
ShuffleNet, which is designed specially for mobile devices with very limited
computing power (e.g., 10-150 MFLOPs). The new architecture utilizes two new
operations, pointwise group convolution and channel shuffle, to greatly reduce
computation cost while maintaining accuracy. Experiments on ImageNet
classification and MS COCO object detection demonstrate the superior
performance of ShuffleNet over other structures, e.g. lower top-1 error
(absolute 7.8%) than recent MobileNet on ImageNet classification task, under
the computation budget of 40 MFLOPs. On an ARM-based mobile device, ShuffleNet
achieves ~13x actual speedup over AlexNet while maintaining comparable
accuracy.